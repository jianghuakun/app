import unittest
from unittest import mock

class SubClass(object):
    def add(self, a, b):
        "两个数相加"
        pass

class test_add(unittest.TestCase):
    "测试两个数相加用例,功能函数未开发完成，使用打桩写死"
    def test_add_1(self):
        # 创建一个mock对象 return_value代表mock一个数据
        list1={"key":"value"}
        mock_add=mock.Mock(return_value=list1)
        # 将mock对象赋予给被测函数
        add=mock_add
        # 调用被测函数
        result=add(8,8)
        # 断言实际结果和预期结果
        #self.assertEqual(result,15)
        with self.subTest(data="SubClass_add，2个数相加，相加的方法未实现"):
            self.assertEqual(result, 15, "点击footballsure Fail")



