import pytest
from fastapi.testclient import TestClient
from soulcube.api.main import app

client = TestClient(app)

def test_user_input_stub_llm(monkeypatch):
    # 더미 LLM 호출로 강제 (실제 external call 차단)
    monkeypatch.setattr('soulcube.api.main.get_llm_response', lambda m, k, p: f"[MOCK LLM] {m} {p}")
    data = {
        "content": "테스트 메시지",
        "agent_settings": {
            "logos": {"model": "gpt-3.5-turbo", "apiKey": "dummy"},
            "pathos": {"model": "claude-3-opus", "apiKey": "dummy"},
            "ethos": {"model": "gpt-4", "apiKey": "dummy"}
        }
    }
    resp = client.post("/api/user_input", json=data)
    assert resp.status_code == 200
    result = resp.json()
    assert result["logos"].startswith("[MOCK LLM]")
    assert result["pathos"].startswith("[MOCK LLM]")
    assert result["ethos"].startswith("[MOCK LLM]")
    assert "summary" in result and result["summary"]
    assert "memory" in result and result["memory"]
    assert "action_plan" in result and result["action_plan"]

def test_user_input_no_llm(monkeypatch):
    # LLM 설정 없이 기존 더미 함수로 동작
    data = {"content": "테스트 메시지", "agent_settings": {}}
    resp = client.post("/api/user_input", json=data)
    assert resp.status_code == 200
    result = resp.json()
    # 더미 함수 결과가 반환되는지 확인
    assert not result["logos"].startswith("[MOCK LLM]")
    assert not result["pathos"].startswith("[MOCK LLM]")
    assert not result["ethos"].startswith("[MOCK LLM]")
