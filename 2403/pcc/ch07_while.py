# for 루프는 컬렉션의 요소를 가져와 각 요소마다 코드 블록을 실행
# while 루프는 특정 조건을 통과하는 한 계속 실행됨

# current_number = 1

# while current_number <= 5 :
#     print(current_number)
#     current_number += 1
#     current_number = int(current_number)
#     print(sum(current_number))
# # TypeError: 'int' object is not iterable --- int로 타입캐스팅 해주었는데도 오류가 나는 이유?

current_number = 1
total_sum = 0

while current_number <= 5:
     print(current_number)
     total_sum += current_number
     current_number += 1
print("총 합 : ", total_sum)

# sum() 함수는 요소들의 합을 계산하기 위해 반복 가능한 객체(리스트, 튜플 등)를 기대
# 정수인 current_number를 합하려고 시도 -> 오류 발생
# 만약 1부터 current_number까지의 숫자를 합하려면, 별도의 변수에 합계를 계속해서 더해주어야 함
# total_sum 변수를 추가하여 1부터 current_number까지의 숫자의 합을 누적하고, 루프가 완료된 후에 합계를 출력

python
squares = []
for number in range(1, 6):
    squares.append(number)
print(sum(squares))

odd_number = 0 # 홀수를 넣을 값 초기화
while odd_number < 10: # 10 미만의 홀수 대상으로 함
    odd_number += 1 # 일단 숫자는 1씩 증가토록 함 (왜 증감 연산자를 안 쓰는가? - 파이썬은 그게 없으니까!)
    if odd_number % 2 == 0: # 2로 나누어 값이 0인 조건이 참이면 print 까지 안 가고 루프를 continue
        continue

    print(odd_number)
