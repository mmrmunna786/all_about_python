# this is misleading because below two print statements should print
# the name of the add function that is "add" and the docstring 
# " """Adds two numbers together.""" " but it doesn't print that 
# therefore we need functools library and "@wraps(fn)" as shown below
# ===================================================================
# def log_function_data( fn ):
#     # @wraps( fn )
#     def wrapper( *args, **kwargs ):
#         """I AM A WRAPPER"""
#         print( f"you are about to call {fn.__name__}" )
#         print( f"here's the documentation {fn.__doc__}" )
#         return fn( *args, **kwargs )
#     return wrapper

# @log_function_data
# def add( x, y ):
#     """Adds two numbers together."""
#     return x + y

# print( add.__name__ )
# print( add.__doc__ )
# help( add )
# ===================================================================
# from functools import wraps
# def log_function_data( fn ):
#     @wraps( fn )
#     def wrapper( *args, **kwargs ):
#         """I AM A WRAPPER"""
#         print( f"you are about to call {fn.__name__}" )
#         print( f"here's the documentation {fn.__doc__}" )
#         return fn( *args, **kwargs )
#     return wrapper

# @log_function_data
# def add( x, y ):
#     """Adds two numbers together."""
#     return x + y

# print( add.__name__ )
# print( add.__doc__ )
# help( add )
# ===================================================================
from time import time
from functools import wraps
# Let's define a speed_test decorator which will show the time it takes
# to sum million digits from 0 to 1 million
def speed_test( fn ):
    @wraps( fn )
    def wrapper( *args, **kwargs ):
        start_time = time()
        result = fn( *args, **kwargs )
        end_time = time()
        print( f"Executing {fn.__name__}" )
        print( f"Time elapsed: {round(((end_time - start_time) * 1000), 2)} ms" )   
        return result
    return wrapper
# seed testing of generators
@speed_test
def sum_nums_gen():
    return sum( x for x in range( 50_000_000 ) ) # generators
# seed testing of lists
@speed_test
def sum_nums_list():
    return sum( [ x for x in range( 50_000_000 ) ] ) # list comprehension

print( sum_nums_gen() )
print( sum_nums_list() )