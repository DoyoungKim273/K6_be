colors = ['red', 'yellow', 'green']

if 'black' in colors:
    print(f"Because of {colors[0].upper()} you got 5 points.")
elif 'yellow' in colors:
    print(f"Because of {colors[1].upper()} you got 3 points.")
else:
    print(f"Because of {colors[2].upper()} you got 1 points.")

age = 12

if age > 12:
    price = 100
elif age < 12:
    price = 50
else:
    price = 80
print(price)

pens = []

if pens:
    for pen in pens:
        print("OK")
else:
    print("Get one") 
# 리스트가 빈 경우의 출력값은 별개로 빼서 입력해야함
