# 문제 1번
from this import d


def sum(a,b):
    # your code
    return print(a+b)
sum(8,6)

# 문제 2번
def sub(a,b):
    # your code
    return print(a-b)
sub(8,6)

# 문제 3번
def mul(a,b):
    # your code
    return print(a*b)
mul(8,6)

# 문제 4번
def div(a,b):
    # your code
    return print(a/b)
div(4,2)

# 문제 5번
def distance(x1,y1,x2,y2):
    # your code
    return print(((x1-x2)**2+(y1-y2)**2)**0.5)
distance(1,1,4,5)
# 문제 6번
def short():
    lylic = "life is short art is long"
    # your code
    return print(lylic[8:13])
short()
# 문제 7번
def myReverse(string):
    # your code
    return print(string[::-1])
myReverse('reviver')

# 문제 8번
def letMeIntroduceMyself():
    # your code
    name = input("이름을 입력해주세요: ") 
    hobby = input("취미를 입력하세요: ")
    school = input("재학 중인 대학을 입력하세요: ")
    birth = input("생일을 입력하세요(예시: 020925): ")
    month = birth[2:4]
    date = birth[4:]
    return print("제 이름은 {}입니다. 제 취미는 {}이구요. 저는 {}를 다니고 있습니다. 제 생일은 {}월 {}일 입니다.".format(name,hobby,school,month,date)) 
                          
letMeIntroduceMyself()
# 문제 9번
def calcAI():
    # your code
    first = int(input("첫 번째 숫자를 입력하세요: "))
    second = int(input("두 번째 숫자를 입력하세요: ")) 
    return print(first+second)
calcAI()  