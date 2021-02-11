import matplotlib.pyplot as plt
import numpy as np

problem_1_1 = np.loadtxt('HW4_problem1_1_data.txt', skiprows = 1)

xvalue = problem_1_1[:,0]
analytical_deriv = problem_1_1[:,1]
fw_diff = problem_1_1[:,2]
central_diff = problem_1_1[:,3]

plt.plot(analytical_deriv, label = 'Analytical Derivative', color = 'green')
plt.plot(fw_diff, label = 'Foward Difference', color = 'red')
plt.plot(central_diff, label = 'Central Difference', color = 'yellow')
plt.title('Derivative calculations for f(x) =  x**3 - 5*x + 2')
plt.xlabel('X value from -5 to 5; increments of 0.01')
plt.ylabel('Value of derivative functions')
plt.legend()
plt.show()
#using a very small value of h, we elimiate much of the error using a central difference differentiation (zooming in on the graph)
#shown on the graph, even with small values of h, there is still much error using the foward difference approach

