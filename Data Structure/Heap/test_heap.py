import unittest
from heap import MaxHeap

class MaxHeapTestCase(unittest.TestCase):
    """ Test for Heap.py"""
    def test(self):
        # test data 
        ob = MaxHeap()
        ob.insert(10)
        ob.insert(5)
        ob.insert(6)
        ob.insert(3)
        ob.insert(8)
        ob.insert(20)
        self.assertEqual(ob.peek(), 20, msg="Max Element is not matched")
        ob.pop()
        ob.pop()
        self.assertEqual(ob.peek(), 8, msg="Max Element is not matched")
        ob.pop()
        self.assertEqual(ob.peek(), 6, msg="Max Element is not matched")
        ob.pop()
        ob.pop()
        ob.pop()
        self.assertEqual(ob.peek(), False, msg="Max Element is not matched")

if __name__ == '__main__':
    unittest.main()


