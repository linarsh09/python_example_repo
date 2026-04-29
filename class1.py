class Car(brand, model, year, speed, fuel):
    def __init__(self):
        self.brand() = brand
        self.model() = model
        self.year() = year
        self.speed() = speed
        self.fuel() = fuel
    
    def accelerate():
        print("машина движется")

    def brake():
        print("машина остановилась")

    def get_info():
        print(f"""
        Brand:{brand}
        Model:{model}
        Year: {year}
        Speed: {speed}
        Fuel: {fuel}""")
    
    def refuel():
        for fuel in range(100):
            print(f"{fuel}%")

class ElectricCar(Car, battery_level):
    def accelerate():
        for battery_level in range(100):
            print(f"машина движется! батарея:", 100-battery_level, "%")

m2.Car(BMW, x5, 2025, 200, 59)
res = m2.get_info()
print(res)

