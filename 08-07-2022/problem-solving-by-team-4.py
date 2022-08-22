##A Truck is a Car but with the additional behaviours.
##Inherit the Car class into Truck class and build the additional features.
##
##Truck Car have following attributes and methods
##Attributes:
##color,max_speed,acceeleration,tyre_friction,is_engine_started,current_speed,nitro
##note: nitro is race_car attributes as child attribute
##
##Methods:
##start_engine,stop_engine,accelerate,apply_breaks,sound_horn
##Sample Input
##Checking Default Tests
##Sample Output
##False
##50
##• You can copy the implementation of Car class from
##the previous set and add new features on top of
##that code.
##Sample Input
##Checking Default Tests
##Sample Output
##False
##50
##25
##0
##Cannot load cargo more than max
##True
##Cannot load cargo during motion
##Cannot unload cargo during moti
##Honk Honk
##Car has not started yet
##
class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.is_engine_started=False
        self.current_speed=0

    def start_engine(self):
        self.is_engine_started=True
        



    def stop_engine(self):
        self.is_engine_started=False


    def accelerate(self):
        if not self.is_engine_started:
            print("Car has not started Yet")
        else:
            self.current_speed +=self.acceleration
            if self.current_speed > self.max_speed:
                self.current_speed=self.max_speed


    def apply_breaks(self):
        self.current_speed -=self.tyre_friction
        if self.current_speed < 0:
            self.current_speed=0


    def sound_horn(self):
        if self.is_engine_started:
            print("BEEP BEEP")
        else:
            print("CAR HAS NOT STARTED YET")



class TruckCar(Car):
    def __init__(self,color,max_speed,acceleration,tyre_friction,nitro):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self.nitro=nitro
        self.load=0
    def load_cargo(self,nitro):
        if self.is_engine_started:
            print("Cannot load cargo during motion")
        elif nitro+self.load>self.nitro:
            print("Cannot load cargo more than max limit: {}".format(self.nitro))
        else:
            self.load+=nitro
    def unload_cargo(self,nitro):
        if self.is_engine_started:
            print("Cannot unload cargo during motion")
        else:
            self.load-=nitro
            if self.load<0:
                self.load=0
    def sound_horn(self):
        if self.is_engine_started:
            print("Honk Honk")
        else:
            print("Car has not yet started")
            

truckcar = TruckCar(color="red",max_speed=250,acceleration =50,tyre_friction=30,nitro=4)
car = Car(color="red",max_speed=250,acceleration =50,tyre_friction=30)
truckcar.start_engine()
truckcar.accelerate()
print(truckcar.current_speed)
print(truckcar.nitro)
truckcar.accelerate()
print(truckcar.current_speed)
print(truckcar.nitro)
truckcar.apply_breaks()
print(truckcar.current_speed)
print(truckcar.nitro)
truckcar.accelerate()
print(truckcar.current_speed)
print(truckcar.nitro)
print(truckcar.sound_horn())
