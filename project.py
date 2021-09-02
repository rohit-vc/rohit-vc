import pickle
main_data = open("datasaver.p", "rb")
main_data_list = pickle.load(main_data)

customer_details = main_data_list[0]
owner_details = main_data_list[1]
admin = main_data_list[2]
bikes = main_data_list[3]
bike_on_rent = main_data_list[4]

customer_ids = customer_details.keys()
owner_ids = owner_details.keys()
bikes_list = bikes.keys()
bikes_on_rent_list = bike_on_rent.keys()
number_of_bike_for_rent = len(bikes_list)

# print(customer_details)
print((""))
print(("WELCOME!!").center(50,'*'))
print((""))
print(("Bike Rental System").center(50,'-'))
print((""))

def remove_bike_owners():
    counter = 0
    for i in owner_ids:
        counter += 1
        print(f"{counter}. {owner_details[i][1]}, User Id = {i}")
    print("")
    choice = input('Enter User ID of Bike Owner you want to remove: ')
    print(f"{owner_details[i][1]} removed successfully")
    owner_details.pop(choice)
    admistrator_functions()

def remove_customer():
    counter = 0
    for i in customer_ids:
        counter += 1
        print(f"{counter}. {customer_details[i][1]}, User Id = {i}")
    print("")
    choice = input('Enter User ID of Bike Owner you want to remove: ')
    print(f"{customer_details[i][1]} removed successfully")
    customer_details.pop(choice)
    admistrator_functions()

def remove_bikes():
    view_bikes()
    print("")
    choice = input('Enter chassis number of bike to be remove: ').lower()
    print("")
    print(f"{bikes[choice][1]} is removed successfully")
    bikes.pop(choice)
    admistrator_functions()

def admistrator_functions():
    print("")
    print("Please select from the following")
    print("")
    print("1: Add a Customer")
    print("2: Add a Bike Owner")
    print("3: Remove a Customer")
    print("4: Remove a Bike Owner")
    print("5: Remove a Bike")
    print("6: Main Menu")
    print("7: Exit")
    print("")
    choice = int(input('Enter your choice: '))
    if choice ==1:
        customer_registeration()
    elif choice ==2:
        bike_owner_registration()
    elif choice ==3:
        remove_customer()
    elif choice ==4:
        remove_bike_owners()
    elif choice ==5:
        remove_bikes()
    elif choice ==6:
        starter()
    elif choice ==7:
        exit()
    else:
        print("")
        print("Invalid choice!! Please try again")
        admistrator_functions()

def rent_bike():
    counter = 0
    for i in bikes_list:
            counter+=1
            print("")
            print(f"{counter}. {bikes[i][1]}, chassis number = {i}")
            print("Specifications--")
            print(f"Engine Size = {bikes[i][2]} cc, Milage = {bikes[i][3]}")
            print("Rent--")
            print(f"Daily = {bikes[i][4]}, weekly = {bikes[i][5]}, monthly = {bikes[i][6]}")
    print((""))
    print(("---------------------------------"))
    print(f"Total number of bikes available = {counter}.")
    print((""))
    choice = input("Enter chassis number of bike your want to rent: ")
    print("")
    print(f"1: Daily basis - {bikes[choice][4]}₹ per day")
    print(f"2: Weekly basis - {bikes[choice][5]}₹ per week")
    print(f"3: Monthly basis - {bikes[choice][6]}₹ per month")
    print("")
    option = int(input("On what basis you want to rent (enter 1,2 or 3): "))
    print("")
    if option == 1:
        m = 'Day(s)'
        a=4
        interval = int(input("For how many days you want to rent: "))
    elif option == 2:
        m = 'Week(s)'
        a=5
        interval = int(input("For how many weeks you want to rent: "))
    elif option == 3:
        m = 'Month(s)'
        a=6
        interval = int(input("For how many months you want to rent: "))

    bikes[choice].extend([customer_username,m,interval,bikes[choice][a]*interval])
    print("")
    print(f"your total amount will be {int(bikes[choice][a])*interval}₹")
    print("")
    print(f"Your request for renting {bikes[choice][1]} for {interval} {m} has been proceded")
    bike_on_rent[choice] = bikes.pop(choice)
    customer_functions()
    
    
def view_rented_bike():
    counter = 0
    for i in bikes_on_rent_list:
        if customer_username == bike_on_rent[i][7]:
            counter += 1
            print("")
            print(f"{counter:} {bike_on_rent[i][1]}, Chassis Number = {i}")
            print(f"Rended for {bike_on_rent[i][9]} {bike_on_rent[i][8]} ")
    customer_functions()

def return_rented_bike():
    counter = 0
    for i in bikes_on_rent_list:
        if customer_username == bike_on_rent[i][7]:
            counter += 1
            print("")
            print(f"{counter:} {bike_on_rent[i][1]}, Chassis Number = {i}")
            print(f"Rended for {bike_on_rent[i][9]} {bike_on_rent[i][8]} ")
    print("")
    choice = input('Enter Chassis of bike you want to return: ')

    print(f"You rented {bike_on_rent[choice][1]} for {bike_on_rent[choice][9]} {bike_on_rent[choice][8]}")
    print("")
    print("Bill-")
    print("")
    print("----------------------")
    print("| Bike Rental System |")
    print("|                    |")
    print(f"| Bike Name = {bike_on_rent[choice][1]}       |")
    print("|                    |")
    print(f"| Rented for {bike_on_rent[choice][9]} {bike_on_rent[choice][8]} basis |")
    print("|                    |")
    print(f"| Total amount = {bike_on_rent[choice][10]}₹    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("----------------------")
    print("")
    bike_on_rent[choice].pop()
    bike_on_rent[choice].pop()
    bike_on_rent[choice].pop()
    bike_on_rent[choice].pop()

    print("Bike reruned successfully")
    bikes[choice] = bike_on_rent.pop(choice)
    print("")
    customer_functions()



def view_bikes():
    counter = 0
    for i in bikes_list:
            counter+=1
            print("")
            print(f"{counter}. {bikes[i][1]}, chassis number = {i}")
            print("Specifications--")
            print(f"Engine Size = {bikes[i][2]} cc, Milage = {bikes[i][3]}")
            print("Rent--")
            print(f"Daily = {bikes[i][4]}, weekly = {bikes[i][5]}, monthly = {bikes[i][6]}")
    print("")
    print(f"Total number of bikes available = {counter}.")
    try:
        if admin_username == 'rohit':
            admistrator_functions()
    except:
        customer_functions()

def customer_functions():
    print((""))
    print(("---------------------------------"))
    print(("Please Select form options below"))
    print((""))
    print(("1: View available bikes"))
    print(("2: Rent a bike"))
    print(("3: View rended bikes"))
    print(("4: Return a bike"))
    print(("5: Main Menu"))
    print(("6: Exit"))
    print((""))
    choice = int(input('Enter your choice: '))

    if choice == 1:
        view_bikes()
    elif choice == 2:
        rent_bike()
    elif choice == 3:
        view_rented_bike()
    elif choice == 4:
        return_rented_bike()
    elif choice == 5:
        starter()
    elif choice == 6:
        exit()
    else:
        print((""))
        print(("Invalid choice!! Please try again"))
        customer_functions()

def owner_bike_remove():
    print((""))
    print(("---------------------------------"))
    counter = 0
    for i in bikes_list:
        if bikes[i][0]==owner_username:
            counter+=1
            print(f"{counter}: {bikes[i][1]} and chassis number {i}")
        print("")
    choice = input('Enter the chassis number of bike to be removed: ').lower()
    print((""))
    print(f"{bikes[choice][1]} removed successfully")
    # print(bikes.pop(choice))
    # print(bikes)

    print((""))
    print(("---------------------------------"))
    owner_functions()

def view_bike_owner():
    print((""))
    print(("---------------------------------"))
    counter = 0
    for i in bikes_list:
        if bikes[i][0]==owner_username:
            counter+=1
            # print("")
            print(f"{counter}. {bikes[i][1]}")
    print((""))
    print(("---------------------------------"))
    owner_functions()
            
def add_bike():
    print((""))
    print(("---------------------------------"))
    print(("Please Enter following details: "))
    chassis_number = input('Please Enter chassis number: ')
    bike_name = input("Please enter your bike's name: " )
    engine_size = input('Please enter your engine size in cc: ')
    milage = input('Please enter milage : ')
    day_price = int(input('Please enter Daily rent amount in ₹: '))
    week_price = int(input('Please enter Weekly rent amount in ₹: '))
    month_price = int(input('Please enter Monthly rent amount in ₹: '))

    bikes[chassis_number] = [owner_username,bike_name,engine_size,milage,day_price,week_price,month_price]
    print("")
    print("Bike added successfully!")
    print((""))
    print(("---------------------------------"))
    print((""))
    owner_functions()
    
def owner_functions():
    print((""))
    print(("Please select from below options"))
    print((""))
    print(("1: Add a Bike"))
    print(("2: Remove a Bike"))
    print(("3: View added bikes"))
    print(("4: Main Menu"))
    print(("5: Exit"))
    print((""))
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_bike()
    elif choice == 2:
        owner_bike_remove()
    elif choice == 3:
        view_bike_owner()
    elif choice == 4:
        starter()
    elif choice == 5:
        exit()
    else:
        print((""))
        print("Invalid choice!! Please try again")
        owner_functions()

def administer():
    print(("Please Enter your details"))
    print((""))
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    global admin_username
    admin_username = username

    if username == admin[0] and password == admin[1]:
        print((""))
        print(("Login Successful"))
        print((""))
        admistrator_functions()
    else :
        print("")
        print(("Invalid credentials"))
        print(("Please try again"))
        starter()

def bike_owner_login():
    print((""))
    print(("---------------------------------"))
    print("Owner's Login")
    print("Please Enter Following Details")
    print((""))
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")

    global owner_username
    owner_username = username

    if username in owner_ids:
        if password == owner_details[username][0]:
            print((""))
            print(("Login Successful"))
            print((""))
            print(("--------------------------"))
            print(f"Welcome {owner_details[username][1]}")
            owner_functions()
        else:
            print("")
            print("Incorrect Password")
            print(("Please Try again"))
            bike_owner()
    else:
        print("")
        print("Incorrect Username")
        print(("Please Try again"))
        bike_owner()
     
def bike_owner_registration():
    print((""))
    print(("---------------------------------"))
    print("Owner's Registeration")
    print(("Please Enter Your Following Details"))
    name = input("Enter your name: ")
    name = name.title()
    user_id = input("Enter user ID: ")
    password = input("Enter password: ")

    if user_id in owner_ids:
        print("Username already exists")
        print(("Please Try Again"))
        print((""))
        print(("---------------------------------"))
        customer_registeration()
    else:
        license = input("Enter Your Licence Number: ")
        aadhaar = input("Enter Your Aadhar Card Number: ")
        owner_details[user_id]=[password,name,license,aadhaar]
        print((""))
        print("Registration Successful")
        print("Please Login to Proceed Forward")
        print((""))
        print("----------------------------------")
        bike_owner()

def bike_owner():

    print((""))
    print(("---------------------------------"))
    print(("Please Select form options below"))
    print((""))
    print("1: Login")
    print("2: Register")
    print("3: Main menu")
    print("4: Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        bike_owner_login()
    elif choice == 2:
        bike_owner_registration()
    elif choice == 3:
        starter()
    elif choice ==4:
        exit()
    else:
        print((""))
        print("Invalid choice Please try again !!!")
        bike_owner()


def exit():
    datasaver = [customer_details, owner_details, admin, bikes, bike_on_rent]
    saver = open("datasaver.p","wb")
    pickle.dump(datasaver,saver)
    saver.close()
    print((""))
    print(("---------------------------------"))
    print(("Thank You For using Bike Rental System"))
    print(("Have a Nice Day"))
    print((""))
    print((""))

def starter():
    print((""))
    print(("---------------------------------"))
    print(("Please Select"))
    print(("1: Admistrators's Portal"))
    print(("2: Bike Owner's Portal"))
    print(("3: Customer's Portal"))
    print(("4: Exit"))
    choice = int(input("Please Enter your choice: "))

    if choice == 1: 
        administer()
    elif choice == 2:
        bike_owner()
    elif choice == 3:
        customer()
    elif choice == 4:
        exit()
    else :
        print((""))
        print("Invalid choice!! Please try again")
        print((""))
        starter()

def customer():
    print((""))
    print(("---------------------------------"))
    print(("Please Select form options below"))
    print((""))
    print("1: Login")
    print("2: Register")
    print("3: Main menu")
    print("4: Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        customer_login()
    elif choice == 2:
        customer_registeration()
    elif choice == 3:
        starter()
    elif choice ==4:
        exit()
    else:
        print((""))
        print("Invalid choice Please try again !!!")
        customer()

def customer_registeration():
    print((""))
    print(("---------------------------------"))
    print("Customer's Registeration")
    print((""))
    print(("Please Enter Your Following Details"))
    print((""))
    name = input("Enter your name: ")
    name = name.title()
    user_id = input("Enter user ID: ")
    password = input("Enter password: ")

    if user_id in customer_ids:
        print("Username already exists")
        print(("Please Try Again"))
        customer_registeration()
    else:
        license = input("Enter Your Licence Number: ")
        aadhaar = input("Enter Your Aadhar Card Number: ")
        customer_details[user_id]=[password,name,license,aadhaar]
        print((""))
        print("Registration Successful")
        print("Please Login to Proceed Forward")
        print(("---------------------------------"))
        customer()        

def customer_login():
    print((""))
    print(("---------------------------------"))
    print("Customer's Login")
    print("Please Enter Following Details")
    print((""))
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    global customer_username
    customer_username = username
    if username in customer_ids:
        if password == customer_details[username][0]:
            print((""))
            print(("Login Successful"))
            print((""))
            print(f"Welcome {customer_details[username][1]}")
            print((""))
            customer_functions()
        else:
            print("")
            print("Incorrect Password")
            print(("Please Try again"))
            customer()
    else:
        print("")
        print("Incorrect Username")
        print(("Please Try again"))
        customer()

starter()







