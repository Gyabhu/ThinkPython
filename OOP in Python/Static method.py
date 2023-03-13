# This method doesnot take class nor method

class Vehicle:
    @staticmethod
    def electric(range):
        if range > 90:
            return 'Yes!'
        return'Nope!'

yatrip1 = Vehicle()
print(yatrip1.electric(110))

print(Vehicle.electric(165))
print(Vehicle.electric(60))