month_num = int(input())
if month_num <= 0:
    print("Error")
elif month_num <= 2 or month_num == 12 :
    print("Winter")
elif month_num <= 5:
    print("Spring")
elif month_num <= 8:
    print("Summer")
elif month_num <= 11:
    print("Autumn")