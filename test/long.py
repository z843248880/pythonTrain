import sys
product = open("pro_list.txt", "r")
product_list = []
shopping_list = []
for line in product:
    line = line.strip()
    product_list.append(line)
print(product_list)
pro_list_open = open("balance.txt", "r+")
salary = pro_list_open.readline()
if salary:
    salary = int(salary)
else:
    while True:
        salary = input("Input your salary:")
        if salary.isdigit():
            salary = int(salary)
            pro_list_open.write(str(salary))
            pro_list_open.close()
            break
        else:
            print("Salary must be a number:")
    print(">>>>>>>")

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
                shopping_list.append(p_item_product)
                salary -= int(p_item_price)
                print("Your current salary is \033[31;1m%s\033[0m" % salary)
                pro_list_open.write(str(salary))
            else:
                print("\033[31;1mPool, fuck off!!!\033[0m")
                sys.exit()
        else:
            print("Invalid number!!!!!!!!")
    elif user_choice == "q":
        print("----------shopping list---------")
        for p in shopping_list:
            print(p)
            print("--------------------------------")
            print("Your current balance is ", salary)
        sys.exit()
    else:
        print("\033[31;1mMust input a  number!!!\033[0m")
        

