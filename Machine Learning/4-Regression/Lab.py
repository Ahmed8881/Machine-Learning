import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('./deeplearning.mplstyle')
#----------------------------------------------------------Add Lab for regression
# x_train is the input variable (size in 1000 square feet)
# y_train is the target (price in 1000s of dollars)
x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
print(f"x_train: {x_train}")
print(f"y_train: {y_train}")
#You will use m to denote the number of training examples. Numpy arrays have a .shape parameter. x_train.shape returns a python tuple with an entry for each dimension. x_train.shape[0] is the length of the array and number of examples as shown below.
# m is the number of training examples
print(f"x_train.shape: {x_train.shape}")#return a tuple
m=x_train.shape[0]
print(f"m: {m}") #return the number of training examples
mn=len(x_train)
print(f"mn: {mn}") #return the number of training examples
#To access a value in a Numpy array, one indexes the array with the desired offset. For example the syntax to access location zero of x_train is x_train[0]. Run the next code block below to get the  𝑖𝑡ℎ training example.
i=0
x_i=x_train[i]
y_i=y_train[i]  
print(f"x^{i}, y^{i}: ({x_i}, {y_i})") #return the first training example
  
#Plotting the data You can plot these two points using the scatter() function in the matplotlib library, as shown in the cell below.The function arguments marker and c show the points as red crosses (the default is blue dots).You can use other functions in the matplotlib library to set the title and labels to display
#plot the data points
plt.scatter(x_train,y_train,marker='x',c='r')
#set the title



