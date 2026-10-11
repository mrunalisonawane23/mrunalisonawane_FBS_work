from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, persons):
        self.persons = persons

    @abstractmethod
    def calculate_toll(self):
        pass

class TwoWheeler(Vehicle):
    def calculate_toll(self):
        basic_toll = 20
        extra_charge = 0
        if self.persons > 2:
            extra_charge = (self.persons - 2) * 10
        return basic_toll + extra_charge

class ThreeWheeler(Vehicle):
    def calculate_toll(self):
        basic_toll = 30
        extra_charge = 0
        if self.persons > 3:
            extra_charge = (self.persons - 3) * 20
        return basic_toll + extra_charge

class FourWheeler(Vehicle):
    def calculate_toll(self):
        basic_toll = 40
        extra_charge = 0
        if self.persons > 4:
            extra_charge = (self.persons - 4) * 40
        return basic_toll + extra_charge

class HeavyVehicle(Vehicle):
    def calculate_toll(self):
        basic_toll = 60
        extra_charge = 0
        if self.persons > 6:
            extra_charge = (self.persons - 6) * 100
        return basic_toll + extra_charge

def main():
    while True:
        print("\n==============================")
        print("      TOLL PLAZA SYSTEM       ")
        print("==============================")
        print("1. Two Wheeler")
        print("2. Three Wheeler")
        print("3. Four Wheeler")
        print("4. Heavy Vehicle (More than 4 wheels)")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Please enter a valid integer choice!")
            continue
            
        if choice == 5:
            print("Exiting Toll System. Have a safe journey!")
            break
            
        if choice in [1, 2, 3, 4]:
            try:
                persons = int(input("Enter total number of persons in the vehicle: "))
                if persons < 0:
                    print("Number of persons cannot be negative.")
                    continue
            except ValueError:
                print("Please enter a valid number for persons!")
                continue
            
            vehicle = None
            if choice == 1:
                vehicle = TwoWheeler(persons)
            elif choice == 2:
                vehicle = ThreeWheeler(persons)
            elif choice == 3:
                vehicle = FourWheeler(persons)
            elif choice == 4:
                vehicle = HeavyVehicle(persons)
        
            total_toll = vehicle.calculate_toll()
            print(f"\n-> Total Toll Amount to Pay: Rs {total_toll}")
        else:
            print("Invalid choice! Please choose between 1 and 5.")

if __name__ == "__main__":
    main()