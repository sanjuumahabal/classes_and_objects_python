#WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
#order based on the ram size.

class Laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd
        
    def showConfig(self):
        print(f"Brand: {self.brand}, RAM: {self.ram}GB, CPU: {self.cpu}, HDD: {self.hdd}GB")
        
laptop1 = Laptop("Dell", 8, "i5", 512)
laptop2 = Laptop("HP", 16, "i7", 1024)
laptop3 = Laptop("Lenovo", 12, "i5", 256)

laptops = [laptop1,laptop2,laptop3]

laptops.sort(key=lambda x:x.ram)

for laptop in laptops:
    laptop.showConfig()