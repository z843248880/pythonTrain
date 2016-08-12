# Author:zhoujunlon
import sys
product = open("pro_list.txt", "r")
product_list = []
shopping_list = []
for line in product:
    line = line.strip()
    product_list.append(line)
pro_list_open = open("balance.txt")
salary = pro_list_open.readline()
pro_list_open.close()


def list_product():
    print("----------shopping list---------")
    sh_list = open("shop_list.txt")
    for p in sh_list:
        print(p)
    sh_list.close()
    print("--------------------------------")
    print("Your current balance is ", salary)
    sys.exit()
if salary:
    salary = int(salary)
else:
    while True:
        salary = input("Input your salary:")
        if salary.isdigit():
            pro_list_open = open("balance.txt", "w")
            pro_list_open.write(salary)
            pro_list_open.close()
            salary = int(salary)
            break
        else:
            print("Salary must be a number:")
while True:
    for index, item in enumerate(product_list):
        print(index, item)
    user_choice = input("Input the product number you want to buy:")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if 0 <= user_choice < len(product_list):
            p_item = product_list[user_choice]
            p_item_product = p_item.split(":")[0]
            p_item_price = p_item.split(":")[1]
            if int(p_item_price) <= salary:
                print("Your choice is {name}".format(name=p_item_product))
                f = open("shop_list.txt", "a+")
                f.write(p_item_product+"\n")
                f.close()
                salary -= int(p_item_price)
                print("Your current salary is \033[31;1m%s\033[0m" % salary)
                pro_list_open = open("balance.txt", "w")
                pro_list_open.write(str(salary))
                pro_list_open.close()
            else:
                if 400 > salary:
                    print("\033[31;1mPool, fuck off!!!\033[0m")
                    list_product()
                else:
                    print("Your current salary does not enough , choice other products!!")
        else:
            print("Invalid number!!!!!!!!")
    elif user_choice == "q":
        list_product()
    else:
        print("\033[31;1mMust input a  number!!!\033[0m")


