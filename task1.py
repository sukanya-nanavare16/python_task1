#Sum of two numbers
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Sum of two numbers:",a+b)


#odd or even checker
a=int(input("Enter a number:"))
if(a%2==0):
    print(a," is even number")
else:
    print(a," is odd number")


#factorial calculation
def fact(n):
    if (n==0):
        return (1)
    return (n*fact(n-1))
num=int(input("Enter a number:"))
if (num<0):
    print("Not defined for negative numbers")
else:
    print("Factorial:", fact(num))


#fibonacci sequence
n=int(input("Enter number of terms: "))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

#String reverse
text = input("\nEnter a string: ")
print("Reversed:", text[::-1])


#Palindrome Check
word=input("Enter a word: ")
if (word == word[::-1]):
    print("Palindrome word")
else:
    print("Not Palindrome word")


#Leap year check
year = int(input("Enter a year: "))
if (year%400==0):
    print("Leap Year")
elif (year%100==0):
    print("Not a Leap Year")
elif (year%4==0):
    print("Leap Year")
else:
    print("Not a Leap Year")


#Armstrong number
n=int(input("Enter a number:"))
sum=0
temp=n
while (temp>0):
    rem=temp%10
    sum=sum+(rem*rem*rem)
    temp//=10
if (sum==n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

