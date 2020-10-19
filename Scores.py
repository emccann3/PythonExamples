score = input("Enter Score: ")
try:
    sc = float(score)
except:
    print("Error, please enter a numeric value")

if sc > 1.0: 
    print("Error, value entered is out of range")
elif sc >= 0.9:
    print("A")
elif sc >=0.8:
    print("B")
elif sc >= 0.7:
    print("C")
elif sc >= 0.6:
    print("D")
elif sc < 0.6:
    print("F")