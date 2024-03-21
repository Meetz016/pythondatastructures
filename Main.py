# import calendar
# dd=int(input())
# mm=int(input())
# yy=int(input())
# if 0< mm <=12:
#     l=calendar.monthcalendar(yy,mm)
#     if 0 < dd <= max(max(l)):
#         print("Valid Date")
#     else:
#         print("Invalid Date")
# else:
#     print("Invalid Date")

n=int(input())
spaces=n-2
for i in range (0,n):
    if i==0 or i==n-1:
        for _ in range(0,n):
            print("*",end=" ")
    else:
        #spaces
        for j in range(0,spaces):
            print(" ",end=" ")
        spaces-=1
        print("*",end="")
    print()