class Camera:

    def __init__(self, name):
        self.name = name

    # method
    def capture(self):
        print("A photo is captured")


class Smart_Phone(Camera):

    def __init__(self, name, resolution):
        super().__init__(name)
        self.resolution = resolution

    # method overriding
    def capture(self):
        print("Photo is captured by a Phone")


class DSLR(Camera):

    def __init__(self, name, resolution):
        super().__init__(name)
        self.resolution = resolution

    def capture(self):
        print("Photo is captured by DSLR")


class Drone(Camera):

    def __init__(self, name, resolution):
        super().__init__(name)
        self.resolution = resolution

    def capture(self):
        print("Photo is captured by Drone")


# Instantiation

phone = Smart_Phone("Phone", 30)
dslr = DSLR("DSLR", 200)
drone = Drone("Drone", 150)

# Method calls
phone.capture()
dslr.capture()
drone.capture()
