#numpy->dataset create
#pandas->dataset represent
#matplotlib->graphically data display


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

years = np.array([2005,2006,2007,2011])
grade = np.array([54.5,71,69,76])
plt.plot(years,grade,marker = "o")
plt.title("My Academic Grades")
plt.xlabel("Year")
plt.ylabel("Grades")
plt.grid()
plt.show()

#PIE
x = np.array([90, 75, 80, 65])
plt.title("Title")
name = np.array(["Python", "Java","React", "C"])
plt.pie(x, labels=name, shadow=True)
plt.legend()
# plt.xticks(name)
plt.show()


#Bar graph
plt.bar(years,grade)
plt.title("bar graph")
plt.show()

#Scatter
plt.scatter(years,grade)
plt.grid()
plt.show()


    