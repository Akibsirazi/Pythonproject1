import time


class car():

    def __init__(self,name,age):
      self.name=name
      self.age=age

    def print_details(self):
        print("My car is a {self.name}it is {self.age} years old")

        def print_starting_up(self):
            print("starting...")
            time.sleep(1)
            print("Vroom,vroom")
        def turn_off_engine(self):
            turn_off_engine=input("Turn off engine or not y or n?")


            if turn_off_engine.lower()=="y":
              print("Engine is turning off")
              quit()
            else:
                 print("Car is still running")




car1=car("BMW",5)
car1.print_details()

