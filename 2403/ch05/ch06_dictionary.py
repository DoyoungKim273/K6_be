# person = {'first_name' : 'Doyoung', 'last_name' : 'Kim', 'gender' : 'Woman' , 'nickname' : 'Kim'}
# message = "\n Good to see you."

# person['hobby'] = 'Reading books'
# person['nickname'] = 'bailey'
# print(person)

# print(f" Hello, {person['first_name']}.{message}")

# for ques, infor in person.items():
#     print(f" {ques} & {infor}")

# print("")

# for ques in sorted(person.keys()):
#     print(ques)

# print("")

# for infor in sorted(person.values()):
#     print(infor)

# print("")

# for infor in set(person.values()):
#     print(infor)

# print(set(person))


# alien_0 = {'color' : 'green', 'point' : '5'}
# alien_1 = {'color' : 'yellow', 'point' : '10'}
# alien_2 = {'color' : 'red', 'point' : '15'}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens :
#     print(alien)

# aliens = []

# for alien_number in range(30):
new_alien = {'colors' : ['green', 'yellow', 'red'], 'points' : ['5', '3', '1']}
    # aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'balck':
#         alien['color'] = 'yellow'
#     elif alien['color'] == 'green':
#         alien['color'] = 'red'

# for alien in aliens [:5]:
#     print(alien)

# print(f"total : {len(aliens)}")
for color in new_alien['colors']:
    print(color)

    for point in new_alien['points']:
        print(point)

# 딕셔너리 안에 딕셔너리를 중첩 -- 키와 값의 쌍으로 두고 값에 다시 딕셔너리를 중첩함
# 중첩된 안쪽의 딕셔너리를 부를때는 for 문으로 우선 밖과 안의 딕셔너리를 명명해주어야함 -- 키값쌍을 반환하는 .item() 메서드를 이용
# for문 안에서 다시 user_info에서 각 값을 선언 -- 출력할 수 있게 됨
        
users = {
    'a' : {
        'first' : 'amy',
        'last' : 'albert',
        'location' : 'busan'
    },
    'b' : {
        'first' : 'ben',
        'last' : 'bently',
        'location' : 'busan'
    },
    'c' : {
        'first' : 'cate',
        'last' : 'cindy',
        'location' : 'busan'
    }  
}

for user_key, user_info in users.items():
    print(user_key)
    full_name = f"{user_info['first']} {user_info['last']}"
    city = user_info['location']
    print(full_name.upper())
    print(city)
