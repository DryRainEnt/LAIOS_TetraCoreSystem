# SoulCube

계층적 분산 인격 아키텍처 기반 AI 시스템

## 프로젝트 목적
- LLM 기반의 사고·기억·감각·행동·윤리 통합 지능체 실험
- 계층별 메시지 및 권한 구조, 자기검열/회고/다중 가치 기반 판단 구현

## 주요 구조
- agents/: 인터페이스, 사고계층, 행동계층 에이전트
- mcp/: MCP 서버 Stub (파일/명령/네트워크)
- memory/: 기억/지식 저장 및 중계
- api/: FastAPI 기반 REST 엔트리포인트
- tests/: 테스트 코드

## 실행 방법
```bash
pip install -r requirements.txt
uvicorn soulcube.api.main:app --reload
```

## 배포 (Docker)
```bash
docker build -t soulcube .
docker run -p 8000:8000 soulcube
```

---

본 프로젝트는 실험적 분산 인격 AI 구조의 프로토타입입니다.
