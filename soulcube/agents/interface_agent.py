# Interface Agent
# 사용자 입력을 받아 요약/정리 및 사고 계층으로 전달

class InterfaceAgent:
    def handle_user_input(self, input_data):
        """사용자 입력 처리 및 요약"""
        # 실제로는 NLP 요약, 토큰화 등. 여기선 단순 반환
        return f"[요약]{input_data}"

    def summarize_and_forward(self, summary):
        """요약 결과를 사고 계층에 전달 (데모용)"""
        return summary
