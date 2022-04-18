# Apki Dictionary ka use kar ke ek json file create karna hai.
# and you have to do some task like
# 1.I want to see the shopping list in json file.
# 2.Then I ask the user which item I want to buy.
# 3.After that the user will give the name then ask the user to input such as 
# how many items do you want.
# 4.Then you have to remove that number item from json file.
# 5.If you want to add shopping items you have to insert json file main.

import json
dic={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
with open("meraki9.json","w") as f:
    json.dump(dic,f,indent=6)

# dic={
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }
# for i in dic:
#     for j in dic[i]:
#         a=dic[i][j]
#         print(a)