n=int(input('enter the number whose sum u want to find:'))

sum=0

for i in range(1,n):
    sum=i+sum
    print("sum=",sum)
