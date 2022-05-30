with open('D:/Users/pgupt016/Desktop/PY/item.txt' , 'r') as ins:
 array = [[n for n in line.split()] for line in ins]
print(array)
dic = {}
for i in array: #Converting List to dictionary
    #print(i)
    dic[i[0]] = int(i[1])
    
    
print(dic)

#dic = { 'apple' : 2, 'orange' : 3 }

orderlist = [] # List to Store users order, AKA cart
cartvalue = 0  #Variable to Hold total cost at bill generation

while True:  #To continuesly prompt user for order
  print ('******* Enter a number to add an fruit to your Cart ********')
  print ('1. Apples \n2. Orange\n3. Generate Bill')
  userinput = int(input())

  if userinput == 3:
        break
  elif userinput == 1:
    print('Please enter quatity for apples')
    qa = int(input())    #converted user entered value to int from str
    orderlist.append(['apple',qa]) #add ordered fruit along with quantity to orderlist
    
  elif userinput == 2:
    print('Please enter quantity for oranges')
    qo = int(input())     #converted user entered value to int from str
    orderlist.append(['orange',qo])   #add ordered fruit along with quantity to orderlist
  print ('\n***************************')  
  print ('Your Cart Contains Following items :- ')
  for item in orderlist: #Reading whole orderlist as it stores users cart
        print (item[0]+" == "+str(item[1])) #Printing items with quantity in cart
  print ('***************************\n') 

print('*************************************') 
for item in orderlist: #Reading cart again to generate final invoice
    value = int(item[1])*dic[item[0]]
    print (item[0]+'     == '+str(int(item[1])*dic[item[0]]))
    cartvalue = cartvalue+value
    
print ('\nTotal Amount to be paid == '+str(cartvalue)+' $$')

with open(r'D:\Users\pgupt016\desktop\PY\invoice.txt' , 'w') as fp:
  fp.write("****** Thank you for Shopping with us *******\n")
  fp.write('ItemName'+" Quantity(KG)   Amount")
  for item in orderlist:
     fp.write('\n'+item[0]+"     "+str(item[1]))
     fp.write('\n--------------------------------')
  fp.write('\nTotal Amount to be paid == '+str(cartvalue)+"$ ")
