# Author: Munna
# Date: 11/06/2026
"""
Unit testing
===================================================
When you write a function or a class, you can also write tests for that code. Testing proves that your 
code works as it’s supposed to in response to all the input types it’s designed to receive.

=> Python comes with a built-in module called "unittest"
=> You can write unit tests encapsulated as classes that inherit from unittest.TestCase
=> This inheritance gives you access to many assertion helpers that let you test the behavior of your
    functions
    
Example: 
consider the file activities.py to test:

def eat( food, is_healthy ):
    pass
    
def nap( num_hours ):
    pass
    
consider the file test.py to test activities.py:
import unittest
from activities import eat,nap

class ActivityTests( unittest.TestCase ):
    pass
if __name__ == "__main__":
    unittest.main()
    
Table 11-1: Assert Methods Available from the unittest Module
-------------------------------------------------------------
Method                              Use
-------------------------------------------------------------
assertEqual(a, b)                   Verify that a == b
assertNotEqual(a, b)                Verify that a != b
assertTrue(x)                       Verify that x is True
assertFalse(x)                      Verify that x is False
assertIn(item, list)                Verify that item is in list
assertNotIn(item, list)             Verify that item is not in list
-------------------------------------------------------------
"""
import unittest
from activities import eat, nap

class ActivityTests( unittest.TestCase ):
    # to test the function "eat" for "equality" def a function to test 
    # for equality between a and b
    def test_eat_healthy( self ):
        self.assertEqual( eat( "broccoli", is_healthy=True ),
                         "I'm eating broccoli, because my body is a temple"
                         )
    # this will not pass because the return value a = "pass" = None is not equal to 
    # "I'm eating broccoli, because my body is a temple"
    def test_eat_unhealthy( self ):    
        self.assertEqual( eat( "pizza", is_healthy=False ),
                         "I'm eating pizza, because YOLO!"
                         )
    # this will not pass because the return value a = "pass" = None is not equal to 
    # "I'm eating pizza, because YOLO!"
    def test_short_nap( self ):
        self.assertEqual( nap( 1 ), 
                         "I'm feeling refreshed after 1 hour of nap" 
                         )
    # this will not pass because the return value a = "pass" = None is not equal to 
    # "I'm feeling refreshed after 1 hour of nap"
    def test_long_nap( self ):
        self.assertEqual( nap( 3 ), 
                         "Ugh I overslept. I didn't mean to nap for 3 hours" 
                         )
    # this will not pass because the return value a = "pass" = None is not equal to 
    # "Ugh I overslept. I din't mean to nap for 3 hours"
if __name__ == "__main__":
    unittest.main()
