#Defining function for buyer's name
def buyer_name():
    while True:
        buyerName = input("Please enter the buyer's name: ")
        if buyerName.isalpha():
            break
        else:
            print("The name cannot be numeric.")
            # buyerName = input("Please enter the buyer's full name: ")

    return buyerName

#Defining function for buyer's contact
def buyer_contact():
    while True:
        buyerContact = input("Enter the buyer's phone number: ")
        if buyerContact.isdigit():
            buyerContact = int(buyerContact)
            break
        else:
            print("The numbers must be numeric.")

    return buyerContact

#Defining function for buyer's address
def buyer_address():
    while True:
        buyerAddress = input("Enter the buyer's address: ")
        if buyerAddress.isalpha():
            break
        else:
            print("The address cannot be numeric.")

#Defining function for quantity validation
def quantity_validation_restock(dictionary, serial):
    quantity = int(input("Enter quantity: "))
    laptop_selected = dictionary[serial][3]
    while quantity <= 0:
        print("Error quantity.")
        print("\n")
        quantity = int(input("Enter quantity again: "))
    return quantity


#Defining function for bill restock
def bill_restock_data(restock_laptop, dictionary, serial, selection, restocking, addressOfBuyer):
    nameOfProduct = dictionary[serial][0]
    brandName = dictionary[serial][1]
    selected_quantity = selection
    price_initial = dictionary[serial][2]
    withoutDollar = dictionary[serial][2].replace("$","")
    actual_price_without_dollar = int(withoutDollar)*int(selected_quantity)
    actual_price = str("$"+str(actual_price_without_dollar))
    vat = actual_price_without_dollar * 0.13
    withVat = actual_price_without_dollar + vat

    restock_laptop.append([nameOfProduct,brandName, selected_quantity,price_initial,actual_price, actual_price_without_dollar, vat, withVat])
    return restock_laptop

#Defining function for dictionary
def laptop():
    file = open("laptop.txt", "r")
    laptopDictionary = {}
    laptopId = 1
    for line in file:
        line = line.replace("\n", "")
        laptopDictionary.update({laptopId: line.split(",")})
        laptopId = laptopId + 1
    file.close()

    return laptopDictionary

    print(
          "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(
        "|S.No.\t\t\t\t|Laptop Name\t\t\t\t|Company Name\t\t\t\t|Price\t\t\t\t|Quantity\t\t\t\t|Processor\t\t\t\t|Graphics Card|")
    print(
        "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    return buyerAddress

#Defining function for serial number validation
def serial_number(dictionary):
    while True:
        laptopSerialNumber = input("Enter the serial number of the customer's choice: ")
        try:
            laptopSerialNumber = int(laptopSerialNumber)
            break
        except ValueError:
            print("The serial number must be a positive integer. ")

    while laptopSerialNumber > len(dictionary) or laptopSerialNumber <= 0:
        print("The serial number is not mentioned in the list above,")
        try:
            laptopSerialNumber = int(input("Please provide the ID that the customer wants: "))
        except ValueError:
            print("\n")
            print("Invalid input. Try entering 1/2/3/4/5 only!")
    return laptopSerialNumber

#Defining function for quantity selection validation
def quantity_selection(dictionary, serial):
    while True:
        try:
            buyCount = int(input("How many does the customer want to buy? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    selectedQuantity = dictionary[serial][3]
    while buyCount <= 0 or buyCount > int(selectedQuantity):
        print(
            "Dear Admin, the selected quantity is not available in our shop. Please look again in the table. ")
        print("\n")
        try:
            buyCount = int(input("How many does the customer want to buy? "))
        except ValueError:
            print("\n")
            print("Invalid input. Please enter a valid integer. ")
    if buyCount <= int(selectedQuantity):
        print("The product is available! ")

    return buyCount


#Defining function bill requirements
def bill_requirements(boughtLaptops, dictionary, serial, selection, updating):
    productName = dictionary[serial][0]
    companyName = dictionary[serial][1]
    userSelectedQuantity = selection
    laptopPrice = dictionary[serial][2]
    selectedItemPrice = dictionary[serial][2].replace("$", "")
    totalPrice = int(selectedItemPrice) * int(userSelectedQuantity)
    totalPrice = int(totalPrice)

    shippingCost = 50

    boughtLaptops.append([productName, companyName, userSelectedQuantity, laptopPrice, totalPrice])


    print("\n")

    return boughtLaptops

#Defining function for buying more laptops
def progress_buying(required_info, date_string, total):
    shippingCost = 50
    print("\n")
    print("\t\t\t\t\t\t--------------------------")
    print("\t\t\t\t\t\t    Pratik Laptop Shop")
    print("\t\t\t\t\t\t--------------------------")
    print("\t\t\t\t\t\t\tYour bill ")
    print("\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t",   date_string)
    print("\n")
    print(
        "---------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\tLaptop Details: ")
    print(
        "---------------------------------------------------------------------------------------------------------------------------------")
    print(
        "\t Item name\t  Company Name\t   Total Quantity\tLaptop Price\t  Total")
    print(
        "---------------------------------------------------------------------------------------------------------------------------------")
    for i in required_info:
        print("\t", i[0], "\t", i[1], "\t\t", i[2], "\t", i[3], "\t" "$", i[4])
    print(
        "---------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t   Your Shopping Cost is: $", shippingCost)
    sp = total + 50
    print("\t\t\t\t\t\t  Grand Total With shipping cost: $",sp)
    print("\n")
    print("THANK YOU FOR CHOOSING PRATIK'S LAPTOP STORE! ")
    print("\n")

    return sp

#Defining function for restocking bill 
def billrestock(dictionary, serial, selection, restocking, stocking_again, total, vat, withVat, contactOfBuyer, nameOfBuyer, addressOfBuyer,date_string):

    print("\n")
    print("\n")
    print("\t\t\t\t\t\t-------------------------------")
    print("\t\t\t\t\t\t    Manufacturer Laptop Shop")
    print("\t\t\t\t\t\t------------------------------")
    print("\n")
    print("\t\t\t\t\t\t\t", "Your Bill")
    print("\n")
    print("\t", date_string)
    print("-------------------------------------")
    print("\tCustomer name:", nameOfBuyer)
    print("\tCustomer contact:", contactOfBuyer)
    print("\tCustomer address:", addressOfBuyer)
    print("-------------------------------------")
    print("\n")
    print(
        "---------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\tLaptop Details: ")
    print(
        "---------------------------------------------------------------------------------------------------------------------------------")
    print(
        "\t Item name\t  Company Name\t   Total Quantity\tLaptop Price\t  Total")
    print(
        "---------------------------------------------------------------------------------------------------------------------------------")
    for i in stocking_again:
        print("\t",i[0],"\t",i[1],"\t\t",i[2],"\t",i[3],"\t", i[4])
    print(
        "---------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\tTotal is: $", total)
    print("\t\t\t\t\t\t\t     The VAT Amount is: $", vat)
    print("\t\t\t\t\t\t\tPrice with 13% VAT added: $", withVat)
    print("\n")
