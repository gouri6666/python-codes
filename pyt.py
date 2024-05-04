n=int(input())
s=" "
while n>0:
    rem=n%2
    s=s+str(rem)
    n=n//2
print(s[::-1])   