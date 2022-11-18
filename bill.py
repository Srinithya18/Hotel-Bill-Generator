import random
import csv

menuList = []
'''
Extracting input from the Menu.csv file
'''
with open("Menu.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        menuList.append(dict(row))
print("**************************  MENU  *************************")
print("Item No. \t Half Plate \t\t Full Plate")
for i in menuList:
    print('{:^12}  {:^20}  {:^20}'.format(
        i["Item no"], i["Half Plate"], i["Full Plate"]))


'''
Taking input for order
order_list stores the details of the items ordered
'''
order_list, total_bill = {}, 0
while(True):
    item_number = int(input("Enter Item Number: "))
    '''
    each order_list (key:value) contains
    items_id: [fullplates,fullplatesTotalprice, halfplates, halfplatesTotalPrice]
    
    '''
    order_list[item_number] = order_list.get(item_number, [0, 0, 0, 0])
    full_plates = int(input("Enter Number Of Full Plates required: "))

    half_plates = int(input("Enter Number Of Half Plates required: "))

    order_list[item_number][0] += (full_plates)
    order_list[item_number][2] += (half_plates)
    full_plate_item_cost = (
        full_plates*(eval(menuList[item_number-1]["Full Plate"])))
    half_plate_item_cost = (
        half_plates*(eval(menuList[item_number-1]["Half Plate"])))
    order_list[item_number][1] += full_plate_item_cost
    order_list[item_number][3] += half_plate_item_cost
    total_bill += (full_plate_item_cost+half_plate_item_cost)
    loop_input = input(
        "Do you want to continue?? Press y for YES | n for NO : ")
    if loop_input == "n":
        break

''' Taking input for tip '''
print("Enter tip Percentage:\n1. 0%\n2. 10%\n3. 20%")
tip_percentage = 0
tip_input = int(input())
if(tip_input == 2):
    tip_percentage = 10
elif(tip_input == 3):
    tip_percentage = 20


''' Updating total bill with the tip '''
total_bill_without_tip = total_bill
total_bill += (total_bill*(tip_percentage))/100
print("Bill to be paid including tip of {:.2f}% is: {:.2f}".format(tip_percentage,total_bill))

''' Taking input for number of shares and printing each share '''
shares = int(input("How many people plan to split the bill: "))
print("Each person share :%.2f" % (total_bill/shares))

""" Code section for test your luck """
print("\n\n*********** Test your luck ***********\nPress y for YES | n for NO :")
luck_input = input()

''' Pattern 1 -- Sad Face'''


def print_sad(n):
    print(' '+"*"*n+" ")
    for i in range(n):
        print("*"+" "*n+"*")
    print(' '+"*"*n+" ")


''' Pattern 2 -- Happy Face'''

def print_happy():
    print(" "+"*"*4+" "*12+"*"*4)
    for i in range(3):
        print("|"+" "*4+"|"+" "*10+"|"+" "*4+"|")
    print(" "+"*"*4+" "*12+"*"*4)
    print("\n{:^22}\n".format('{}'))
    print("{:^22}".format('______________'))

discount_value = 0

def test_your_luck():
    '''
    TEST_YOUR_LUCK 
    Random assignment of discount percentage 
    '''
    global discount_value
    discount_percentage = 0
    random_number = random.randint(1, 100)
    """
    5%  chance for 50% discount
    10% chance for 25% discount
    15% chance for 10% discount
    20% chance for no discount
    50% chance for increases by 20%

    """
    if random_number in range(1, 6):
        discount_percentage = -50
    elif random_number in range(6, 21):
        discount_percentage = -10
    elif random_number in range(21, 41):
        discount_percentage = 0
    elif random_number in range(41, 51):
        discount_percentage = -25
    else:
        discount_percentage = 20
    discount_value=(total_bill*discount_percentage)/100
    if discount_percentage < 0:
        print("Congratulations!! You got a discount {}".format((discount_value)))
        print_happy()
    else:
        print("Bad day!! You got an increment on bill of  {}".format((discount_value)))
        print_sad(4)
    



if(luck_input == "y"):
    test_your_luck()


print("\n\n*************** Total bill breakdown ***************")
for key, value in order_list.items():
    """ If any full plate exists in the order_list with key """
    if(value[0]):
        print("Item {} [Full] [{}] : {:.2f}".format(key, value[0], value[1]))
    """ If any half plate exists in the order_list with key """
    if(value[2]):
        print("Item {} [Half] [{}] : {:.2f}".format(key, value[2], value[3]))

print("Total: %.2f" % round(total_bill_without_tip, 2))
print("Tip Percentage: %.2f" % round(tip_percentage, 2))

print("Discount/Increase: %.2f" % round(discount_value, 2))
total_bill = total_bill+(discount_value)
print("Final Total: %.2f" % round(total_bill, 2))
print("Updated share that each person has to contribute: %.2f" %
      round(total_bill/shares, 2))
