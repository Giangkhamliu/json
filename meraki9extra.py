import json
a={}
num=int(input("enter your items number: "))
for i in range(num):
    item_user=input("enter your item: ")
    amount_item=int(input("enter your number: "))
    a[item_user]=amount_item
with open("shopping_list.json","w")as f:
    json.dump(a,f,indent=4)