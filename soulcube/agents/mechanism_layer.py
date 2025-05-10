# Mechanism Layer (Memory, Sensation, Action)
# 하위 행동 계층 및 MCP 접근 담당

class MemoryAgent:
    def query_knowledge(self, query):
        """지식/기억 쿼리 및 저장"""
        return f"[기억조회]{query}"

    def write_memory(self, data):
        """기억 저장"""
        return f"[기억저장]{data}"

class SensationAgent:
    def analyze_input(self, input_data):
        """입력 데이터/파일 분석"""
        return f"[감각분석]{input_data}"

class ActionAgent:
    def plan_action(self, context):
        """실질적 출력/행동 계획"""
        return f"[행동계획]{context}"

    def call_mcp(self, command):
        """MCP 서버 직접 호출"""
        return f"[MCP호출]{command}"
