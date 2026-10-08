class Device:
  def __init__(self, name, power):
    self.name = name
    self.power = power 
    
  def display(self):
    print(f"Device Name: {self.name}\nPower: {self.power}")  
    
d = Device("Laptop", "Battery")
d.display()