
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as m

"""* Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives."""

arr = np.array([np.zeros(10),np.ones(10),np.ones(10)*5],dtype=int)
print(arr)

"""* Write a NumPy program to find the number of rows and columns of a given matrix."""

s = arr.shape
print(s)

"""* Write a Pandas program to replace all the NaN values with Zero's in a column of a dataframe.
(Use IMDB-Movie-Data file)
"""

# data collection
!cd sample_data
!wget https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv

#reading the data
data = pd.read_csv("IMDB-Movie-Data.csv")
data.head(5)

data.info()

data.isnull().sum()

#filling NaN values
data.fillna(0,inplace=True)
data.isnull().sum()

"""* Write a Pandas program to get those movies whose revenue more than 100 million in IMDB-
Movie-Data file.
"""

money = data['Revenue (Millions)']
more100 = data[money>=100.00]
more100

"""* Write a Python program to plot two lines with legends, different widths, colors and style."""

#two functions writen
t = np.linspace(0,100,1000)
x = np.exp(-0.5*t)
y = np.sin(2*m.pi*0.02*t)

#plotting
plt.plot(t,x,'g',t,y,'k--',linewidth=1)
plt.legend(['exponential function','sine function'], loc = 'lower right')
plt.xlabel("Time axis")
plt.ylabel("Amplitude axis")
plt.title("sample function plots")

"""* Write a Python program to display a bar chart of the popularity of programming Languages."""

# data entry
lan = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'] #PHP Sucks!!! it should be banned
pop = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

#plotting.
plt.bar(lan,pop,color = ("g","b","r","m","c","y"), edgecolor = "k")
plt.title("popularity chart")
plt.xlabel("Programming langauge")
plt.ylabel("Users in millions")
