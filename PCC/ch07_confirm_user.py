# 미확인 사용자 리스트의 사용자를 확인된 사용자를 저장할 빈 리스트로 옮겨준다
unconfirmed_users = ['amy', 'ben', 'cate']
confirmed_users = []

# 미확인 사용자가 한명도 남아있지 않을때 까지 계속해서 pop 으로 옮기기 진행
while unconfirmed_users:
    current_users = unconfirmed_users.pop()

# 현재 이용자를 계속해서 출력하고 그것을 확인된 이용자 목록에 추가해줌
    print(f"Verifying user : {current_users.title()}")
    confirmed_users.append(current_users)

# 확인된 이용자들의 목록에서 확인된 이용자를 각 한명씩 출력함
print("confirmed users : ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

