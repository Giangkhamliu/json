import json
p_obj={"name": "David", "class": "I", "age": 6
}
new=open("meraki2.json","w")
json.dump(p_obj,new,indent=4)
new.close()