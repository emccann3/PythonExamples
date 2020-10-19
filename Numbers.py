largest = None
smallest = None
while True :
    number = input("Enter a number: ")
    if number == "done" :break
    try: 
        n = int(number)
    except:
        print("Invalid input, number must be an integer")
        continue
  
    if smallest is None:
        smallest = n
    elif n < smallest :
        smallest = n
    if largest is None:
        largest = n
    elif n > largest :
        largest = n
        
print("Maximum", largest)
print("Minimum", smallest)




