x=int(input())
a = x//100
b = (x//10)-(a*10)
c = x%10
print(2*(c*100 + b*10 + a))
