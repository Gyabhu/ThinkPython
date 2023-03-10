class Rocket:
    category = 'reuseable'

    def __init__(self,name,payload,thrust):
        self.name = name
        self.payload = payload
        self.thrust = thrust

    def mission(self):
        return f"This is {self.name} having {self.thrust} lbs of thrust, delivering {self.payload} lbs of payload into LEO."

    def change_payload(self):
        self.payload = '35,000'
        return f"This is {self.name} having {self.thrust} lbs of thrust, delivering {self.payload} lbs of payload into GTO."


falconhvy = Rocket('Falcon Heavy','141,000', '5,000,000')
falcon9 = Rocket('Falcon 9','50,265','1,700,000')


print(falconhvy.mission())
print(falconhvy.change_payload())
print(falcon9.mission())