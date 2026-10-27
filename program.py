 1.a=4
    if(a>0):
       print("negative")
    else:
       print("zero")
o/p
positive
2.
a=int(input("enter first no:"))
b=int(input("enter second no:"))
if(a>b):
  print("largest no:",a)
else:
 print("largest no:",b)
o/p:
enter first no:4
enter second no:8
largest no: 8

3.
a=10
if(a%2==0):
  print("even")
else:
  print("odd")
o/p
even

4.
a=int(input("enter your age:"))
if(a>=18):
  print("your voting eligible")
else:
  print("not eligible")
o/p
enter your age:20
your voting eligible

5.
a=int(input("enter your mark:"))
if(a>=65):
  print("pass")
else:
  print("fail")
o/p
enter your mark:40
fail

6.
a=int(input("enter your first no:"))
b=int(input("enter your second no:"))
c=int(input("enter your third no:"))
if(a>b):
  print("a is greater:",a)
elif(b>c):
  print("b is greater:",b)
else:
  print("c is greater:",c)
o/p
enter your first no:9
enter your second no:17
enter your third no:89
c is greater: 89

7.
a=int(input("enter a year:"))
if(a%4==0):
  print("leap year")
else:
  print("not a leap year")
o/p
enter a year:1995
not a leap year

8.
n=int(input("enter a number:"))
if(n%5==0):
  print("divisible by 5")
else:
  print("not divisible by 5")
o/p
enter a number:35
divisible by 5

9.
n=int(input("enter a number:"))
if(n%5==0) and (n%3==0):
  print("divisible by 5 or 3")
elif(n%3==0):
  print("not divisible by 3")
elif(n%5==0):
  print("not divisible by 5")
else:
  print("not divisible by 5 or 3")
o/p
enter a number:78
not divisible by 3

10.
a=int(input("enter your first no:"))
b=int(input("enter your second no:"))
c=int(input("enter your third no:"))
if(a<b):
  print("a is smaller:",a)
elif(b<c):
  print("b is smaller:",b)
else:
 print("c is smaller :",c)
o/p
enter your first no:6
enter your second no:8
enter your third no:9
a is smaller: 6
11.
n=int(input("enter a no:"))
if n>=0 &n<=99:
  print("two digit no")
else:
  print("not a two digit no")
 o/p
enter a no:70
two digit no
12.
n=int(input("enter a no:"))
if n%5==5:
  print("last digit is 5")
else:
  print("not last digit is 5")
 o/p
enter a no:50
not last digit is 5
13.
a=input("enter a character:")
if a.isupper():
   print("upper case")
else:
   print ("lower case")
 o/p
enter a character:c
lower case
14.
a=input("enter a value:")
if a.isalpha():
  print("alphabet")
elif a.isdigit():
  print("digit")
else:
  print("special character")
 o/p
enter a value:6
digit
15.
a=int(input("enter a temperature:"))
if(a>37):
  print("above")
elif(a<37):
  print("below")
else:
  print("equal")
 o/p
enter a temperature:37
equal
16.
bill=int(input("enter your bill:"))
if bill>2000:
  discount=bill*10/100
  bill=bill-discount
print("final bill=",bill)
o/p
enter your bill:2050
final bill= 1845.0
17.
mark=int(input("enter a mark:"))
attendance=float(input("enter a attendance:"))
if(mark>=90) and (attendance>=85):
   print("eligible")
else:
   print("not eligible")
 o/p
enter a mark:85
enter a attendance:60
not eligible
18.
count=0
for i in range(1,51):
    if(i %5==0):
      count+=1
print(count)
o/p
10
19.
sum=0
for i in range(1,21):
  if(i%2==0):
    sum+=i
print(sum)
o/p
110
20.
for i in range(1,31):
  if(i%3==0) or (i%2==0):
      print(i)
  o/p
 20.
 for i in range(1,31):
  if(i%3==0) and (i%4!=0):
      print(i)
   o/p
3
6
9
15
18
21
27
30
21.
n = int(input("How many numbers? "))
for i in range(n):
    n = int(input("Enter a number: "))

    if n > 0:
        print("positive")
    elif n < 0:
        print("negative")
    else:
        print("zero")
     o/p
How many numbers? 2
Enter a number: 4
positive
Enter a number: 6
positive
21.peter son number
n = int(input("Enter a number: "))
temp = n
total = 0

while temp > 0:
    digit = temp % 10
    fact = 1

    for i in range(1, digit + 1):
        fact *= i

    total += fact
    temp //= 10

if total == n:
    print("Peterson number")
else:
    print("Not a Peterson number")
o/p
Enter a number: 6
Not a Peterson number

22. print tables from getting the values from user
num=int(input("enter a number:"))
for i in range(1,11):
  print(num ,"x", i ,"=",num*i) 
o/p
enter a number:6
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60
23.
for i in range(5, 8):
    if i == 5 or i == 7:
        print(i)
     o/p
5
7
24.
word = input("Enter a word:")
for i in word:
  print (i)
o/p
Enter a word:python
p
y
t
h
o
n
25.
a=input("enter a string:")
count=0
for ch in a:
  count+=1
print("length of string:",count)
o/p
enter a string:python
length of string: 6
26.
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
o/p
Enter a string: mam
Palindrome
27.
a="varshini"
b=19
print(f"my name is {a}")
print(f"my age is {b}")
o/p
my name is varshini
my age is 19
28.
   a=str(input("enter a word:"))
if a[0]==a[-1]:
  print("same")
else:
  print("not same")
o/p
enter a word:google
not same
29.
n=input("enter a string:")
for i in n:
  if n.count(i)==1:
     print(i)
     break
   o/p
enter a string:malayalam
y
30.
n= input("enter a string:")
count=0
for i in n:
  if n.count(i)>1:
    print(i)
o/p
enter a string:varshini
i
i
31.
a=input("enter a string;")
print(a[-2:])
o/p
enter a string;python
on
32.
a="h e l l o  w o r l d"
print(a.replace("h e l l o  w o r l d","hello world"))
O/P
hello world


















 




