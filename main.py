import pandas as pd
from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig


# --- 1. 설정 및 파서 초기화 ---

# [수정 1] TemplateMinerConfig 객체를 생성하고 속성을 직접 설정합니다.
config = TemplateMinerConfig()
config.drain_sim_th = 0.5  # 유사도 임계값
config.drain_depth = 4     # 탐색 트리 깊이
config.drain_extra_delimiters = [ # 파라미터 식별을 위한 정규식
    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
    r'\'(.*?)\''
]

# 설정 객체를 전달하여 TemplateMiner를 생성합니다.
parser = TemplateMiner(config=config)


# --- 2. 파싱할 원본 로그 데이터 ---

raw_logs = [
    "INFO: User 'alice' connected from 192.168.1.10",
    "INFO: User 'bob' connected from 192.168.1.12",
    "WARN: Auth failed for user 'charlie'; reason: invalid password",
    "WARN: Auth failed for user 'david'; reason: account locked",
    "INFO: Service 'AuthService' started successfully"
]


# --- 3. 로그 파싱 실행 ---

# 파싱 결과를 저장할 리스트
parsed_results = []

for log_message in raw_logs:
    result = parser.add_log_message(log_message)
    template = result['template_mined']
    
    # [수정 2] 라이브러리에 내장된 메서드를 사용하여 파라미터를 추출합니다.
    params = parser.get_parameter_list(template, log_message)

    # 결과 저장
    parsed_results.append({
        'log_id': len(parsed_results) + 1,
        'template_id': result['cluster_id'],
        'template': template,
        'parameters': params,
        'original_log': log_message
    })


# --- 4. 결과 출력 ---

# Pandas DataFrame을 사용하여 결과를 깔끔하게 출력
df = pd.DataFrame(parsed_results)

print("=" * 80)
print("### 로그 파싱 결과 (DataFrame) ###")
print("=" * 80)
print(df[['log_id', 'template_id', 'template', 'parameters']])


print("\n" + "=" * 80)
print("### 발견된 고유 템플릿 목록 ###")
print("=" * 80)
# 'template_id'를 기준으로 중복을 제거하고 출력
unique_templates = df.drop_duplicates(subset='template_id').sort_values('template_id')
for index, row in unique_templates.iterrows():
    print(f"ID {row['template_id']}: {row['template']}")
print("=" * 80)