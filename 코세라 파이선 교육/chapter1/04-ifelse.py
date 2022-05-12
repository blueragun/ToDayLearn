hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

if h <= 40 :
    pay = h * r
    print(pay)
else :
    pay = (40 * r) + ((h - 40) * (r * 1.5))
    print(pay)



# ----------------------------------------------------


score = input("Enter Score: ")
s = float(score)
if s >= 0.9 :
    print('A')
elif s >= 0.8 :
    print('B')
elif s >= 0.7 :
    print('C')
elif s >= 0.6 :
    print('D')
else :
    print('F')