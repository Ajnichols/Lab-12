#For this project we need to work on a class
#This class will be named Car and will have
#three data attributes; __year_model, __make,
# and __speed. The class should also have an
#__init__ method that accepts year model and
#make as arguments. These values are assigned
#to the object's year model and make attributes.
#It should also assign 0 to the speed data att.
#It should have 3 methods; accelerate, brake,
#and get_speed. The first two +/- 5 and the
#last retrieve's the speed.
#After all that is set up create a car program.
#The programs accelerates 5 times and retrieve's
#the speed 5 times alternating. Then does the same
#with brake.

def main():

    #This is the class I'm making, contains what
    #is required above. I believe I'm setting up
    #the attributes correctly.
    class Car:
        __year_model = ""
        __make = ""
        __speed = 0

        #This is the __init__ which should allow
        #the year and make as arguments and set
        #the speed to zero if the above doesnt
        #do that already.
        def __init__(self, __year_model, __make):
            self.__year_model = __year_model
            self.__make = __make
            self.__speed = 0

        #Finally I'm defining the three methods
        #my later program will call on.
        def accelerate():
            __speed + 5

        def brake():
            __speed - 5

        def get_speed():
            print(__speed)

    #This should be the program that accelerates
    #5 times with intermitten printouts and then
    #does the same with braking.
    def testDrive():
        a = 0
        while a < 5:
            a += 1
            accelerate()
            print(__speed)
        b = 0
        while b < 5:
            b += 1
            brake()
            print(_speed)

    testCar = Car()
    
    testCar.testDrive()

main()
