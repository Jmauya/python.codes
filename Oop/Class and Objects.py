# base class / parent class

class Phone:
  category = "Electronics"

  # constructor
  def __init__(self,model , battery , camera,battery_percentage=100):
    self.model = model
    self.battery = battery
    self.camera = camera
    self.battery_percentage = battery_percentage

  # methods
  def charge(self,hour):
    print(f"charge completed by {hour} {model}")

  def capture(self,photo):
    if(self.battery_percentage)<=0:
      print("No charge")
    else:
      self.battery_percentage-=photo
      print(f"photo captured in {self.model}")



class Cooling_Mechanism:
  def __init__(self,cooling_method):
    self.cooling_method= cooling_method


  #methods
  def cooling_on(self):
    print(f"the system is being cool by {self.cooling_method}")

## creating object

apple = Phone("Iphone17",3000,40)
blueberry = Phone("B-17",4000,30)
motorola = Phone("M-17",3500,35)
apple.capture(10)
print(motorola.battery_percentage)
