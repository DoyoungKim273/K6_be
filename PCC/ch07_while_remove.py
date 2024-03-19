pets = ['dog', 'cat', 'dog', 'cat', 'cat']

print(pets)

# while 루프를 이용해 리스트의 cat을 모두 제거한다
while 'cat' in pets:
    pets.remove('cat') 
# 리스트명 + '.' + 메서드명
    
print(pets)
