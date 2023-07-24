#Defining function for restocking laptop
def laptop_restock(dictionary, serial, selection):
    dictionary[serial][3] = int(dictionary[serial][3]) + int(selection)
    file = open("laptop.txt", "w")
    for i in dictionary.values():
        file.write(str(i[0]) + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]) + "," + str(i[4]) + "," + str(
            i[5]) + "\n")
    file.close()

#Defining function for updating the text file
def updating_text_file(dictionary, serial, selection):
    # update laptopDictionary with new quantity
    dictionary[serial][3] = int(dictionary[serial][3]) - int(selection)

    # creating a temporary list to store the updated laptops
    laptopList = []
    for values in dictionary.values():
        laptopList.append(
            str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(
                values[4]) + "," + str(values[5]))
    

    file = open("laptop.txt", "w")
    for item in laptopList:
        file.write(item + "\n")
    file.close()

    return laptopList

#Defining function for external bill
def bill_txt(boughtLaptops, required_info, date_string, nameOfBuyer, contactOfBuyer, addressOfBuyer, dictionary, serial,
             selection, terminal_bill, total):
    sp = total + 50
    shippingCost = 50
    file = open(str(nameOfBuyer) + str(date_string) + ".txt", "w")
    file.write("\n")
    file.write("\t\t\t\t\t\t Pratik Laptop Shop")
    file.write("\n")
    file.write("\n")
    file.write("\t\t\t\t\t\t\tYour bill ")
    file.write("\n")
    file.write("\n")
    file.write("Date:" + str(date_string))
    file.write("\n")
    file.write("\n")
    file.write("Customer Name: " + str(nameOfBuyer))
    file.write("\n")
    file.write("Customer Phone Number: " + str(contactOfBuyer))
    file.write("\n")
    file.write("Customer Address:" + str(addressOfBuyer))
    file.write("\n")
    file.write("\n")
    file.write("\t\t\t\t\t\tLaptop Details: ")
    file.write("\n")
    file.write(
        "---------------------------------------------------------------------------------------")
    file.write("\n")
    file.write(
        "\tItem name \t\t Company Name \tTotal Quantity\tLaptop Price\t Total")
    file.write("\n")
    file.write(
        "---------------------------------------------------------------------------------------")
    file.write("\n")
    for i in required_info:
        file.write("\t" + str(i[0]) + "\t\t" + str(i[1]) + "\t\t\t" +  str(i[2]) + "\t" + str(
            i[3]) + "\t\t" + "$" + str(i[4]) + "\t" + "\n")
    file.write("\n")
    file.write(
        "---------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\tYour Shopping Cost is: $" + str(shippingCost))
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\tGrand Total(With Shipping cost): $" + str(sp))
    file.write("\n\n")
    file.write("THANK YOU FOR CHOOSING PRATIK'S LAPTOP STORE! ")
    file.write("\n")
    file.write("DO VISIT AGAIN! ")


#Defining function for external restock bill
def restockbilltxt(dictionary, date_string,serial, restocking, stocking_again, restock, nameOfBuyer,contactOfBuyer, addressOfBuyer, total, vat, withVat):
    file = open("restock" + str(nameOfBuyer) + str(date_string) + ".txt", "w")
    file.write("\n")
    file.write("\t\t\t\t\t\t Manufacturer Laptop Shop")
    file.write("\n")
    file.write("\n")
    file.write("\t\t\t\t\t\t\tYour bill ")
    file.write("\n")
    file.write("\n")
    file.write("Date:" + str(date_string))
    file.write("\n")
    file.write("\n")
    file.write("Customer name:" + str(nameOfBuyer))
    file.write("\n")
    file.write("Customer Phone Number: " + str(contactOfBuyer))
    file.write("\n")
    file.write("Customer Address:" + str(addressOfBuyer))
    file.write("\n")
    file.write("\n")
    file.write("\t\t\t\t\t\tLaptop Details: ")
    file.write("\n")
    file.write(
        "---------------------------------------------------------------------------------------")
    file.write("\n")
    file.write(
        "\tItem name \t\t  Company Name \tTotal Quantity\tLaptop Price\t Total")
    file.write("\n")
    file.write(
        "---------------------------------------------------------------------------------------")
    file.write("\n")
    for i in stocking_again:
        file.write(
            str("\t" + str(i[0]) + "\t\t" + str(i[1]) + "\t\t\t" +str(i[2]) + "\t" + str(i[3])+ "\t\t" +  str(i[4])))
        file.write("\n")
        file.write(
            "---------------------------------------------------------------------------------------")
        file.write("\n")
    
    file.write("\t\t\t\t\t\t\t\t\t\t\t  Total is: $" + str(total)+"\n")
    file.write("\t\t\t\t\t\t\t\t\t\tThe VAT Amount is: $" + str(vat))
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\tPrice with 13% Vat: $" + str(withVat))
    file.write("\n")
    file.write("\n")
    file.write("THANK YOU FOR VISITING MANUFACTURER'S STORE!")
    file.write("\n")
    file.write("DO VISIT AGAIN!")





