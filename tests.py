import unittest
import requests


class TestFlaskModel(unittest.TestCase):

    def testing_demo(self):
        r = requests.post('http://127.0.0.1:5000/testing', json={"mydata": '1'})
        result = r.text
        flt_result = float(result)
        self.assertTrue(type(result) is str)
        self.assertTrue(type(flt_result) is float)


if __name__ == '__main__':
    unittest.main()