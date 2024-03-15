def greet_user():
    print("Hello")

greet_user()

def answer_user(answer) : # 매개변수 answer 
    print(answer) # 문자열과 함께 출력하는게 아니면 중괄호도 써줄 필요가 없다는 점!
answer_user("Hi") # 인수 "Hi"

def describe_person(name, age) :
    print(name, age)

describe_person("Amy", 21)
describe_person("ben", 34) # 함수는 필요한 만큼 호출 할 수 있음(단, 위치 인수이기에 인수의 위치가 중요)
describe_person(age = 56, name = "cate") # 키워드 인수를 활용했기에 인수의 위치가 달라도 출력값은 제대로 나옴

def describe_animal(age, name, breed = "jindo"): # 기본값이 있는 매개변수는 항상 기본값이 없는 매개변수보다 뒤에 선언해야함
    print(breed, age, name)

describe_animal(age = 2, name = "jack")
# describe_animal(name = "jack") 하나의 print에 출력을 하려면 당연히 하나의 괄호 안에 인수들을 전달해줘야함

def full_name(first, last) :
    full_name_ver = f"{first} {last}" 
    return full_name_ver.title()
    
user_name = full_name("dan", "drake" )
# 값을 반환하는 함수를 호출할때는 반환값을 할당하는 변수를 지정해줘야함(full_name 함수 호출 위해 return 값 할당 하는 변수 user_name 지정)
print(user_name) # 반환값을 할당해둔 변수를 프린트 -- fullname의 반환값인 fullname_ver이 호출됨

def shirt(size, color) : 
    shirt_info = f"{size} {color}"
    return shirt_info

my_shirt = shirt("S", "red")

print(my_shirt)

def note(page, color): # 함수 note는 page, color을 매개변수로 가지고 note_infor라는 반환값을 가진다
    note_infor = f"{page} {color}"
    return note_infor

my_note = note(100, "blue") 
# 함수 note의 반환값 note_infor가 할당된 변수인 my_note가 생기고 이는 구체적인 page, size 인수를 받는다
print(my_note) # 반환값이 할당되었으며 구체적인 인수룰 받은 my_note에 저장된 값들이 출력된다

def bus(color, num, size = ""): # size 값을 옵션으로 만들기 위해 빈 문자열을 지정하고 매개변수의 순서에서 맨 뒤로 밀음
    
    if size : 
        bus_infor = f"{size} {color} {num}"
    else : 
        bus_infor = f"{color} {num}"
    return bus_infor

my_bus = bus("orange", 1008)
print(my_bus)

def dic(brand, price): # dic 함수는 brand 와 price를 받고
    dictionary = {'my_brand' : brand, 'my_price' : price} # 이 값을 딕셔너리에 저장(키 : 값)
    return dictionary # 딕셔너리를 반환

my_dic = dic("munwha", 50000) # 반환값이 할당되는 변수 = 함수명(인수)
print(my_dic) # 반환값 할당된 변수 출력

def fruit(color, price, made_in = None): # None은 일종의 플레이스 홀더(자리를 만들어 두는 것, 항상 대문자로 시작하는 예약어)
    apple = {"my_color" : color, "my_price" : price} # 딕셔너리의 키 : 함수의 매개변수(인수라는 값이 들어올 예정)
    if made_in :
        apple["my_made_in"] = made_in 
        # from은 예약어이기에 쓸 수 없다(변수 선언 하늘색이 아니면 그건 변수로 쓸 수 없는 값)
        # 딕셔너리의 키는 대괄호 안에 들어간다
        # 딕셔너리의 키에 값을 선언해주는데, 여기서 왜 바로 korea를 써주면 안되냐면 딕셔너리의 키 값이 함수의 매개변수라고 선언해줘야 하기 때문
    return apple

my_fruit = fruit("red", 1000, made_in = "korea")
print(my_fruit)
    
