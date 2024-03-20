def get_city_country(city, country):
    full_infor = f"{city} , {country}" # 애초에 이걸 while문 밖에 선언해줘야 하는 이유는? : 그게 원래 함수의 형식이니까!
    return full_infor.title()

while True:
    print("\nPlease tell me your city.")
    print("(enter 'q' at any time to quit.)")

    city = input("City : ") # 인수는 input 으로 전달
    if city == 'q':
        break # 마디 마다 break 문 걸어줘야 무한 루프를 안 돌긴 하지만, 어차피 city 뒤에 country 입력해야만 하는 상황이라면 굳이 break 안 달아줘도 됨

    country = input("Country : ")
    if country == 'q':
        break

    full_infor = get_city_country(city, country) # while 문 안에서 print 를 해주어야 하기에 다시 선언해줄 필요가 있음
    print(full_infor) 

    print(f"Hello, {city}, {country}") # 콤마로 나눠서 출력하기 위해 쓰는 형태이며, 이 경우에는 굳이 full_infor로 선언할 필요가 없음
