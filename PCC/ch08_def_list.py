def customer_list(names) :
    for name in names:
        msg = f"Hello, {name.upper()}!"
        print(f"Hello, {name.title()}!") # 따로 msg 변수 지정해주지 않고 이렇게 출력해도 무방함
        print(msg)

customer_names = ['amy', 'ben', 'cate'] # 함수에 들어가야 할 리스트 명명, 값 배당
customer_list(customer_names) # 함수에 리스트 명 넣어주기

vvip_customer_names = [] # 빈 리스트 하나 준비
 
while customer_names:
    vip_customer_names = customer_names.pop()
    print(f"vip : {vip_customer_names}") # 별도의 리스트를 변수로 지정해 남는 게 없을 때까지 리스트의 내용을 pop 하고(동시에 출력)
    vvip_customer_names.append(vip_customer_names) # 별도로 만든 리스트를 옮길 목적으로 만든 리스트에 append 해준다 

print("<vvip>")
for vvip in vvip_customer_names : # 옮길 목적으로 만든 리스트의 내용을 for 문을 돌며 출력해준다
    print(vvip)

print(" ")

# 독립된 작업을 수행하는 함수 2개를 만들어 코드를 정리 - 중요한 작업을 수행하는 코드를 함수로 분리, 프로그램의 주된 흐름 쉽게 이해 가능
def order_list(first_stages, last_stages):
    while first_stages :
        second_stages = first_stages.pop()
        print(f"second : {second_stages}")
        last_stages.append(second_stages)
        print(first_stages)

def show_last_stages(last_stages):
    print("<last>")
    for last in last_stages:
        print(last)
    
first_stages =['apple', 'banana', 'kiwi']
last_stages =[]

order_list(first_stages, last_stages)
show_last_stages(last_stages)

