# Author:zhoujunlon
import sys
import time
time_format = '%Y-%m-%d %X'
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
    print("Your current balance is \033[31;1m{sal}\033[0m".format(sal=salary))
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
        print(index+1, item)
    print("Your balance is \033[31;1m{sal}\033[0m".format(sal=salary))
    user_choice = input("Input the product number you want to buy or enter 'L' show your cart:")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if 0 < user_choice <= len(product_list):
            p_item = product_list[user_choice-1]
            shopping_list.append(p_item)
    elif user_choice == "L":
        while True:
            for index2, item2 in enumerate(shopping_list):
                print(index2+1, item2)
            user_choice2 = input(
                "Enter '\033[31;1mB\033[;0m' add new product ,enter '\033[31;1mok\033[;0m'buy all products or enter product number remove product!!!")
            if user_choice2.isdigit():
                user_choice2 = int(user_choice2)
                if 1 <= user_choice2 <= len(shopping_list):
                    del shopping_list[user_choice2-1]
                else:
                    print("Invalid number")
            elif user_choice2 == "B":
                break
            elif user_choice2 == "ok":
                u = 0
                for i in shopping_list:
                    u += int(i.split(":")[1])
                if u <= salary:
                    f = open("shop_list.txt", "a+")
                    for j in shopping_list:
                        f.write(j.split(":")[0] + "<BUY TIME>" + time.strftime(time_format, time.localtime()) + "\n")
                    f.close()
                    salary -= u
                    print("Your current balance is \033[31;1m%s\033[0m" % salary)
                    pro_list_open = open("balance.txt", "w")
                    pro_list_open.write(str(salary))
                    pro_list_open.close()
                    shopping_list = []
                    break
                else:
                    print("Balance not enough,remove one or more product!!!")
            else:
                print("Invalid Input!!!!!")
    elif user_choice == "q":
        list_product()
    else:
        print("\033[31;1mMust input a  number!!!\033[0m")


