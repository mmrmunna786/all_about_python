import matplotlib.pyplot as plt # importing the library and naming it as plt

# squares = [ squares**2 for squares in range( 1, 5+1 ) ] # creating a squares of numbers from 1-5 using list comprehension
# input_values = [ vals for vals in range( 1, 5+1 ) ]

# print( squares )

# plt.figure()
# plt.style.use('Solarize_Light2') # pre-defined style, can be accessed using terminal command: plt.style.available
# plt.plot( input_values, squares )
# plt.axis('tight')
# plt.title("Squares of numbers 1-5")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend(["Squares"])
# plt.show()

# Plotting and Styling Individual Points with scatter()

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# set chart title and label axes.
ax.set_title( "Square Numbers", fontsize=24 ) 
ax.set_xlabel( "Value", fontsize=14 )
ax.set_ylabel( "Square of Value", fontsize=14 )

# set size of tick labels
ax.tick_params( labelsize=14 )

plt.show()

# Plotting a Series of Points with scatter()
# To plot a series of points, we can pass scatter() separate lists of x- and y-values, like this:

x_values = [ vals for vals in range( 1, 5+1 ) ]
y_values = [ vals**2 for vals in range( 1, len(x_values)+1 ) ]

print( x_values,"\n",y_values )

plt.style.use( "seaborn-v0_8" )
fig, ax = plt.subplots()
ax.scatter( x_values, y_values, s=100 ) 
plt.show()
