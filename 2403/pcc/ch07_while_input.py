# responses = {}

# polling_active = True

# while polling_active:
#     name = input("\nWhat's your name?")
#     response = input("\nWhat's your favorite color?")

#     responses[name] = response

#     repeat = input("Another people? (y/n)")
#     if repeat == 'n':
#         polling_active = False

    
# print("\n---Result---")
# for name, response in responses.items():
#     print(f"{name} likes {response} color.")


answer = {}

survey_active = True

while survey_active:
    first = input("Input your name.")
    second = input("Input your job.")

    # answer 라는 딕셔너리의 first 키에 second라는 값을 저장하는 과정을 반복 
    answer[first] =  second
    
    # 이 단계를 거치지 않으면 while 루프 탈출 불가
    repeat = input("Finished?(y/n)")
    if repeat == 'y':
        survey_active = False

print("==Result==")
for first, second in answer.items():
    print(f"{first.title()}, you are {second}.")
