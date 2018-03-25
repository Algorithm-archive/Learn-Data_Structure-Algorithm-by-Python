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

        ob.pop()
        ob.pop()
        
        get_max = ob.getMax()
        self.assertEqual(ob.printHeap(), [8, 6, 3, 5], msg="Heap Element Should be [8,6,3,5]")
        self.assertEqual(get_max, 8, msg="Max Element is not matched")

if __name__ == '__main__':
    unittest.main()
