#========The beginning of the class==========
class Shoe:
        
        #initialising the variables
    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    #defining method to return the cost of a shoe
    def get_cost(self):
        return float(self.cost)
    
    #Defining a method to return the quantity in stock of a shoe
    def get_quantity(self):
        return int(self.quantity)
    
    #defining string method to print the objects in as a string
    def __str__(self):
        return f"Country: {self.country} \nCode: {self.code} \nProduct: {self.product} \nCost: {self.cost} \nQuantity: {self.quantity}\n"
        
'''
The list will be used to store a list of objects of shoes.
'''
#creating an empty list that will be used to store all the data from the inventory.txt file
shoe_list = []

#==========Functions outside the class==============

#defining a function that read all the data from the inventory.txt file and append every line as an object to the shoe list
def read_shoes_data():
    file = open('inventory.txt', 'r')
    for line in file:
        line = line.strip('\n').split(',')
        if line[0] != 'Country':  #using if statement to skip the first line 
            try:
                shoe_obj = Shoe(line[0], line[1], line[2], float(line[3]), int(line[4])) #appending the lines to the shoe list
                shoe_list.append(shoe_obj)
            
            #Excepting index error, if the line does not have all the items
            except IndexError:
                print(f"There are items missing in this line, please fix it: \n{line}")
            #Excepting value error, if the cost or quantity have values that are not numbers
            except ValueError:
                print(f"Please make sure that cost and quantity values are numbers on the following line: \n{line}")
                
    file.close() #Closing the file 
    
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

#Defining a function so the user has the option of add a shoe to the shoe list
def capture_shoes():
    
    #Asking the user for input for all the arguments
    country = input("Enter the country where the shoe is from: ")
    code = input("Enter the code of the shoe: ")
    product = input("Enter the name of the shoe: ")
    while True:
        
        #Using try/except to make sure the user enter numbers for cost and quantity
        try:
            cost = float(input("Enter the cost of this shoe: "))
            quantity = int(input("Enter the quantity in stock for this shoe: "))
            break
        except ValueError:
            print("Please make sure you entered only numbers for cost and quantity")
    
    #using all the inputs to create a new object and appending it to the shoe list
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    return 

#Defining a function to view all the content of the shoe list
def view_all():
   
    #Using for loop to iterate through the list and printing the objects in a string format
    for product in shoe_list:
        print(f"Product {shoe_list.index(product)}: \n{product.__str__()}")
        
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

#Defining a function that returns the product with the lowest quantity in stock and ask the user if he/she would like to re-stock the item
def re_stock():
    
    #Setting a object to the variables just to start the code
    shoes = shoe_list[0]
    quantity = shoe_list[0].get_quantity()
   
    #using for loop to iterate through the shoe list
    #using get_quantity() method to get the quantity for the object being looped.
    #if that object quantity is smaller than the quantity variable, that becomes the new lowest quantity item.
    for i in shoe_list:
        if i.get_quantity() < quantity:
            shoes = i
            quantity = i.get_quantity()
    print(f"The shoe with the lowest quantity in stock is '{shoes.product}' and its stock is '{quantity}'.")
    
    #Using while loop to keep asking the user again if the input is incorrect.
    while True:
        restock = input("Would you like to restock this item? Yes or No").lower()
        
        if restock == 'yes':
            
            #if the input is yes, ask the user for a new quantity
            #using try/except to make sure the user will enter a number
            while True:
                try:
                    new_quantity = int(input("Enter the new quantity for the stock of this shoe: "))
                    shoes.quantity = new_quantity
                    break

                except ValueError:
                    print('Oops, invalid input! Please try again and make sure you entered a number..')
            
            #opening file in read mode and storing all the lines to a new shoe list that will overwrite the current data from the inventory.txt later
            file = open('inventory.txt', 'r')
            new_shoe_list = []
            for line in file:
                    line = line.strip('\n').split(',')
                    
                    #matching the lowest quantity shoe code, to the right line in the file
                    if line[1] == shoes.code:
                        line[4] = str(new_quantity)  #when it matches, replace the quantity for the quantity the user entered previously
                    new_shoe_list.append(line)
                    
            file.close() #Closing the file
            
            #Reopening the file in write mode and overwriting the data with the content from the new shoe list
            file = open('inventory.txt', 'w')
            for i in new_shoe_list:
                file.write(','.join(i)+'\n') 
            file.close()
            break
                
        elif restock == 'no':
            break
        
        else:
            print("Valid input! Please try try again..")
        
            
    
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

#Defining a function that will look for a specific shoe and return it by using the its code
def search_shoe():
    code = 0 
    
    #Using while loop to keep asking the user until '-1' is entered.
    while code != '-1':
        code_found = False #Setting a variable to False so the code can break when it becomes True
        code = input('Enter the code of the shoe you want to search or enter "-1" to exit: ')
            
        for item in shoe_list:
            if item.code == code:  #Checking if the code the user entered matches with any code in the shoe list
                print(item.__str__())
                code_found = True
                break
        
        #If code does not match, and user did not enter '-1' to exit the code, print a message and let it try again
        if code_found == False and code != '-1':
            print("The code you entered does not match any of the codes in the inventory. Please try again..")
        
        '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

#Defining a fucntion that will return the whole value of stock for each shoe in the shoe list
def value_per_item():
    
    #Usinf for loop to iterate through the shoe list
    for i in shoe_list:
        total_value = i.get_cost() * i.quantity  #Calculating the total value of stock for each shoe
        print(f"The total value for '{i.product}' is: £{total_value}\n\n")
    return
    
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

#Defining a function to return the shoe with the highest quantity in stock and printing it is for sale.
def highest_qty():
    
    #Setting a object to variables just to start the code
    highest_shoe = shoe_list[0].product
    highest_quantity = shoe_list[0].quantity
    
    #Using for loop to iterate through the shoe list
    for i in shoe_list:
        if i.quantity > highest_quantity:  #If the quantity of the item the is being looped is higher than the one in the variable, that becomes the new highest quantity
            highest_shoe = i.product
            highest_quantity = i.quantity
    print(f"{highest_shoe} is the shoe with the higher quantity in stock and it is for sale!")
    
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============

#Calling the fucntion to read the data from the text file before the user selects the menu to prevent errors.
read_shoes_data()
print('Data has been read')

#Using while loop to keep asking the user for an input until the user enters 'exit'
while True:
    menu = input('''Please choose one of the following:
r = read data from inventory
c = add a shoe to the inventory
v = view all shoes in the inventory
rs = re-stock low stock shoes
s = search for a specific shoe
vpi = check the total value in stock of all the shoes
h = view the shoe with the highest quantity in stock
exit = exit the code
''')
    
    #Using if statements to call the functions depending on the user input
    if menu == 'r':
        read_shoes_data()
        print('Data has been read')
    
    elif menu == 'c':
        capture_shoes()
    
    elif menu == 'v':
        view_all()
    
    elif menu == 'rs':
        re_stock()
    
    elif menu == 's':
        search_shoe()
    
    elif menu == 'vpi':
        value_per_item()
    
    elif menu == 'h':
        highest_qty()
    
    elif menu == 'exit':
        print('Goodbye!')
        break
    
    #If the user input does not match any of the above, print an error message and let it try again.
    else:
        print('Invalid input! Please try again..')
        
    