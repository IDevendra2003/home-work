file = open("input.txt","rt") 
even = open("even.txt","w") 
odd = open("odd.txt","w")
for i in file: 
    if i.strip(): 
        num = i
        if (num % 2 == 0): 
            even = open("even.txt","a") 
            even.write(str(num))
            even.write("\n") 
        else: 
            odd = open("odd.txt","a") 
            odd.write(str(num))
            odd.write("\n")
odd.close() 
even.close()