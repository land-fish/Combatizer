import pymc
import math
import random

# A set of methods that return a perturber utility vector subject to parameters given to the constructor. Helper
# methods are prefixed with "h_".

# Usage
# Perturber(utilities, comparitor, threshold).perturbing_method()
# Example
#  import Perturber
#  perturbed_utilities = Perturber([-1, -0.5, 0, 0.5, 1], some_comparitor, 0.5).normal()
class Perturber:
    # Arguments
    #  utilities: A vector of floats with values in [-1,1]. Each element in the vector represents the utility of a
    #   single world.
    #  comparitor: A function that takes two utility vectors and outputs a value in [-1,1]. The output represents
    #   the similarity between the two inputs.
    #  threshold: A value between [-1,1]. Represents the minimum similarity (according to "comparitor") that a
    #   perturbed utility vector should have to the "utilities" parameter.
    def __init__(s, utilities, comparitor, threshold):
        # Validate input. Save them into the object if they're valid.
        print utilities, type(utilities)
        if type(utilities) != list:
            raise StandardError(s.h_log('Utilities parameter is not a list'))
        for utility in utilities:
            if not s.h_utilities_within_range(utilities):
                raise StandardError(s.h_log('Given utilities must all be in the interval [-1,1]'))
        s.utilities = utilities
        
        s.comparitor = comparitor
        
        if type(threshold) != float:
            if type(threshold) == int:
                threshold = float(threshold)
            else:
                raise StandardError('Given threshold must be an int nor a float')
        if threshold < -1 or threshold > 1:
            raise StandardError(s.h_log('Given threshold must be within the interval [-1,1]'))
        s.threshold = threshold
    
    # Perturb by adding normally-distributed noise
    def normal(s):
        cur_var = 1.0

        while True:
            result = []
            for utility in s.utilities:
                while True:
                    cur_result = utility + pymc.rnormal(0, 1/cur_var)
                    if s.h_utilities_within_range([cur_result]):
                        break
                result.append(cur_result)
            if comparitor(s.utilities, result) >= s.threshold:
                break
            cur_var /= 2
            
            # DEBUG
            print 'cur_var: ' + str(cur_var)
            print 's.utilities: ' + str(s.utilities)
            print 'result: ' + str(result)
            print 'similarity: ' + str(comparitor(s.utilities, result))
            print
        
        return result
   
    # Removes top 10% of utility values and replaces them with random values 
    def remove_max(s):
        remove_percent = .1
          #replace_num is the number of elements in the list to be changed
        replace_num = int(math.ceil(len(s.utilities) * remove_percent)) 
        top_percent_index = sorted(range(len(s.utilities)), key=lambda i: s.utilities[i], reverse=True)[:replace_num] 
        
        #Replace top values with random values between -1 and 1
        while True:
            result = s.utilities
            for aa in top_percent_index:
                result[aa] = random.random() * 2 - 1 
            if comparitor(s.utilities, result) >= s.threshold:
                break

        return result      

    def h_log(s, logtext):
        return '%s: %s' % (s.__class__.__name__, logtext)
    
    def h_utilities_within_range(s, utilities):
        for utility in utilities:
            if utility < -1 or utility > 1:
                return False
        return True


if __name__ == '__main__':
    comparitor = lambda x,y: 1 - sum([abs(x[i] - y[i]) for i in range(len(x))])/float(len(x))
    p = Perturber([random.random() * 2 -1 for i in range(100)], comparitor, 0.9)
    p.normal()
    p.remove_max()
