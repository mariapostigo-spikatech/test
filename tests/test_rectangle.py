# Unittest (no need to create a new environment)

from src.rectangle import Rectangle

# import unittest
# class TestGetAreaRectangle(unittest.TestCase):
#     def runTest(self):
#         rectangle = Rectangle(2, 3)
#         self.assertEqual(rectangle.get_area(), 6)

# if __name__ == '__main__':
#     unittest.main()

# pytest need to install pytest

import pytest
class TestGetAreaRectangle():

    @classmethod
    def setup_class(cls):
        cls.rectangle = Rectangle(2, 3)

    @classmethod
    def teardown_class(cls):
        del cls.rectangle

    def test_correct_area(self):
        assert self.rectangle.get_area() == 6
    
    def test_incorrect_area(self):
        self.rectangle.set_width(None)
        with pytest.raises(TypeError):
            self.rectangle.get_area()

# from testify import *

# class TestGetAreaRectangle(TestCase):

#     @class_setup
#     def init_the_variable(self):
#         self.rectangle = Rectangle(2, 3)

#     # @setup
#     # def increment_the_variable(self):
#     #     self.variable += 1

#     def test_the_variable(self):
#         assert_equal(self.rectangle.get_area(), 6)

#     # @suite('disabled', reason='ticket #123, not equal to 2 places')
#     # def test_broken(self):
#     #     # raises 'AssertionError: 1 !~= 1.01'
#     #     assert_almost_equal(1, 1.01, threshold=2)

#     # @teardown
#     # def decrement_the_variable(self):
#     #     self.variable -= 1

#     @class_teardown
#     def get_rid_of_the_variable(self):
#         self.rectangle = None

# if __name__ == "__main__":
#     run()