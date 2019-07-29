from google.appengine.ext import ndb

class Car(ndb.Model):
    carMake = ndb.StringProperty(required=True)
    carModel = ndb.StringProperty(required=True)

    def printCarInfo(self):
        print(self.carMake + " " + self.carModel)

car1 = Car(carMake = "ford", carModel = "mustang")
car2 = Car(carMake = "toyota", carModel = "prius")

car1.printCarInfo()
car2.printCarInfo()
