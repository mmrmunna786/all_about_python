# what is an "iterator"?
# ans: An object that can be iterated upon and returns data, one element at 
# a time when next() is called on it

# what is an "iterable"?
# ans: An object which will return an iterator when iter() is called on it

# example:
'''
menu = ["Margheritat", "Pepperoni", "Hawaiian"] # <= Iterable (the menu)

waiter = iter(menu) # <= Creates iterator (hires the waiter)

print(next(waiter))  # "Margherita" <= Waiter brings first pizza
print(next(waiter))  # "Pepperoni"  <= Waiter brings second pizza
print(next(waiter))  # "Hawaiian"   <= Waiter brings third pizza
print(next(waiter))  # StopIteration! <= Waiter says "no more pizzas"
'''

def my_for( iterable ):
    # define an iterator using iter()
    my_iter = iter( iterable )
    # print the items using the iterator object by calling next() on it
    while True:
        try:
            print( next( my_iter ) )
        # except StopIteration:
        except:
            print( "END OF ITERATION" )
            break
my_for( [1, 2, 3, 4] )
