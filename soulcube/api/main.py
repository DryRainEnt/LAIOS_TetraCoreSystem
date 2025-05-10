# FastAPI 엔트리포인트
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from soulcube.agents.interface_agent import InterfaceAgent
from soulcube.agents.core_cognition import CoreCognition
from soulcube.agents.mechanism_layer import MemoryAgent, SensationAgent, ActionAgent
from soulcube.memory.memory_agent import MemoryAgent as GlobalMemoryAgent
from soulcube.mcp.mcp_server import MCPServer

app = FastAPI()

# 정적 파일 서빙
import os
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../static'))
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/dashboard")
def dashboard():
    return FileResponse(os.path.join(static_dir, "dashboard.html"))

# 입력 데이터 모델
from typing import Dict, Any, Optional
class UserInput(BaseModel):
    content: str
    agent_settings: Optional[Dict[str, Dict[str, str]]] = None

# 에이전트 인스턴스 (실제 구현에선 DI/싱글턴 등 고려)
interface_agent = InterfaceAgent()
core_cognition = CoreCognition()
memory_agent = MemoryAgent()
sensation_agent = SensationAgent()
action_agent = ActionAgent()
global_memory = GlobalMemoryAgent()
mcp_server = MCPServer()

@app.get("/")
def root():
    return {"message": "SoulCube API is running."}

import openai
import httpx
import asyncio

import os

def get_llm_response(model: str, api_key: str, prompt: str) -> str:
    try:
        # 우선순위: 함수 인자 > 환경변수
        if model.startswith('gpt-'):  # OpenAI (v1.x)
            import openai
            key = api_key or os.getenv('OPENAI_API_KEY')
            if not key:
                return '[LLM Error] OpenAI API 키가 없습니다.'
            client = openai.OpenAI(api_key=key)
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=256,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        elif model.startswith('claude-'):  # Anthropic Claude
            key = api_key or os.getenv('ANTHROPIC_API_KEY')
            if not key:
                return '[LLM Error] Anthropic API 키가 없습니다.'
            headers = {
                'x-api-key': key,
                'anthropic-version': '2023-06-01',
                'content-type': 'application/json'
            }
            anthropic_model = model
            payload = {
                "model": anthropic_model,
                "max_tokens": 256,
                "temperature": 0.7,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
            url = "https://api.anthropic.com/v1/messages"
            resp = httpx.post(url, headers=headers, json=payload, timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                return data["content"][0]["text"] if "content" in data and data["content"] else ""
            else:
                return f"[Claude Error] {resp.text}"
        else:
            return f"[지원하지 않는 모델] {model}"
    except Exception as e:
        return f"[LLM Error] {str(e)}"

@app.post("/api/user_input")
def user_input(input: UserInput):
    summary = interface_agent.handle_user_input(input.content)
    settings = input.agent_settings or {}
    # 2. 사고계층이 판단 (논리/감정/윤리)
    def agent_llm(agent, prompt, fallback):
        s = settings.get(agent, {})
        model = s.get('model')
        api_key = s.get('apiKey')
        if model and api_key:
            return get_llm_response(model, api_key, prompt)
        return fallback(prompt)
    logos = agent_llm('logos', summary, core_cognition.process_logos)
    pathos = agent_llm('pathos', summary, core_cognition.process_pathos)
    ethos = agent_llm('ethos', summary, core_cognition.process_ethos)
    # 3. 행동계층이 판단 및 MCP 호출
    memory_result = memory_agent.query_knowledge(summary)
    sensation_result = sensation_agent.analyze_input(summary)
    action_plan = action_agent.plan_action({
        "logos": logos, "pathos": pathos, "ethos": ethos,
        "memory": memory_result, "sensation": sensation_result
    })
    mcp_result = action_agent.call_mcp(action_plan)
    # 4. 결과 반환
    return {
        "summary": summary,
        "logos": logos,
        "pathos": pathos,
        "ethos": ethos,
        "memory": memory_result,
        "sensation": sensation_result,
        "action_plan": action_plan,
        "mcp_result": mcp_result
    }
