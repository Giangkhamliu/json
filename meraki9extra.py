import json
a={}
b={}
name_list=input("Enter the string:-")
num=int(input("Enter your no. of items: "))
for i in range(num):
    item_user=input("Enter the item: ")
    amount_item=int(input("Enter your number: "))
    a[item_user]=amount_item
b[name_list]=a
with open("shopping_list.json","w")as f:
    json.dump(b,f,indent=4)