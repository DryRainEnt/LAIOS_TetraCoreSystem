# Memory Agent
# 모든 계층의 지식/기억 접근 중계

class MemoryAgent:
    def __init__(self):
        self.memory_store = {}

    def query(self, key):
        """지식/기억 조회"""
        return self.memory_store.get(key, f"[글로벌기억없음]{key}")

    def store(self, key, value):
        """지식/기억 저장"""
        self.memory_store[key] = value
        return f"[글로벌기억저장]{key}:{value}"
