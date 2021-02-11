"""Problem 1 in Homework set 3 for ASTR260"""


import numpy as np


def f(x):
    """function to test in our derivative
    program"""
    return x**3 - 5*x + 2

def analytic_deriv_f(x):
    """The analytic derivative of
     x**3 - 5*x + 2."""
    value = (3 * x**2) - 5
    return value

def absolute_error(truth, computed):
    """returns the absolute error between
    the computed and true value"""
    value = (np.abs(truth - computed)/np.abs(truth))
    return value

def relative_error(truth, computed):
    """returns the relative error between
    the computed and true value"""
    value = ((truth - computed)/truth)
    return value

def forward_difference(x, h, func=None):
    """Computes the numerical derivative
    of an arbitrary function using the forward
    difference method.
    x: point at which to evaluate the func
    h: stepsize to compute the secant
    func: a valid python function"""
    numerator = func(x+h)-func(x)            
    denominator = h
    return numerator/denominator

def central_difference(x, h, func=None):
    """Computes the numerical derivative
    of an arbitrary function using the central
    difference method.
    x: point at which to evaluate the func
    h: stepsize to compute the secant
    func: a valid python function"""
    numerator = func(x+h)-func(x-h)
    denominator = (2 * h)
    return numerator/denominator
    
def g(x):
    """Function to be tested for harmonic oscillator problem"""
    return 1 * np.sin(2 * np.pi*(0.02)*x)

def analytical_deriv_g(x):
    """True derivative to be testing against"""
    return (2*np.pi*0.02) * (np.cos(2*np.pi*(0.02)*x))

if __name__ == "__main__":
    print('\n')
    print("The central difference of x**3 - 5*x + 2,"+
          " evaluated at 0, with stepsize 0.01, is:")
    print(str(central_difference(0, 0.01, f)))

    print("Generating data for part 1 of problem 1")
    #Data for part 1, over the range -5-->5
    output_data_fullrange = []
    error_data = []
    h = 0.01
    #loop over an array from -5 to 5  in steps of 0.01
    for x_val in np.arange(-5, 5.01, h):
    
        #calculate analytic derivative, fw diff, and central diff
        analytic_diff = analytic_deriv_f(x_val)
        fw_diff = forward_difference(x_val, h, f)
        central_diff = central_difference(x_val, h, f)
        #store this as a tuple
        data = (x_val, analytic_diff, \
                fw_diff, central_diff)
        #append this to a list
        output_data_fullrange.append(data)
        
        #error tracking for relative difference
        
        fowarderror = relative_error(analytic_diff , fw_diff)
        centralerror = relative_error(analytic_diff, central_diff)
        error_values = (x_val, fowarderror,centralerror)
        
        error_data.append(error_values)
    #save this as an output textfile for plotting
    fname_part1 = 'HW3_problem1_1_data.txt'
    np.savetxt(fname_part1, #filename
               np.array(output_data_fullrange), #data to save
               delimiter=' ', #how to separate values in the file
               header=("function: x**3-5x+3\n"+
               "x, analytic_deriv(x), fw_diff(x), central_diff(x)"),
               fmt = '%.05f')#<--5 digits of precision, look up "format codes"
    print("Saved data to: "+fname_part1+"\n\n")
    
    #saves file for error part of question 1
    print("Generating data for part 2 of problem 1")
    fname_part1_error = 'HW3_problem1_error_data.txt'
    np.savetxt(fname_part1_error, #filename
               np.array(error_data),
               delimiter=' ',
               header = ("function: x**3-5x+3\n"+
               "x, fowarderror(x), centralerror(x)"),
               fmt = '%.05f')
    print("Saved data to: "+fname_part1_error+"\n\n")

    print("Generating data for problem 2")
    
    problem_2_time = np.genfromtxt('C:/Users/Rfole/Desktop/PythonFiles/sensor_position_data.txt',delimiter=',', skip_header = 1, dtype = float, usecols = 0)
    problem_2_position = np.genfromtxt('C:/Users/Rfole/Desktop/PythonFiles/sensor_position_data.txt',delimiter=',', skip_header = 1,dtype = float, usecols = 1)
    prob2 = []
    h = 0.01
    for x in problem_2_position:
        adiffq2 = analytical_deriv_g(x)
        
    for x in problem_2_time:
        cdiffq2 = central_difference(x,h,f)
        fdiffq2 = forward_difference(x,h,f)
        q2data = (adiffq2,fdiffq2,cdiffq2)
        prob2.append(q2data)
        
    fname_part2 = 'HW3_problem2_data.txt'
    np.savetxt(fname_part2,
        np.array(prob2),
        delimiter = ' ',
        header = ("function: 1 meter * sin(2*pi*(0.02)*t\n"+
        "analytic_deriv(x), fw_diff(x), central_diff(x),"),
        fmt = '%.05f')
    print("Saved data to: "+fname_part2+"\n\n")
    
    
