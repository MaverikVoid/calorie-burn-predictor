a = int(input("Enter the number: "))
sum = 0
while a>0:
    d = a%10
    a = a//10
    sum = sum*10 + d
    
print(sum)