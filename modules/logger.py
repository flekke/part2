import os
from datetime import datetime

# 로그 파일 경로 설정
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # modules 상위 디렉토리(root 폴더)
log_file = os.path.join(root_dir, "logs.txt")  # root 폴더 안의 logs.txt 파일

# 로그를 파일에 쓰는 함수
def log_to_file(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:  # 파일을 append 모드로 열기
        file.write(f"{timestamp} - {level} - {message}\n")

# 로그 함수 래핑
def log_info(message):
    log_to_file("INFO", message)

def log_error(message):
    log_to_file("ERROR", message)
