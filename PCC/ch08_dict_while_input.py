def make_album(name, title) : # make_album() 함수를 매개변수로 name, title 을 받도록 정의
    album = f"{name}, {title}" # 두 매개변수를 조합하고 콤마를 삽입해 album에 할당
    return album.title()
# print(make_album) # 이렇게 해버리면 함수야 출력이 되겠지만 여기서 의도한 바는 그게 아님

while True: # while 값을 True로 지정하지 않으면 루프가 시작이 안 됨
    print("\nPlease input the singer name.")
    print("Enter 'q' if you want to stop.")

    name = input("name : ") # 대입은 = (하나)
    if name == 'q' : # 같은지 평가는 == (둘)
        break

    title = input("title : ")
    if title == 'q':
        break

    album = make_album(name,title)
    print(f"Here you are, <{album}>.")

