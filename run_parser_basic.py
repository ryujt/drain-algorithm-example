# 파일명: run_parser_basic.py

import pandas as pd
from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig

# --- 1. 설정 및 파서 초기화 ---

config = TemplateMinerConfig()
config.drain_sim_th = 0.5
config.drain_depth = 4
# [핵심 변경] 사전 규칙을 전혀 정의하지 않음 (제로 베이스)
config.drain_extra_delimiters = []

parser = TemplateMiner(config=config)


# --- 2. 파싱할 원본 로그 데이터 (규칙 없는 한글 로그 추가) ---
raw_logs = [
    "INFO: User 'alice' connected from 192.168.1.10",
    "INFO: User 'bob' connected from 192.168.1.12",
    "WARN: Auth failed for user 'charlie'; reason: invalid password",
    "WARN: Auth failed for user 'david'; reason: account locked",
    "INFO: Service 'AuthService' started successfully",
    "[WARN] 폴더 /usr/local/bin 에 대한 권한이 없습니다.",
    "[WARN] 폴더 /var/log 에 대한 권한이 없습니다."
]

# --- 3. 로그 파싱 및 결과 출력 ---
parsed_results = []
for log_message in raw_logs:
    result = parser.add_log_message(log_message)
    template = result['template_mined']
    params = parser.get_parameter_list(template, log_message)
    parsed_results.append({
        'log_id': len(parsed_results) + 1, 'template_id': result['cluster_id'],
        'template': template, 'parameters': params, 'original_log': log_message
    })

df = pd.DataFrame(parsed_results)
print("### [run_parser_basic.py] 실행 결과 ###")
print(df[['template_id', 'template', 'parameters']])