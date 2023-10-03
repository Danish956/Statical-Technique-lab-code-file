from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

#Probility Functions
#PDF - Probablity Density Functions 
#CDF - Cumulative Distributions Functions

np.set_printoptions(precision=4)  #print  arrays to 4 decimal places

#Make a t distribution object for t with 20 degree of freedom
t_dist = stats.t(20)

#plot the PDF

t_values = np.linspace(-4, 4, 1000)
plt.plot(t_values, t_dist.pdf(t_values))
plt.xlabel("t_value")
plt.ylabel("Probalitiy for t value")
plt.title("PDF for t Distribution with df=20")
plt.show() 

#Plot the CDF
plt.plot(t_values, t_dist.cdf(t_values))
plt.xlabel("t_value")
plt.ylabel("Probalitiy for t value <=t")
plt.title("CDF for t Distribution with df=20")
plt.show()

#Moment Generta
data = [[3,5,7,9,34], 
[45,7,34,67,6], 
[4,8,6,3,7]]

print("")
print("Momemt Genertaing Functions")

print("2th moment =  ", stats.moment(data,moment=2))