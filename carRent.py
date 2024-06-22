
import datetime
from datetime import datetime
from datetime import date
import random
import string

cInv = 0
rCar = 0
orderList=[]

class Car:
 def __init__(self,carId, model, vehNum, availStat, dailyRate):
  self.carId = carId
  self.model = model
  self.vehNum = vehNum
  self.availStat=availStat
  self.dailyRate=dailyRate
 
 def display(self):
  print("carId   : " ,self.carId)
  print("model   : " ,self.model)
  print("vehNum : " ,self.vehNum)
  print("availStat: " ,self.availStat)
  print("dailyRate: ",self.dailyRate)

class Customer():
  def __init__(self,cusId, cusName, cusAdd):
    self.cusId = cusId
    self.cusName = cusName
    self.cusAdd = cusAdd
  def cusDisplay(self):
    print("cusId   : " ,self.cusId)
    print("cusName   : " ,self.cusName)
    print("cusAdd : " ,self.cusAdd)

class RentalCar(Car,Customer):
  def __init__(self):
    self.carList = []
    self.orderList = []
    
  def carInv(self, carId, model, vehNum, availStat, dailyRate):
    global cInv
    #self.carList.append(Car(carId, model, vehNum, availStat, dailyRate))
    if len(self.carList)==0:
      self.carList.append(Car(carId, model, vehNum, availStat, dailyRate))
      cInv+=1
    else:
      for obj in self.carList:
        #print(obj.carId, obj.model, obj.vehNum, obj.availStat, obj.dailyRate) 
        if obj.carId != carId:
           self.carList.append(Car(carId, model, vehNum, availStat, dailyRate))
           cInv+=1
           break
        else:
            break
       
  def getInvCt(self):
    #global cInv
    #print("Inv Count")
    #for obj in self.carList:
        #cInv+=1
    return cInv
            
  def remInv():
    print("remInv ")
      
  def Invdisplay(self):  
    print("Inside InvDisplay ... ")
    for obj in self.carList:
        if obj.availStat == "Yes":
          print(obj.carId, obj.model, obj.vehNum, obj.availStat, obj.dailyRate)

  def ran_gen(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
    
  def rentCar(self,carId,cust_name,address,mode,num_of_cars):
   if int(num_of_cars) < cInv:
      orderId=''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(10)])
      print(orderId)
      now = datetime.now()
      # dd/mm/YY H:M:S
      dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
      print("date and time =", dt_string)   
    
      y=now.strftime("%Y")
      print("y ", y)
      m=now.strftime("%m")
      print("m ", m)
      d=now.strftime("%d")
      print("d " , d)
      H = now.strftime("%H")
      print("H ", H)
      M = now.strftime("%M")
      print("M ", M)
      S = now.strftime("%S")
      print("S ", S)

      epoch = datetime(int(y),int(m),int(d), int(H), int(M), int(S)).strftime('%s')
      print(epoch)

      obj_to_append = {'carId': carId,'cusName': cust_name,'address': address,'Mode': mode,'NoOfDay': num_of_cars,'rentTime': int(epoch)}  
      if len(self.orderList)!=0:
        for item in self.orderList:
          for key, value in item.items():
              print("Key:", key)
              print("Value:", value)
              if value["carId"] != carId:
               self.orderList.append({orderId : obj_to_append})
               print("OrderList : " , self.orderList)
              else:
               print("Sorry Request Denied - Car Unavailable ")
      else:
        self.orderList.append({orderId : obj_to_append})
        print("OrderList : " , self.orderList)

      for item in self.orderList:
          for key, value in item.items():
              print("Key:", key)
              print("Value:", value)
              
      for obj in self.carList:
         print(" OBJECT :", obj.carId, obj.model, obj.vehNum, obj.availStat, obj.dailyRate)
         if obj.carId == carId:
           obj.availStat="No"
    
      for obj in self.carList:
         print(obj.carId, obj.model, obj.vehNum, obj.availStat, obj.dailyRate)
        
      for obj in self.orderList:
         print(obj)
   else:
       print("Sorry Request Denied - Number of cars requested exceeding the inventory total... ")

  def returnCar(self,carId):
       print("Inside return Car")

       now = datetime.now()
       # dd/mm/YY H:M:S
       dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
       print("date and time =", dt_string)      
       y=now.strftime("%Y")
       m=now.strftime("%m")
       d=now.strftime("%d")
       H = now.strftime("%H")
       M = now.strftime("%M")
       S = now.strftime("%S")
       epoch = datetime(int(y),int(m),int(d), int(H), int(M), int(S)).strftime('%s')
       print(epoch)

       for item in self.orderList:
           for key,value in item.items():
             print(f"{key}: {value}")
             if int(value['carId']) == int(carId):
                NumDays = round((int(epoch) - 1712941695)/86400)
                print(" No of days to calculate is : ", NumDays)
                print (35 * '-')
                print(" ----------- Rental Bill ------------ ")
                print("Customer Name : ", value['cusName'])
                print("Address       : ", value['address']) 
                print("Days Rented   : ", NumDays)
                print("Amount        : ", NumDays * 24) 
                print (35 * '-')
       for obj in self.carList:
         if obj.carId == carId:
           obj.availStat="Yes"   
         print(" OBJECT :", obj.carId, obj.model, obj.vehNum, obj.availStat, obj.dailyRate)