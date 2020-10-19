def computepay(h,r):
    if h > 40 :
        reg = h * r
        ot = (h - 40.0) * (r * 0.5)
        total = reg + ot
    else:
        total = h * r
    return total

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h,r)
print("Pay",p)