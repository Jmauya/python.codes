class SmartPhone_CoolingMode(SmartPhone,Cooling_Mechanism):
   def __init__(self,model , battery , camera,processor,cooling_method):
    SmartPhone.__init__(self,model,battery,camera,processor)
    Cooling_Mechanism.__init__(self,cooling_method)
