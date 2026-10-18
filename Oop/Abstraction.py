from abc import  ABC , abstractmethod

class Telephone(ABC):

  @abstractmethod
  def make_call(self):
    pass



class Sphone(Telephone):
  def make_call(self):
    print("Making a call using SPhone")



class Iphone(Telephone):
   def make_call(self):
    print("Making a call using IPhone")


