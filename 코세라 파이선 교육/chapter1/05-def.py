def computepay(hr, ra):
    if hr <= 40 :
        pay = hr * ra
    else :
        pay = (40 * ra) + ((hr - 40) * (ra * 1.5))
        
    return pay

hrs = input("Enter Hours:")
rate = input("Enter rate:")
hr = float(hrs)
ra = float(rate)
p = computepay(hr, ra)
print("Pay", p)