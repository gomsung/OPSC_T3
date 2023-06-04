# OPSC_T3


과제


사용자로부터 자연어 질의를 입력받으면 그에 대한 답을 그림으로 그려주는 시스템을 구현  *Github에서 관리해야 함
 
ChatGPT와 DALL-E를 활용하되, 그림으로 바로 표현하기 어려운 자연어 답의 경우 자연어 답을 가공하여 DALL-E에게 넘겨주거나 사용자에게 다시 묻는 등의 과정이 필요



##### api_key에 발급 받은 개인키 사용
  




ChatGPT
  
    입력: 자연어 질의

    출력: 자연어 답
  DALL-E

    입력: 자연어 답

    출력 : 그림


# 추가 기능

 *목적 : 맞춤 운동 제시
 
 *api_key를 input으로 받아서 사용
 
 *구현 = streamlit

 *csvkit 기능 추가
    csvkit fork  https://github.com/gomsung/OS_csvkit.git



## csvkit 기능
csvlook:

    • csvlook filename.csv와 같이 사용하여 CSV 데이터를 테이블 형식으로 출력합니다.
    
    • 출력 결과는 행과 열로 구성된 테이블로, 데이터 구조를 시각화하여 파악할 수 있습니다.
    
csvsort:

    • csvsort -c column_name filename.csv와 같이 사용하여 특정 열을 기준으로 CSV 파일을 정렬합니다.
    
    • -c옵션을 사용하여 정렬할 열을 지정하고, column_name에는 해당 열의 이름을 입력합니다.
    
    • 기본적으로 오름차순으로 정렬되며, -r옵션을 추가하면 내림차순으로 정렬할 수 있습니다.
csvcut:

    • csvcut -c column_name filename.csv와 같이 사용하여 특정 열을 선택하여 새로운 CSV 파일을 생성합니다.
    
    • -c옵션을 사용하여 선택할 열을 지정하고, column_name에는 해당 열의 이름을 입력합니다.
    
    • 여러 개의 열을 선택하려면 쉼표로 구분하여 열 이름을 나열합니다.
    
csvgrep:

    • csvgrep -c column_name -m pattern filename.csv와 같이 사용하여 특정 조건에 맞는 행을 필터링하여 새로운 CSV 파일을 생성합니다.
    
    • -c옵션을 사용하여 필터링할 열을 지정하고, -m옵션을 사용하여 필터링할 패턴을 입력합니다.
    
    • pattern에는 필터링할 패턴을 정규 표현식으로 입력합니다.
    
csvjoin:

    • csvjoin -c column_name file1.csv file2.csv와 같이 사용하여 두 개의 CSV 파일을 조인하여 하나의 파일로 결합합니다.
    
    • -c옵션을 사용하여 조인할 열을 지정하고, column_name에는 공통 열의 이름을 입력합니다.
    
    • 조인 작업은 공통 열의 값을 기준으로 수행됩니다.
    
csvstack:

    • csvstack file1.csv file2.csv와 같이 사용하여 여러 개의 CSV 파일을 수직으로 결합하여 하나의 파일로 생성합니다.
    
    • 파일들은 입력한 순서대로 결합되며, 각각의 파일은 동일한 열 구조를 가져야 합니다.
    
csvformat:

    • csvformat -D ';' -U 1 filename.csv와 같이 사용하여 CSV 파일의 형식을 변경합니다.
    
    • -D옵션을 사용하여 필드 구분자를 지정하고, -U옵션을 사용하여 따옴표 사용 여부를 설정합니다.
    
    • 다양한 옵션을 사용하여 CSV 파일의 형식을 조정할 수 있습니다.
    
csvstat:

    • csvstat filename.csv와 같이 사용하여 CSV 파일의 통계 정보를 출력합니다.
    
    • 각 열의 데이터 유형, 최솟값, 최댓값, 평균 등을 확인할 수 있습니다.
    
csvsql:

    • csvsql --query "SELECT * FROM filename.csv" -o output.csv와 같이 사용하여 SQL 쿼리를 사용하여 CSV 파일을 처리합니다.
    
    • --query옵션을 사용하여 실행할 SQL 쿼리를 입력하고, -o옵션을 사용하여 출력 파일을 지정합니다.
    
    • 데이터베이스처럼 쿼리를 실행하여 데이터를 조작할 수 있습니다.
    
