# Core Cognition (Logos, Pathos, Ethos)
# 논리, 감정, 윤리 판단 담당

class CoreCognition:
    def process_logos(self, input_data):
        """논리적 판단"""
        return f"[논리판단]{input_data}"

    def process_pathos(self, input_data):
        """감정적 판단"""
        return f"[감정판단]{input_data}"

    def process_ethos(self, input_data):
        """윤리적 판단"""
        return f"[윤리판단]{input_data}"
