#!/usr/bin/env python3
#Seems something going wrong when I connect output on line 52 here.
#repost Thank you Joseph for emailing me! the problem is perfectly solved!
''' This function can create a car with 6 attributes including name color, mileage, brand, year they made 
in, and it can perform basic function like: create car and print their information. 
Furthermore it can turn on a car's engine, and drive you somewhere.
'''

from Classcar import Car
from Classcar import create_car
import random

def test_car_change(Car, new_car):
    Car.name = new_car
    return Car.name == new_car
def quick_test_car_generate():
    # Test section: I wrote a function to generate new object in a class
    # This function let us see if methods from Car-class works.
    testsubaru = Car("legacy", "Blue", "73000", "2015", "Subaru", False)
    print(f"Test attempt 1: testsubaru:{testsubaru.to_string()}")

    testtoyota = Car("avalon", "White", "230000", "2004", "Toyota", False)
    print(f"Test attempt 2: testtoyota: {testtoyota.to_string()}")
    
    print(f"Toyota engine status (True):({testtoyota.turn_on_the_car()})")
    print(f"Subaru engine status (False):({testsubaru.ignition})")
    tnc = test_car_change(testsubaru, "Subaru")
    print(f"Test attempt 3: Test_car_change result: \n{tnc}")
    ran = random.randrange(0, 2)
    if ran == 0:
        current_car = testtoyota
        print("yo got toyota this time")
        return current_car
    else:
        current_car = testsubaru
        print("yo got subaru this time")
        return current_car
def quick_test_methods():
    current_car = quick_test_car_generate()
    print(f"Test attempt 4: Subi turn on:{current_car.turn_on_the_car()}")
    print(f"Test attempt 5: Subi test drive:{ current_car.drive()})")
    
    # Here in this way it will store subi and toyota into current car to test other options from menu.


    # This section works perfectly so far. Is there any way to get this method's output into another method?
def main():
# Here are the interface of menu part.
    menu = " \
    ---------       Menu    --------\n \
    0. Quit\n \
    1. Create car\n \
    2. Look at current car\n \
    3. Turn on the car\n \
    4. Try a random drive! Lets see where did you end up at!\n \
   *Start with tests\n \
    5. Perform a quick test!\n \
    6. Generate quick test and use its result!\n \
   *Start with write and read\n \
    7. Write a car!\n \
    8. Read a car and print it out!\n \
    "
# Here are the menu algorithm part (this is algorithm part right?)
    #A Set choice to -1 and create while >0 loop. This is pretty useful.
    menu_prompt = "What would you like to do? "
    current_car = None
    choice = -1
    #B Further algorithm
    while choice != 0:
        choice = int(input(menu + menu_prompt))
        # If there is a car this is true
        #0 quit
        if choice == 0:
            print("Thank you! Goodbye!")
        #1 creating
        elif choice == 1:
            current_car = create_car()
        #2 look up the current one and give false solution
        elif choice == 2:
            if current_car != None:
                #pulling method from another file here.
                print(f"\n Your current car information are:\n{current_car.to_string()}")
            else:
                print("No car yet inputed for information look up, create(1) a car or quickstart(6) one first!. ")
        #3 Igniting, as one of the starting method
        elif choice == 3:
            if current_car != None:
                #pulling method
                print(f"\nYour engine status now are:\n{current_car.turn_on_the_car()}")
            else:
                print("No car yet inputed for turning engine on, create(1) a car or quickstart(6) one first!. ")
        #4 Driving, this method just gives you a random location
        elif choice == 4:
            if current_car != None:
                print(current_car.drive())
            else:
                print("No car yet inputed for drive, create(1) a car or quickstart(6) one first!. ")
        
        elif choice == 5:
            #Raw quick test, just output string
            quick_test_car_generate()
            quick_test_methods()
        elif choice == 6:
            #But this one makes everything work around quick test result.
            current_car = quick_test_car_generate()
        
        elif choice == 7:
            # This write out a current car.
            # I found that no matter whats words in that perentathies it just accepts anyway.
            if current_car != None:
                Car.write_car(current_car)
                print("current car write out successful!")
            else:
                print("No volunteer car yet inputed for write out car, create it or Quick start one first!")
        elif choice == 8:
            # This read car from a existed file
            Car.read_car(current_car)
        else: #if there is unknown entry
            print(f"Unknown choice 12 : {choice}")       
if __name__ == "__main__":
    main()
    #this main() is menu function