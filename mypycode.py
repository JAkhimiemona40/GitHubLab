import sys

shift_amount = int(sys.argv[1]) #step1

message = input() #step2

message = message.upper() #step3

counter_letters = 0

counter_column = 0

#print(shift_amount, message)

for ch in message :
  if ch.isalpha(): #step4
    if ord(ch) + shift_amount > ord('Z'):
      answer = ord('A') + (ord(ch) + shift_amount) - ord('Z') - 1
    else:
      answer = ord(ch) + shift_amount
    counter_letters += 1
    if counter_letters == 5:
       print(chr(answer), end = " ") 
       counter_letters = 0
       counter_column += 1
       if counter_column == 10:
         print("")
         counter_column = 0
    else:
      print(chr(answer), end = "") 
        
       
    
    
    
  
    
     
   
   

  


  
 
