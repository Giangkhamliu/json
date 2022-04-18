import json
filename ='filetojson.txt'
dict1 = {}
with open(filename) as f:
    for line in f:
        c, d = line.strip().split(None, 1)
        dict1[c] = d.strip()
out_file = open("test1.json", "w")
json.dump(dict1, out_file, indent = 4)
out_file.close()

