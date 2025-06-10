# 파일명: run_parser_with_rules.py

import pandas as pd
from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig

# --- 1. 설정 및 파서 초기화 ---

config = TemplateMinerConfig()
config.drain_sim_th = 0.5
config.drain_depth = 4
# [핵심] IP, 따옴표 등 명확한 규칙을 사전에 정의
config.drain_extra_delimiters = [
    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
    r'\'(.*?)\''
]
parser = TemplateMiner(config=config)

# --- 2. 파싱할 원본 로그 데이터 ---
raw_logs = [
    "INFO: User 'alice' connected from 192.168.1.10",
    "INFO: User 'bob' connected from 192.168.1.12",
    "WARN: Auth failed for user 'charlie'; reason: invalid password",
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
print("### [run_parser_with_rules.py] 실행 결과 ###")
print(df[['template_id', 'template', 'parameters']])