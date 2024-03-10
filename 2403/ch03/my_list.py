friends = ['amy', 'ben', 'cate', 'dean']
print(friends[0].upper())
print(f"Hello, {friends[1].title()}.")

fruits = ['apple', 'banana', 'lemon', 'kiwi']
# fruits[0] = 'pear'
# fruits.append('watermelon')
# fruits.insert(1, 'fig')
# del fruits[3]
# favorite = fruits.pop(3)
# fruits.remove('lemon')
# sour = 'lemon'
# fruits.remove(sour)

# print(fruits)
# print(sour)
unwanted = fruits.pop()
print(f"{fruits[2].title()} is too sour.")
print(f"{unwanted.title()} is green.")
print(f"Minion loves {fruits[1].upper()}.")
# print(favorite)

colors = ['red', 'yellow', 'green', 'blue'] 
# del colors [0]
# colors.append('purple')
# abc = colors.sorted()
# print(colors)
# print(abc)
# print(sorted(colors))
colors.reverse()
print(colors)
# print(len(colors))
print(f"I have {len(colors)} colors.")

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
print(cars[-1])