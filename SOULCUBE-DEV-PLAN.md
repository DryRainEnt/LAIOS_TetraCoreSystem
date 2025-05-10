# SoulCube 개발 계획서 (MCP/기억 권한 구조 반영)

## 1. 주요 설계 변경점

- **MCP 사용 권한**  
  행동계층(3단계: Memory, Sensation, Action) 에이전트 모두 MCP 서버에 직접 접근 및 명령 실행 가능.

- **기억 에이전트의 지식/기억 중계**  
  상위 사고계층(2단계: Logos, Pathos, Ethos)은 직접 MCP 접근은 불가.  
  대신, Memory 에이전트를 통해 필요한 지식/기억(벡터 DB, 세션 로그 등)에 무제한 접근 가능.

---

## 2. 시스템 아키텍처 및 권한 구조

```
[User] → [UI Agent] → [Logos | Pathos | Ethos]
                                 ↓
                             [Memory | Sensation | Action]
                                 ↓        ↓        ↓
                              [MCP 서버] (모두 직접 접근)
```
- **Logos/Pathos/Ethos**: Memory 에이전트에 쿼리하여 지식/기억을 획득(무제한)
- **Memory/Sensation/Action**: MCP 서버에 직접 파일/명령/네트워크 등 요청 가능

---

## 3. 개발 범위 및 목표

1. 계층 구조 및 에이전트별 권한 구현
2. MCP 서버 Stub/Mock(파일/명령/네트워크) 구현
3. Memory 에이전트의 지식/기억 중계 기능 구현
4. 상위 사고계층이 Memory를 통해 지식/기억을 쿼리하는 API/함수 설계
5. 전체 메시지/상태 흐름 구현 및 통합
6. 최소한의 테스트 및 예시 시나리오
7. 로컬 환경에서 실행 및 배포(Docker, FastAPI 등)

---

## 4. 개발 단계별 계획

### 1단계: 기본 구조 및 권한 모델 구현
- Python 패키지/디렉토리 구조 설계
- 각 계층별 에이전트 클래스/모듈 구현
- 에이전트별 권한(메서드/인터페이스) 명확히 분리

### 2단계: MCP 서버 Stub 및 연결
- MCP 서버 Mock: 파일 읽기/쓰기, 명령 실행, 네트워크 요청 등
- 행동계층 에이전트에서 MCP 직접 호출 기능

### 3단계: Memory 에이전트 중계/저장소 구현
- 벡터 DB 또는 간단한 DB/딕셔너리로 기억/지식 저장
- 상위 사고계층이 Memory에 쿼리하는 API/함수 제공

### 4단계: 메시지/상태 흐름 통합
- 사용자 입력 → UI → 사고계층 → 행동계층 → MCP → 결과 반환
- 사고계층은 Memory를 통해 지식/기억 무제한 조회

### 5단계: 테스트 및 예시 시나리오
- 각 계층별 단위 테스트
- 전체 플로우 통합 테스트
- 예시: “파일 내용 요약”, “명령 실행 결과 회고” 등

### 6단계: 배포 환경 구축
- Dockerfile, requirements.txt, README 작성
- FastAPI/Flask 등 REST API 서버화
- 로컬 실행 및 배포

---

## 5. 예시 디렉토리/모듈 구조

```
soulcube/
  ├── agents/
  │     ├── interface_agent.py
  │     ├── core_cognition.py
  │     └── mechanism_layer.py
  ├── mcp/
  │     └── mcp_server.py
  ├── memory/
  │     └── memory_agent.py
  ├── api/
  │     └── main.py
  ├── tests/
  ├── Dockerfile
  ├── requirements.txt
  └── README.md
```

---

## 6. 기술 스택

- Python 3.10+
- FastAPI (REST API)
- Docker (배포)
- (선택) Chroma/Pinecone 등 Vector DB
- (Stub) MCP 서버: Python 모듈로 구현

---

## 7. 배포 및 실행

- `docker build .`
- `docker run -p 8000:8000 soulcube`
- (로컬) `uvicorn api.main:app --reload`

---

## 8. 향후 확장

- 실제 LLM 연동, 외부 API 연동
- Vector DB 고도화, 세션 회고 자동화
- 권한/감정/윤리 정책 세분화
