comm_rate= 0.0
sales_amt= 0.0  
sales_per_num= "" 
class_= 0 
close_message= ""
error_= ""

print("JAM EX LIMITED COMMISSION CALCULATOR v1.0.0 \n")
while not close_message.upper().__eq__ ("N"):
   sales_per_num= input("Enter Salesperson Number Please: \n")
   while not sales_per_num.isdigit():
       print("INCORRECT INPUT PLEASE ENTER A NUMBER(S)\n")
       sales_per_num= input ("Enter Salesperson Number Please: \n")
   class_= input("Enter Class Number Please: \n")
   while not class_.isdigit():
       print("INCORRECT INPUT PLEASE ENTER A CLASS NUMBER \n")
       class_= input ("Enter Class Number Please: \n")      
   while True:
       sales_amt = input("Enter Sales Amount Please: \n")       
       if sales_amt.isdigit():
           break
       else:
           partition = sales_amt.partition('.')
           if (partition[0].isdigit() and partition[1] == '.' and partition[2].isdigit()) or (partition[0] == '' and partition[1] == '.' and partition[2].isdigit()) or (partition[0].isdigit() and partition[1] == '.' and partition[2] == ''):
               break
           else:
               print("INCORRECT INPUT PLEASE ENTER A NUMBER(S) \n")
         
   if  int(class_)== 1: 
        if float(sales_amt) <=1000:
            comm_rate= .06*float(sales_amt)
        elif float(sales_amt)>1000 and float(sales_amt)<2000:
            comm_rate= .07*float(sales_amt)
        elif float(sales_amt)>=2000:
            comm_rate= .10*float(sales_amt)
        print("COMMISION IS: ",comm_rate)    
   elif int(class_) == 2:
        if float(sales_amt)<1000:
            comm_rate= .04*float(sales_amt)
        elif float(sales_amt) >=1000:
             comm_rate= .06*float(sales_amt)
        print("COMMISION IS: ",comm_rate)     
   elif int(class_) == 3:
        comm_rate= .45*float(sales_amt)
        print("COMMISION IS: ",comm_rate)
   else: print ("ERROR NOT A VALID CLASS. \n")
   
   
   close_message= input("PRESS n or N TO CANCEL: \n")
   while not close_message:
       print("PLEASE ENTER SOMETHING. \n")
       close_message= input("PRESS n or N TO CANCEL: \n")
print ("HAVE A NICE DAY (: \n")

            
            
                
