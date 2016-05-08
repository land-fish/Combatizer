import pymc

# A set of methods that return a perturber utility vector subject to parameters given to the constructor. Helper
# methods are prefixed with "h_".

# Usage
#  Perturber(utilities, comparitor, threshold).perturbing_method()
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
        if type(utilities) != 'list':
            raise StandardError(s.h_log('Utilities parameter is not a list'))
        for utility in utilities:
            if not s.h_utilities_within_range(utilities):
                raise StandardError(s.h_log('At least one of the given utilities is not in the interval [-1,1]'))
        s.utilities = utilities
        
        s.comparitor = comparitor
        
        if type(threshold) != float:
            if type(threshold) == int:
                threshold = float(threshold)
            else:
                raise StandardError('Given threshold does not have type int or float')
        if threshold < -1 or threshold > 1:
            raise StandardError(s.h_log('Given threshold is not within the interval [-1,1]'))
        s.threshold = threshold
    
    # Normally perturb input
    def normal(s):
        result = []
        return result
    
    def h_log(s, logtext):
        return '%s: %s' % (s.__class__.__name__, logtext)
    
    def h_utilities_within_range(s, utilities):
        for utility in utilities:
            if utility < -1 or utility > 1:
                return False
        return True

if __name__ == '__main__':
    p = Perturber([1], 'blah', 2)