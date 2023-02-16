def hello():
    print("this is my first fuction")
hello()

def calculate():
    x=7
    y=9
    print(x*y)
calculate()

def majina(fname,lname):
    print(fname+ " "+lname)
majina("Sylvia", "Wambui")

def names(sname,fname,lname):
    print(sname+ " "+fname+" "+lname)
names("joan", "wanjiru","wanjira")

def greetings(name,greetings="hello"):
    print(greetings +" "+name)
greetings("sylvia")
greetings("niaje","boboh")
def schools(primary,school="ngaru"):
    print(school+ " "+primary)
schools("sagana")
#max and min fuction
def maxvalue(a,b,c,d,e,f):
    return max(a,b,c,d,e,f)
results=maxvalue(4,7,8,6,3,58)
print(results)
def minvalue(q,e,r,t,y):
    return min(q,e,r,t,y)
results=minvalue(6,45,12,5,7)
print(results)
#sort fuction
def sort_list(lst):
    return sorted(lst)
answer=sort_list([72,15,4,8,13])
print(answer)

def print_numbers(n):
    for i in range(n):
print(i)
print_numbers(5)