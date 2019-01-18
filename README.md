# 简介
JSON / Model 转换模块，Python 版。

### 其他版本
* [PHP 版](https://github.com/fangqk1991/php-model)

### 依赖
* Python 3

### 安装
```
pip install git+https://github.com/fangqk1991/py-model.git
```

### 示例
`model-demo.py`

```
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
```

![](https://image.fangqk.com/2019-01-18/py-model-demo.jpg)
