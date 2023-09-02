#!/usr/bin/env python3

class Dog:
    # Class body goes here

    # Instance method definition
    def bark(self):
        print("Woof")
    #New instance method definition
    def sit(self):
        print("The dog is sitting.")
    
fido = Dog()  # Create an instance of the Dog class
fido.bark()   # Call the bark method to produce the output
fido.sit()    #Call the sit method to produce the output

snoopy = Dog()
snoopy.bark() 
snoopy.sit()  #Call the sit method on the snoopy instance


    