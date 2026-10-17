# child / derived class
class SmartPhone(Phone):
  def __init__(self,model , battery , camera,processor):
    super().__init__(model,battery,camera)
    self.processor = processor

   ## modified method
  def charge(self,hour):
    print("fast charging in process")
    super().charge(hour)
