import matplotlib.pyplot as plt
import numpy as np
 
 
problem_2 = np.loadtxt('HW3_problem2_data.txt',skiprows = 1)

analytical_diff = problem_2[:,0] #pulls data from loaded txt
fwderror = problem_2[:,1]
centralerror = problem_2[:2]

plt.title('Derivative calculations for f(x) =  1m * sin(2pi*(0.02Hz)*t')
plt.plot(analytical_diff, label = 'Analytical Derivative', color = 'green')
plt.plot(fwderror, label = 'Foward Difference', color = 'red', linewidth = 0.5)
plt.plot(centralerror, label = 'Central Difference', color = 'blue')
plt.ylabel('Position of x (m)')
plt.xlabel('Time 0.01s')
plt.legend()
plt.show()