friends = ['amy', 'ben', 'cate', 'dean', 'eric']

print(friends[0:3])
print(friends[:4])
print(friends[1:-1])
print(friends[:])

for friend in friends[:3]:
    print(f"Welcome to my home, {friend.upper()}.")

new = friends[:]
new.append('francis')
print(new)

numbers = (1, 2, 3, 4, 5)
print(f"number {numbers[0]}")

for number in numbers:
    print(number)

numbers = (10, 20, 30, 40, 50)

for number in numbers:
    print(number)