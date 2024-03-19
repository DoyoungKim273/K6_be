# number = input("How old are you?")

# # 입력된 값이 문자열로 처리됨 - 파이썬은 문자열과 정수 비교 불가, int로 type casting 해주어야함
# # 연산이나 비교를 위해 숫자 입력을 받을때는 먼저 입력을 숫자로 변환해주어야함

# number = int(number)

# if number > 10 :
#     print("come in")
# else :
#     print("get out")

prompt = "\n Tell me someting."
prompt += "\n Enter 'quit' if you want to stop."

# message = ""

# while message != 'quit':
#     message = input(prompt)
#     # print(message)

#     if message != 'quit':
#         print(message)
#     # while 문만 사용시에는 프로그램의 종료값인 quit이 메시지처럼 출력되는 단점 있음
#     # if 문으로 프로그램이 메시지 출력 전 종료값과 일치하는지 확인하고 일치X 경우에만 메시지를 출력함

# 여러 조건을 통과해야만 프로그램을 실행하는 경우, 전체 프로그램의 실행 여부 결정하는 변수(플래그) 정의 가능
# 프로그램에 대한 일죵의 신호 역할
# 플래그가 True 이면 실행 계속, False 이면 실행 중지
# 플래그의 이름은 아무렇게나 지어도 됨 

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False

    else :
        print(message)