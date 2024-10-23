#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:w0457754   
#Student Name: William Wilson

def main():
    #Display welcome message
    print("Welcome to Geoff's Auto Insurance. I am Insurance Agent William. \nFor your quote, I am going to start with your gender, age, then vehicle cost.")
    
    #Store gender age precentage
    precentageM1 = .25
    precentageM2 = .17
    precentage3 = .10
    precentageF1 = .20
    precentageF2 = .15

    #Gather input from user about gender, age, vehicle price
    gender = input("Are you 'Male' or 'Female'?: ").lower()
    age = input("Please enter your age: ")
    vehiclePrice = float(input("Please enter the purchase price of the vehicle: "))

    #compare input to data for male and calculate
    if gender.lower() == "male":
        if age >= "15" and age <= "24":
            insurance = (vehiclePrice * precentageM1) / 12
        elif age >= "25" and age <= "39":
            insurance = (vehiclePrice * precentageM2) / 12
        elif age >= "40" and age <= "69":
            insurance = (vehiclePrice * precentage3) / 12
        else:
            print("You do not qualify for insurance. We apologize for the inconvenience.")
    
    #compare input to data for female and calculate
    if gender.lower() == "female":
        if age >= "15" and age <= "24":
            insurance = (vehiclePrice * precentageF1) / 12
        elif age >= "25" and age <= "39":
            insurance = (vehiclePrice * precentageF2) / 12
        elif age >= "40" and age <= "69":
            insurance = (vehiclePrice * precentage3) / 12
        else:
            print("You do not qualify for insurance. We apologize for the inconvenience.")
    
    #display output for user input data and calculations
    if (gender.lower() == "male" or gender.lower() == "female") and age < "70":
        print("Your monthly insurance will cost: ${0:.2f}".format(insurance))
    else:
        print()

main()