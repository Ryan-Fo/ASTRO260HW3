import matplotlib.pyplot as plt
import numpy as np

problem1_error = np.loadtxt('HW4_problem1_error_data.txt', skiprows = 1)

xvalue = problem1_error[:,0]
fwderror = problem1_error[:,1]
centralerror = problem1_error[:,2]

plt.plot(fwderror, label = 'Foward Error',color = 'red')
plt.plot(centralerror, label = 'Central Error',color = 'blue')
plt.title('Error Values Between Central and Foward Difference from Analytical Values')
plt.xlabel('X value from -5 to 5; increments of 0.01')
plt.ylabel('Error values computed using relative error equation')
plt.yscale('log')
plt.legend()
plt.show()

#a much less extreme error graph is seen between the fwd difference and central difference methods. Meaning less deviation from real values.