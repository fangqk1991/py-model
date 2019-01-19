# 简介
JSON / Model 转换模块，Python 版。

支持基本类型、Model、List[Model] 对象递归转换。

### 其他版本
* [PHP 版](https://github.com/fangqk1991/php-model)

### 依赖
* Python 3

### 安装
```
pip install git+https://github.com/fangqk1991/py-model.git
```

### 使用
1. Model 类继承于 `FCModel`
2. 实现 `fc_property_mapper` 方法，返回 (propName => jsonKey) 的映射字典
3. 如成员需解析为 `FCModel` 类型，实现 `fc_property_class_mapper` 并声明
4. 如成员需解析为 `List[FCModel]` 类型，实现 `fc_array_item_class_mapper` 并声明

### 示例
[Demo](https://github.com/fangqk1991/py-model/tree/master/demos)

```
# 简单对象实现
class ModelSubEx(FCModel):
    name = None
    def fc_property_mapper(self):
        return {
            'name': 'name',
        }

```

```
# 复杂对象实现
class ModelMainEx(FCModel):

    # xxx is not in fc_property_mapper
    xxx = None

    xyy = None
    xxxYYY = None
    subObj = None
    subItems = None

    def fc_property_mapper(self):
        return {
            'xyy': 'xyy',
            'xxxYYY': 'xxx_yyy',
            'subObj': 'sub_obj',
            'subItems': 'sub_items',
        }

    def fc_property_class_mapper(self):
        return {
            'subObj': ModelSubEx,
        }

    def fc_array_item_class_mapper(self):
        return {
            'subItems': ModelSubEx,
        }
```

```
# model-demo

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
