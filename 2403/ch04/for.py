pizzas = ['cheese', 'ham', 'pineapple', 'meat']

for pizza in pizzas :
    print(f"I love {pizza} pizza.")
print(f"Let's eat.")

squares = []
for value in range(1, 21):
    square = value * 2
    squares.append(square)
print(squares)

simple_way = [num * 2 for num in range(1, 11)]
print(simple_way)

numbers = list(range(1, 4))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

triples = []
for count in range(1, 11):
    triple = count **3
    triples.append(triple)
print(triples)