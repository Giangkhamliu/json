# Q4.Python dictionary(sort by key) object ko json data ::mai convert 
# karne ka program likho?
import json
p_obj={'4': 5,'6': 7,'1': 3,'2': 4}
a=json.dumps(p_obj,indent=4,sort_keys=True)
print(a)