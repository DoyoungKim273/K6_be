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

users = {
    'a' : {
        'first' : 'amy',
        'last' : 'albert'
    },
    'b' : {
        'first' : 'ben',
        'last' : 'bently'
    },
    'c' : {
        'first' : 'cate',
        'last' : 'cindy'
    }
}

for user_key in users.items():
    print(user_key)
