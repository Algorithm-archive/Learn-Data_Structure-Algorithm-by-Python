import unittest
from heap import MaxHeap

class MaxHeapTestCase(unittest.TestCase):
    """ Test for Heap.py"""
    def test(self):
        # test data
        ob = MaxHeap()
        ob.insert(10)
        self.assertEqual(ob.peek(), 10, msg="Max Element is not matched")
        ob.insert(5)
        self.assertEqual(ob.peek(), 10, msg="Max Element is not matched")
        ob.insert(6)
        self.assertEqual(ob.peek(), 10, msg="Max Element is not matched")
        ob.insert(3)
        self.assertEqual(ob.peek(), 10, msg="Max Element is not matched")
        ob.insert(8)
        self.assertEqual(ob.peek(), 10, msg="Max Element is not matched")
        ob.insert(20)
        self.assertEqual(ob.peek(), 20, msg="Max Element is not matched")
        ob.pop()
        self.assertEqual(ob.peek(), 10, msg="Max Element is not matched")
        ob.pop()
        self.assertEqual(ob.peek(), 8, msg="Max Element is not matched")
        ob.pop()
        self.assertEqual(ob.peek(), 6, msg="Max Element is not matched")
        ob.pop()
        self.assertEqual(ob.peek(), 5, msg="Max Element is not matched")
        ob.pop()
        self.assertEqual(ob.peek(), 3, msg="Max Element is not matched")
        ob.pop()
        self.assertEqual(ob.peek(), None, msg="Max Element is not matched")

if __name__ == '__main__':
    unittest.main()
