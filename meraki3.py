# Q.3 Python object ko json string mai convert karne ka program likho?
import json
p={"Name":"Grace","Age":23,"Sex":"Female","Education":"Graduate"}
a= json.dumps(p,indent=4)
print(a)
print(type(a))