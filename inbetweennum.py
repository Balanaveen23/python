a=5
b=15
even=0
odd=0
for i in range(a,b+1):
    if i%2==0:
        even=even+i
    else:
            odd=odd+i      
print(even)
print(odd)
diff=even-odd
print(diff)
    
