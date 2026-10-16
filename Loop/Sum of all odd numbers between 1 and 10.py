sum = 0 

for i in range(1,11):

    print(i , "is processing")

    if i % 2 ==0 :  ## even 
        continue 
          
    sum+= i 
    print(i ,"is added to the sum")
