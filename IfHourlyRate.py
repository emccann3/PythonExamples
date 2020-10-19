hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except: 
    print("Error, please enter numeric input")
    quit()

print(h, r)
if h > 40 :
    reg = h * r
    ot = (h - 40.0) * (r * 0.5)
    total = reg + ot
else:
    total = h * r
print(total)   