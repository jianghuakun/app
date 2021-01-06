import unittest
from unittest import mock
class subclass():
    def add(self,a,b):
        "2个数相加"
        return a+b
class test_sub(unittest.TestCase):
    "测试2个数相机，功能已经实现"
    def test_add(self):
        "初始化被测函数类实例"
        sub=subclass()
        #创建一个mock对象，返回默认值return_value
        #传递side_effect关键字参数, 会覆盖return_value参数值, 使用真实的add方法测试
        sub.add=mock.Mock(return_value=15,side_effect=sub.add)
        #调用被测函数
        result=sub.add(5,5)
        # 断言实际结果和预期结果
        with self.subTest(data="2个数相加，相加的方法已经实现"):
            self.assertEqual(result, 15, "点击footballsure Fail")

