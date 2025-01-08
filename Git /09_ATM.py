#출금 요청한 금액을 받는 변수 : withdraw_amount
#출금을 요청한 금액을 balance 변수에서 뺀 결과가 들어가도록 작성해주세요.
#영수증에 다음 순서로 값이  들어가도록 코드를 만들어주세요 -> ("출금", withdraw_amount, balance) 순으로 데이터 넣어주세요.
# 기본 금액: balace
# 기본금액에 돈을 넣어주세요
#while문을 이용해서 입금, 출금 ,영수증보기, 종료라는 기능이 졸료라는 버튼을 누르기전 전까지 계속해서 노출 되도록 만들어주세요.
#종료를 누르면 서비스를 종료한다는 메서지를 출력하고 현재 잔액을 보여주세요.

balance = 3000 #현재 잔액
receiots = []

while True:
    num = input("사용하실기능을 선택해주세요 (1:입금, 2:출금, 3:영수증보기:, 4:종료)")
    if num == "4":
        break
    if num == "1":
        deposit_amout = int(input("입금할 금액은 입력해주세요 :"))
        balance += deposit_amout
        receiots.append(("입금",deposit_amout,balance))
        print(f'압금허신금액은 {deposit_amout}원이고,현재잔액은 {balance}원 입니다.')
    if num == "2":
        withdraw_amount = int(input("출금할 금액을 입력하세요: "))
        withdraw_amount = min(balance, withdraw_amount)
        balance -= withdraw_amount
        receiots.append(("출금",withdraw_amount,balance))
        print(f'출금하신금액은 {withdraw_amount}원이고,현재잔액은 {balance}원 입니다.')
 
 
print(f'서비스를 종료합니다.현제잔액은{balance}원 입니다.')
    

