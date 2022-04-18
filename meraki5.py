import json
def is_complex(obj):
    if 'complex' in obj:
        return complex(obj['real'], obj['img'])
    return obj

complex_object =json.loads('{"complex": true, "real": 4, "img": 5}', object_hook = is_complex)
simple_object =json.loads('{"real": 4, "img": 3}')
print("Complex_object: ",complex_object)
print("Without complex object: ",simple_object)