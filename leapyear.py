year = int(input("Provide a year to check if its a Leap Year=> "))
# check_w_4 = year % 2
# check_w_100 = year % 100
# check_w_400 = year % 400

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is 300% Leap Year")
        else:
            print(f"{year} is not a Leap Year")
    else:
       print(f"{year} is 100% Leap Year") 
else:
    print(f"{year} is not a Leap Year")
