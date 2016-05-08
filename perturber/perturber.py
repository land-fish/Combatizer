import numpy
import random
import math

# A set of methods that return a perturber utility vector subject to parameters given to the constructor.

# Usage
#  Perturber(utilities, comparitor, threshold).perturbing_method()
# Example
#  import Perturber, random
#  perturbers = Perturber([-0.5, -1, 0.5, 1, 0], some_comparitor, 0.5).get_perturbers()
#  result = random.choice(perturbers)
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
        if type(utilities) != list:
            raise StandardError(s.log('Utilities parameter is not a list'))
        for utility in utilities:
            if not s.utilities_within_range(utilities):
                raise StandardError(s.log('Given utilities must all be in the interval [-1,1]'))
        s.utilities = utilities
        
        s.comparitor = comparitor
        
        if type(threshold) != float:
            if type(threshold) == int:
                threshold = float(threshold)
            else:
                raise StandardError('Given threshold must be an int or a float')
        if threshold < -1 or threshold > 1:
            raise StandardError(s.log('Given threshold must be within the interval [-1,1]'))
        s.threshold = threshold
    
    # Perturb by adding normally-distributed noise
    def normal(s):
        cur_var = 1.0
        
        while True:
            result = []
            for utility in s.utilities:
                while True:
                    cur_result = utility + numpy.random.randn() * math.sqrt(cur_var)
                    if s.utilities_within_range([cur_result]):
                        break
                result.append(cur_result)
            if s.comparitor(s.utilities, result) >= s.threshold:
                break
            cur_var /= 2
            
        return result
    
    # Perturb by randomly swapping 2 utilities
    def random_swap(s):
        found_result = False
        for i in range(100):
            indexes = range(len(s.utilities))
            c1 = random.choice(indexes)
            indexes.remove(c1)
            c2 = random.choice(indexes)
            
            result = s.utilities[:]
            result[c1], result[c2] = result[c2], result[c1]
            
            if s.comparitor(s.utilities, result) >= s.threshold:
                found_result = True
                break
            
        if found_result:
            return result
        else:
            return s.utilities
    
    # Return list of perturbers
    def get_perturbers(s):
        return [s.normal, s.random_swap]
    
    # Log output
    def log(s, logtext):
        return '%s: %s' % (s.__class__.__name__, logtext)
    
    # True if all utilities in a vector are in the interval, else false
    def utilities_within_range(s, utilities):
        for utility in utilities:
            if utility < -1 or utility > 1:
                return False
        return True


if __name__ == '__main__':
    comparitor = lambda x,y: 1 - sum([abs(x[i] - y[i]) for i in range(len(x))])/float(len(x))
    p = Perturber([i/10. for i in range(10)], comparitor, 0.999)
    print p.get_perturbers()[0]()