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
