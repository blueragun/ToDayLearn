# 그는 피자 가게에서 주문할 수 있는 피자 중 1 달러 당 열량이 최대가 되는 피자를 주문하고 싶어한다.
#Miss 피자는 N 종류의 토핑에서 여러 종류를 자유롭게 선택하여, 도우 위에 올려 주문할 수있다.
#같은 토핑을 2 개 이상 올릴 수 없다.
#도우에 토핑을 하나도 하지 않은  피자도 주문할 수있다.
#도우의 가격은 A 달러이며, 토핑의 가격은 모두 B 달러이다.
#실제 피자 가격은 도우의 가격과 토핑 가격의 합계이다.
#즉, 토핑을 k 종류 (0 ≦ k ≦ N) 한 피자의 가격은 A + k × B 원이다.
#피자 전체의 칼로리는 도우 열량과 토핑 칼로리의 합계이다.
#도우의 가격과 토핑의 가격, 그리고 도우와 각 토핑 열량 값이 주어 졌을 때, "최고의 피자"의 1 달러 당 열량의 수를 구하는 프로그램을 작성하시오.

to_kind = 3
dow_price = 12
toping_price = 2
dow_cal = 200
to1_cal = 50
to2_cal = 300
to3_cal = 100

toping_cal = [to1_cal, to2_cal, to3_cal]
toping_cal.sort()

firsttocal = toping_cal[to_kind - 1]
secondtocal = toping_cal[to_kind - 2]

totoal_price = 0

result = 0
cal = 0


for i in toping_cal :
  cal += i
  totoal_price += toping_price
  
  totalresult = (dow_cal + cal) / (dow_price + totoal_price)
  if result > totalresult :
    break
  else :
    result = totalresult

print(int(result))  
