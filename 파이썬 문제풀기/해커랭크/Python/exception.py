# 문제
# 정수 n이 입력되고 n의 범위 만큼 a(1 ~ n까지의 정수), b(정수 또는 문자)가
# 입력될 때 a / b의 몫을 구하고 오류가 전시될 경우 정해진 문구를 내보낼 수 있는
# 프로그램을 작성 

n = int(input())

for i in range(n) : # n 범위만큼 반복
    try :
        a, b = input().split()
        print(int(a) // int(b)) # 몫 구하기
    except ZeroDivisionError as e : # 몫이 안구해지면 에러코드 전시
        print("Error Code:", e)
    except ValueError as v : # 몫이 안구해지면 에러코드 전시
        print("Error Code:", v)