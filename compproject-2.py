import random
from datetime import date, timedelta,datetime


def eligiblefordiscount(price):
    discount=0
    if price <=1000:
        discount=0
    elif price >1000 and price <=5000:
        discount = 0.05*price
    elif price>5000 and price<=10000:
        discount = 0.1*price
    elif price>10000:
        discount = 0.15*price
    return discount
def deliverytime(n):
    days =0
    if n<3:
        days=2
    elif n>=3 and n <8:
        days=4
    elif n>=8:
        days =7
    return(days)
ans='n'
while ans=='n' or ans=='N':
 print()   
 print(" Welcome to NIKE-CLOTHES,SHOES,AND ACCESSORIES")
 print("1. New order")
 print("2. Cancel an existing order")
 print("3. Track order")
 choice = int(input("Enter choice(1 ,2,3):"))
 while choice!=1 and choice !=2 and choice!=3:
    print("Invalid choice")
    choice=int(input("Enter correct choice(1 ,2,3):"))



 if choice==1:
  myfile3 =open("orderhistory.txt","a+")
  myfile1 = open("nike.txt","r")
  myfile3.seek(0)
  str1 = myfile3.read()
  billno= random.randint(10000,999999)
  while str(billno) in str1:
      billno= random.randint(10000,999999)
  str2 =myfile1.read()
  print(str2)
  myfile2= open("bill.txt","w+")
  myfile2.write("%30s"%"NIKE-CLOTHES,SHOES,AND ACCESSORIES\n")
  myfile2.write("BILL NO.:" + str(billno)+"\n")




              


  myfile2.write("PRODUCT" +"%20s"%"QTY" + "%20s"%"PRICE\n")          
  fif,nba,nik21,nik22,lf,rg,jo,bb,fb,tg,gf,ts,bp,sk,ha,wb=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  name=input("Enter name:")
  while not(name.isalpha()):
      print("Invalid name given")
      name=input("Enter name:")
  pno=input("Enter phone no:")
  while not(pno.isdigit()) or len(pno) !=10:
     print("Inavlid phone no.")
     pno=input("Enter correct pnone no.")
  address=input("Enter address:")
  while address=='':
      print("Invalid address given")
      name=input("Enter address:")
  date = date.today()
  print("Discount: 5% on purchase above 1000 and below 5000")
  print("Discount: 10% on purchase above 5000 and below 10000")
  print("Discount: 15% on purchase above 10000 ")
  
  print()
  print("Note:The below also accounts for if you want more than 1 quantity for an item.Ex: If you want 2 socks and 1 hat enter 3 as number of items")
  n =int(input("Enter number of items:"))
  print()
  print("Note:Check for product code, enter same product code again if you want one more item of the same kind ")
  print()
  
  tprice=0
  for i in range(0,n):
        pcode =input("Enter product code:")
        pcode=pcode.upper()
        if pcode=='FIFA22':
            tprice+=2500
            fif+=1  
        elif pcode=='NBA21':
            tprice+=3500
            nba+=1
        elif pcode=='NIKE21':
            tprice+=1000
            nik21+=1
        elif pcode=='NIKE22':
            tprice+=600
            nik22+=1
        elif pcode=='LF21':
            tprice+=4500
            lf+=1
        elif pcode=='RG21':
            tprice+=5300
            rg+=1
        elif pcode=='JO21':
            tprice+=8500
            jo+=1
        elif pcode=='BB21':
            tprice+=7500
            bb+=1
        elif pcode=='FB21':
            tprice+=11000
            fb+=1
        elif pcode=='TG21':
            tprice+=6200
            tg+=1
        elif pcode=='GF21':
            tprice+=4000
            gf+=1
        elif pcode=='TS21':
            tprice+=9000
            ts+=1
        elif pcode=='BP21':
            tprice+=2500
            bp+=1
        elif pcode=='SK21':
            tprice+=400
            sk+=1
        elif pcode=='HA21':
            tprice+=700
            ha+=1
        elif pcode=='WB21':
            tprice+=800
            wb+=1
        else:
            print("Invalid product code")
            i-=1
  if fif>0:
        myfile2.write("Football jersey" +"%12s"%str(fif) + "%20s"%str(fif*2500)+"\n")
  if nba>0:
        myfile2.write("Basketball jersey" +"%10s"%str(nba) + "%20s"%str(nba*3500)+"\n")
  if nik21>0:
        myfile2.write("Nike t-shirt" +"%15s"%str(nik21) + "%20s"%str(nik21*1000)+"\n")
  if nik22>0:
        myfile2.write("Nike short and pant" +"%8s"%str(nik22) + "%20s"%str(nik22*600)+"\n")
  if lf>0:
        myfile2.write("Lifestyle shoe" +"%13s"%str(lf) + "%20s"%str(lf*4500) +"\n")
  if rg>0:
        myfile2.write("Running shoe" +"%15s"%str(rg) + "%20s"%str(rg*5300)+"\n")
  if jo>0:
         myfile2.write("Jordan shoe" +"%16s"%str(jo) + "%20s"%str(jo*8500)+"\n")
  if bb>0:
         myfile2.write("Basketball shoe" +"%12s"%str(bb) + "%20s"%str(bb*7500)+"\n")
  if fb>0:
         myfile2.write("Football shoe" +"%14s"%str(fb) + "%20s"%str(fb*11000)+"\n")
  if tg>0:
         myfile2.write("Gym shoe" +"%19s"%str(tg) + "%20s"%str(tg*6200)+"\n")
  if gf>0:
         myfile2.write("Golf shoe" +"%18s"%str(gf) + "%20s"%str(gf*4000)+"\n")
  if ts>0:
         myfile2.write("Tennis shoe" +"%16s"%str(ts) + "%20s"%str(ts*9000)+"\n")
  if bp>0:
         myfile2.write("Backpack" +"%19s"%str(bp) + "%20s"%str(bp*2500)+"\n")
  if sk>0:
         myfile2.write("Socks" +"%22s"%str(sk) + "%20s"%str(sk*400)+"\n")
  if ha>0:
         myfile2.write("Hats" +"%23s"%str(ha) + "%20s"%str(ha*700)+"\n")
  if wb>0:
         myfile2.write("Water bottle" +"%15s"%str(wb) + "%20s"%str(wb*800)+"\n")
  day= deliverytime(n)       
  discount= eligiblefordiscount(tprice)
  fprice = tprice -discount
  print("Price:", tprice)
  print("Discount:", discount)
  print("Price after discount:",fprice)
    
  print("Printing bill....\n")
  for i in range(0,100000000):
        pass
  myfile2.write("Date of Purchase:" + str(date) + "\n")    
  myfile2.write("Name:" + name + "\n")
  myfile2.write("Phone no.:" + pno + "\n")
  myfile2.write("Address:" + address + "\n")
  myfile2.write("Price:" + str(tprice)+"\n")
  myfile2.write("Discount:" + str(discount)+"\n")
  myfile2.write("Price after discount:" + str(fprice)+"\n")
  myfile2.flush()
  myfile2.seek(0)
  print(myfile2.read())
  print("PAYMENT OPTIONS:")
  print("1.Credit Card")
  print("2. Paytm")
  choice1=int(input("Enter choice:"))
  if choice1==1:
      credit=input("Enter 16 digit credit card number:")
      while not(credit.isdigit()) or len(credit) !=16:
            print("Inavlid credit card no.")
            credit=input("Enter correct credit card no.")
      cvv= input("Enter 3 digit cvv for above credit card:")
      while not(cvv.isdigit()) or len(cvv) !=3:
            print("Inavlid cvv")
            cvv=input("Enter correct cvv:")
      print()  
      print("PAYMENT CONFIRMATION SENT TO", pno)
      print()
      print()      
  if choice1==2:
      pno2=input("Enter phone no. registered to paytm:")
      
      while not(pno2.isdigit()) or len(pno2) !=10:
             print("Inavlid phone no.")
             pno2=input("Enter correct pnone no.")
      print("Final Amount:", fprice)
      print()  
      print("PAYMENT CONFIRMATION SENT TO", pno)
      print()
      print()
      
  
  if fprice>=10000 and fprice<20000:
       print("CONGRATULATIONS YOU GET A FREE BACKPACK")
  elif fprice>=20000 and fprice<40000:
       print("CONGRATULATIONS YOU GET A FREE LIFESTYLE/RUNNING SHOE OF YOUR CHOICE")
  elif fprice>=40000:
       print("CONGRATULATIONS YOU GET A FREE FOOTBALL JERSEY AND RUNNING SHOE")
  else:
       print("Not eligible for any prize")
  print("DELIVERY IN " + str(day)+ " days")       
  print("THANK YOU FOR SHOPPING WITH NIKE")
  deldate= date +timedelta(days=day)

  myfile3.write(str(billno) + ' ' + name + ' ' + pno + ' ' + str(date) +' ' + str(deldate) +'\n')
  myfile3.close()
 elif choice==2:
    myfile4=open("orderhistory.txt","r")
    data= myfile4.readlines()
    phno=input("Enter phone number given at time of order:")
    while not(phno.isdigit()) or len(phno) !=10:
     print("Inavlid phone no.")
     pno=input("Enter correct phone no.")
    count, count1=0, 0
    date2=date.today()
    for i in data:
        data1=i.split()
        if phno==data1[2]:
             d =datetime.strptime(data1[4],"%Y-%m-%d")
             d=d.date()
             if date2<=d :
                print("Bill no:", data1[0])
                print("Date of purchase:", data1[3])
                count1+=1
             else :
                 print("Bill no:"+ data1[0]+" Order should already be delivered")
             count+=1    
                 
                
                
                
    myfile4.close()        
    if count==0:
        print("Phone number doesnt exist")
    else:
        if count1>0:
            
           myfile5=open("orderhistory.txt","w+")
           bill=input("Enter bill number for order to be cancelled")
           index=0
           flag=False
           date2=date.today()
           for j in range(0,len(data)):
              data1=data[j].split()
              d =datetime.strptime(data1[4],"%Y-%m-%d")
              d=d.date()
              if bill==data1[0] and date2<=d:
                  index=j
                  flag=True
           if flag:       
              del data[index]
              myfile5.writelines(data)
              myfile5.close()
              print("Order cancelled successfully")
           else:
               myfile5.writelines(data)
               myfile5.close()
               print("Cannot cancel order, order already delivered")               
        else:
            print("Orders already delivered cant be cancelled")
    
 elif choice==3:
     myfile6=open("orderhistory.txt","r")
     data2=myfile6.readlines()
     phno2=input("Enter phone no. given at time of order")
     count=0
     date3=date.today()
     for i in data2:
         data3=i.split()
         if phno2==data3[2]:
           count+=1
           d =datetime.strptime(data3[4],"%Y-%m-%d")
           d=d.date()
           if date3<d:
              print("Bill no.:",data3[0])
              print("Delivery in:", (d-date3).days , "days")
           elif date3==data3[4]:
               print("DELIVERY TODAY")
           else:
               print("Bill no:"+ data3[0]+" ORDER SHOULD ALREADY BE DELIVERED")
     if count==0:
         print("Phone number doesnt exist")
               
         
 ans=input("Do you want to terminate session(y/n):")        
       

