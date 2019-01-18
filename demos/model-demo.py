from demos.ModelMainEx import ModelMainEx

data = {
    'xyy': 1,
    'xxx_yyy': 'hehehe',
    'xxx': 'ttt',
    'sub_obj': {'name': 'Sub - Obj'},
    'sub_items': [
        {'name': 'Sub - Obj - 1'},
        {'name': 'Sub - Obj - 2'},
        {'name': 'Sub - Obj - 3'},
    ]
}

obj = ModelMainEx()
obj.fc_generate(data)

print(obj)
print(obj.fc_encode())
