def make_album(name, title, number="") : # 인수를 옵션으로 만들때는 함수의 매개변수 중 제일 마지막 순서로 해당 인수를 위치시키고 ="" 를 달아줘야함
    album = {"singer_name" : name, "album_title" : title, "song_number" : number}  # 딕셔너리의 키-값에서 값은 당연히 함수의 매개변수, 키는 자유롭게 명명
    
    if number :
        album = f"{name} {title} {number}"
    else : 
        album = f"{name} {title}"
    
    # return album.title() # 이렇게 하면 첫글자 대문자
    # return (album) # 이런 형태로 출력해도 되고
    return album # 이렇게 해도 됨

case_1 = make_album("ann", "first song", 2)
case_2 = make_album("ben", "next song", 3)
case_3 = make_album("cindy", "last song") # 굳이 없는 인수를 None 으로 써줄 필요는 없지만, 써주어도 출력값은 의도대로 cindy, last song 이 나옴

print(case_1)
print(case_2)
print(case_3)



