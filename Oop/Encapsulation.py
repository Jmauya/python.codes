# design
class Mobile:
  def __init__(self,name,model,imei):
    self.__name = name
    self.__model = model
    self.__imei = imei # private

  def charge(self):
    print("phone is charging")

  # method imei ta paite pari
  def imei_getter(self):
    return self.__imei

def name_getter(self):
    return self.__name


  def name_setter(self,name):
    self.__name = name

#outside world ( user )

# registration
iphone = Mobile("Phone","17","1xkaf1")

print(iphone.name_getter())

iphone.name_setter("Phitron")


print(iphone.name_getter())
