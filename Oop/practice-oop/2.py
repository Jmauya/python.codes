class MobilePhone:

    def __init__(self, model):
        self.model = model  # Public attribute
        self.__battery = 100  # Private attribute (default 100)

    def use(self, amount=15):
        # Reduce battery, but don't let it drop below 0
        self.__battery = max(0, self.__battery - amount)
        print(
            f"[{self.model}] Used device. Battery level: {self.__battery}%"
        )

    def charge(self, amount=20):
        # Increase battery, but cap it at a maximum of 100
        self.__battery = min(100, self.__battery + amount)
        print(
            f"[{self.model}] Charged device. Battery level: {self.__battery}%"
        )

    def get_battery(self):
        # Return/show the current battery level
        return self.__battery


# 1. Create a phone object
my_phone = MobilePhone("Pixel 9")

# 2. Accessing the public attribute works fine
print(f"Phone Model (Public): {my_phone.model}")

# 3. Using methods to modify and check battery
my_phone.use(30)   
my_phone.charge(10)  
print(f"Current Battery via getter: {my_phone.get_battery()}%")

# 4. Trying to access the private attribute (__battery) directly
try:
    print(my_phone.__battery)
except AttributeError as e:
    print(
        f"\n[Error Caught]: Cannot access __battery directly because it is private!"
    )
    print(f"Details: {e}")
