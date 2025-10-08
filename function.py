def even(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
even(14)

def num(n):
    for i in range(1,n+1):
        print(i)
num(20)

def num(n):
    for i in range(n+1,0,-1):
        print(i)
num(20)

def year(e):
    if e%4==0 or e%100==0 and e%400!=0:
        print("leap year")
    else:
        print("not year")
year(2025)
    
