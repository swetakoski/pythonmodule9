#9.1
#
# class Car:
#     def __init__(self, regPlate, max_speed):
#         self.regPlate =regPlate
#         self.max_speed = max_speed
#         self.current_speed = 0
#         self.odometer = 0
#
# if __name__ == "__main__":
#
#     Audi= Car(regPlate="ABC-123", max_speed=240)
#     print(f"Registration Number {Audi.regPlate}, Maximum Speed {Audi.max_speed}, km/h"
#     f"Current Speed {Audi.current_speed}, km/h, odometer {Audi.odometer}, km")

#9.2
# class Car:
#     def __init__(self,regPlate, max_speed):
#         self.regPlate = regPlate
#         self.max_speed = max_speed
#         self.current_speed = 0
#         self.odometer = 0
#
#     def accelerate(self, change):
#
#         self.current_speed = max(0, min(self.current_speed + change, self.max_speed))
#
#
# if __name__ == "__main__":
#
#     Audi= Car(regPlate="ABC-123", max_speed=142)
#
#     Audi.accelerate(30)
#     Audi.accelerate(70)
#     Audi.accelerate(50)
#
#
# print(f"Current Speed: {Audi.current_speed}, km/h")
# Audi.accelerate(-200)
# print(f"Final Speed: {Audi.current_speed}, km/h")

# 9.3
# class Car:
#     def __init__(self,regPlate, max_speed):
#         self.regPlate = regPlate
#         self.max_speed = max_speed
#         self.current_speed = 0
#         self.odometer = 0
#
#     def accelerate(self, change):
#         self.current_speed = max(0, min(self.current_speed + change, self.max_speed))
#
#     def drive(self, hours):
#         odometer = self.current_speed * hours
#         self.odometer += odometer
#
# # Main program
# if __name__ == "__main__":
#
#     Bentley = Car(regPlate="ABC-123", max_speed=142)
#
#     Bentley.accelerate(30)
#     Bentley.accelerate(70)
#     Bentley.accelerate(50)
#
#     print(f"Current Speed: {Bentley.current_speed}, km/h")
#     Bentley.accelerate(-200)
#     print(f"Final Speed: {Bentley.current_speed}, km/h")
#     Bentley.drive(1.5)
#
#     print(f"Travelled Distance: {Bentley.odometer}, km")

#9.4

# import random
#
# class Car:
#     def __init__(self, regPlate, max_speed):
#         self.regPlate = regPlate
#         self.max_speed = max_speed
#         self.current_speed = 0
#         self.odometer = 0
#
#     def accelerate(self, change):
#         self.current_speed = max(0, min(self.current_speed + change, self.max_speed))
#
#     def drive(self, hours):
#
#       odometer= self.current_speed * hours
#
#
#       self.odometer += odometer
#
# # Main program
# if __name__ == "__main__":
#
#     cars = [Car(regPlate=f"ABC-{i}", max_speed=random.randint(100, 200)) for i in range(1, 11)]
#
#     race_finished = False
#     hour_count = 0
#
#     while not race_finished:
#
#         for car in cars:
#             car.accelerate(random.randint(-10, 15))
#
#
#         for car in cars:
#             car.drive(1)
#
#
#         for car in cars:
#             if car.odometer>= 10000:
#                 race_finished = True
#                 break
#
#
#         hour_count += 1
#
#
#     print("Race Results:")
#     print(f"{'Registration Number':<15}{'Max Speed (km/h)':<20}{'Final Speed (km/h)':<25}{'Travelled Distance (km)':<30}")
#     for car in cars:
#         print(f"{car.regPlate:<15}{car.max_speed:<20}{car.current_speed:<25}{car.odometer:<30}")
#
#     print(f"\nRace Duration: {hour_count} hours")

