#Importing

import datetime
from operations import *
from read import *
from write import *
now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d_%H-%M-%S")

#Designing layout for terminal
print("\n")
print("\n")
print(
    "------------------------------------------|-------------------------------------|--------------------------------------------------")
print(
    "Address: New Road, Kathmandu\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t     Pratik Laptop Store\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPhone: 9847346220")
print(
    "------------------------------------------|-------------------------------------|--------------------------------------------------")
print("\t \t \t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t     Welcome to Pratik's Laptop Store!")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t.......................................")

print("\n")

#Calling laptop function and storing it in dictionary variable
dictionary = laptop()

#Setting total to 0 for calculations
total = 0

#Setting loop to true for the entire program
loop = True
while loop == True:

    print("Press 1 to sell.")
    print("Press 2 to purchase.")
    print("Press 3 to exit.")

#Using try except and while loop over it to catch any invalid data input
    while True:
        try:
            chooseOption = int(input("Enter your choice:"))
            break
        except:
            print("Invalid.")
    restock_laptop = []
    boughtLaptops = []
    if chooseOption == 1:

#Calling buyer_name(), buyer_contact() and buyer_address() functions in main and storing them in variables for future use
        nameOfBuyer = buyer_name()
        contactOfBuyer = buyer_contact()
        addressOfBuyer = buyer_address()

#Setting buyMore to true for looping if the customer wants to buy more laptops
        buyMore = True

#Calling buy_more(), serial_number(), quantity_selection(), updating_text_file(), bill_requirements() functions and storing them
        while buyMore == True:
            wantMore = buy_more()

            serial = serial_number(dictionary)

            selection = quantity_selection(dictionary, serial)

            updating = updating_text_file(dictionary, serial, selection)

            required_info = bill_requirements(boughtLaptops, dictionary, serial, selection, updating)

            # if continueBuying == "Y":
            continueBuying = input("Does the customer want to buy another laptop? (Y/N) ").upper()
            if continueBuying == "Y":
                buyMore = True
            else:
                buyMore = False
                for i in required_info:
                    total += int(i[4])
                terminal_bill = progress_buying(required_info, date_string, total)
                bill_txt(boughtLaptops, required_info, date_string, nameOfBuyer, contactOfBuyer, addressOfBuyer, dictionary, serial, selection, terminal_bill, total)

#For option 2
    elif chooseOption == 2:
        nameOfBuyer = buyer_name()
        contactOfBuyer = buyer_contact()
        addressOfBuyer = buyer_address()

#Set reloop to true
        reloop = True
        while reloop == True:
            wantMore = buy_more()

#Call all the functions again and call the billing functions from write.py
            dictionary = laptop()
            serial = serial_number(dictionary)
            selection = quantity_selection(dictionary, serial)
            restocking = laptop_restock(dictionary, serial, selection)
            againRestock = input("Restock more? (Y/N): ").upper()
            stocking_again = bill_restock_data(restock_laptop, dictionary, serial, selection, restocking, addressOfBuyer)
            if againRestock == "Y":
                reloop = True
            else:
                reloop = False
                for i in stocking_again:
                    total += int(i[5])
                vat = total * 0.13
                withVat = total + vat
                billrestock(dictionary, serial, selection, restocking, stocking_again, total, vat, withVat, contactOfBuyer, nameOfBuyer, addressOfBuyer, date_string)
                restockbilltxt(dictionary, date_string,serial, restocking, stocking_again, stocking_again, nameOfBuyer,contactOfBuyer, addressOfBuyer, total, vat, withVat)
            print("THANK YOU FOR VISITING MANUFACTURER'S STORE!")
            print("\n")
            print("Laptops will be restocked again.")
            print("\n")

#For option 3
    elif chooseOption == 3:
        print("Thanks for visiting our store!")
        loop = False
        
    else:
        print("The input", chooseOption, "Did not match the number mentioned above. Please enter the number that is mentioned. ")


