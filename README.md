네, 알겠습니다. 프로젝트를 독립적이고 깔끔하게 관리하기 위해 \*\*가상 환경(Virtual Environment)\*\*을 사용하는 것은 매우 좋은 방법입니다.

기존 `README.md` 파일의 **4. 설치 (Installation)** 와 **5. 사용법 (Usage)** 부분을 가상 환경 기준으로 다시 작성해 드리겠습니다.

-----

# Drain 알고리즘 로그 파싱 예제 (Drain Algorithm Log Parsing Example)

[](https://www.python.org/downloads/)
[](https://opensource.org/licenses/MIT)

`logpai/logparser` 라이브러리의 Drain 알고리즘을 활용하여 비정형 로그 메시지를 구조화된 \*\*템플릿(Template)\*\*과 \*\*파라미터(Parameter)\*\*로 분리하는 간단한 Python 예제 프로젝트입니다.

## 1\. 개요 (Overview)

로그 데이터는 시스템의 상태를 파악하고 문제를 해결하는 데 필수적이지만, 대부분 비정형 텍스트 형태로 되어 있어 분석이 어렵습니다. 이 프로젝트는 Drain 알고리즘을 통해 이러한 로그들을 자동으로 파싱하여, 다음과 같이 구조화하는 방법을 보여줍니다.

  - **원본 로그**: `INFO: User 'alice' connected from 192.168.1.10`
  - **파싱 결과**:
      - **템플릿**: `INFO: User <_> connected from <_>`
      - **파라미터**: `['alice', '192.168.1.10']`

이렇게 구조화된 로그는 저장 공간을 효율적으로 사용하고, 검색 및 통계 분석, 이상 징후 탐지 등 고급 분석의 기반이 됩니다.

## 2\. 주요 기능

  - Drain 알고리즘을 이용한 로그 템플릿 추출
  - 정규표현식을 활용한 사전 파라미터 식별
  - Pandas DataFrame을 이용한 깔끔한 결과 출력

## 3\. 사전 준비 (Prerequisites)

  - Python 3.7 이상

## 4\. 설치 및 환경 설정 (Installation & Setup)

프로젝트의 의존성을 시스템 전역이 아닌, 독립된 가상 환경에 설치하여 관리합니다.

1.  **저장소(Repository)를 로컬 환경에 복제(Clone)합니다.**

    ```bash
    git clone https://github.com/your-username/log-parsing-example.git
    cd log-parsing-example
    ```

2.  **Python 가상 환경을 생성합니다.**
    프로젝트 폴더 내에 `venv`라는 이름의 가상 환경을 생성합니다.

    ```bash
    python3 -m venv venv
    ```

3.  **가상 환경을 활성화합니다.**
    활성화 명령어는 사용 중인 운영체제에 따라 다릅니다.

      - **macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```
      - **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```

    *가상 환경이 활성화되면 터미널 프롬프트 앞에 `(venv)`가 표시됩니다.*

4.  **필요한 라이브러리를 가상 환경 내에 설치합니다.**
    프로젝트에 포함된 `requirements.txt` 파일을 사용하여 필요한 라이브러리를 설치합니다.

    ```bash
    pip3 install -r requirements.txt
    ```

    *(참고: `requirements.txt` 파일 내용은 다음과 같습니다.)*

    ```
    # requirements.txt
    logparser
    pandas
    ```

## 5\. 사용법 (Usage)

1.  **가상 환경 활성화 확인**
    스크립트를 실행하기 전, 터미널 프롬프트 앞에 `(venv)`가 표시되어 가상 환경이 활성화된 상태인지 확인합니다. 활성화되어 있지 않다면 위의 4-3 단계를 다시 수행해주세요.

2.  **스크립트 실행**
    가상 환경이 활성화된 터미널에서 메인 스크립트 파일을 실행합니다.

    ```bash
    python3 main.py
    ```

3.  **가상 환경 비활성화**
    작업이 끝나면 아래 명령어를 입력하여 가상 환경을 빠져나옵니다.

    ```bash
    deactivate
    ```

## 6\. 실행 결과 (Example Output)

```
================================================================================
### 로그 파싱 결과 (DataFrame) ###
================================================================================
   log_id  template_id                                           template                                  parameters
0       1            1          INFO: User <_> connected from <_>          ['alice', '192.168.1.10']
1       2            1          INFO: User <_> connected from <_>            ['bob', '192.168.1.12']
2       3            2  WARN: Auth failed for user <_>; reason: invalid ...                        ['charlie']
3       4            2  WARN: Auth failed for user <_>; reason: account ...                          ['david']
4       5            3         INFO: Service <_> started successfully                         ['AuthService']

================================================================================
### 발견된 고유 템플릿 목록 ###
================================================================================
ID 1: INFO: User <_> connected from <_>
ID 2: WARN: Auth failed for user <_>; reason: invalid password
ID 3: INFO: Service <_> started successfully
================================================================================
```

## 7\. 핵심 기술 (Underlying Technology)

  - **Logparser Library**: [logpai/logparser](https://github.com/logpai/logparser)
  - **Drain Algorithm**: [Drain: An Online Log Parsing Approach with Fixed Depth Tree (Paper)](https://www.google.com/search?q=https://www.cs.utah.edu/~lifeifei/papers/drain.pdf)

## 8\. 라이선스 (License)

이 프로젝트는 [MIT 라이선스](https://opensource.org/licenses/MIT)를 따릅니다.