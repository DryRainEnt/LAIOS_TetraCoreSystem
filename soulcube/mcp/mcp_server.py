# MCP 서버 Stub
# 파일/명령/네트워크 요청 처리 (Stub)

class MCPServer:
    def read_file(self, filepath):
        """파일 읽기 Stub"""
        return f"[파일읽기]{filepath}"

    def write_file(self, filepath, data):
        """파일 쓰기 Stub"""
        return f"[파일쓰기]{filepath}:{data}"

    def run_command(self, command):
        """명령 실행 Stub"""
        return f"[명령실행]{command}"

    def send_network_request(self, url, payload):
        """네트워크 요청 Stub"""
        return f"[네트워크요청]{url}:{payload}"
