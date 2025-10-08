#functions
def add(x,y,z):
    sum=x+y+z
    print(sum)
add(3,9,6)

def name(n):
    print("Hello!"n)
name("madhuhasn")
name("sathya sudar")

def name():
    print("Hello world")
name()

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
    
