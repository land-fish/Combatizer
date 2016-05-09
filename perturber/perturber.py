import numpy
import random
import math

# Set of methods that return a perturbed utility vector subject to params passed into the constructor.
# Example usage
#  import perturber, random
#  my_comparitor = lambda x,y: 1 - sum([abs(x[i] - y[i]) for i in range(len(x))])/float(len(x))
#  perturbers = perturber.Perturber([-0.5, -1, 0.5, 1, 0], my_comparitor, 0.75).get_perturbers()
#  perturbed_utilities = random.choice(perturbers)()
class Perturber:
    # Arguments
    #  utilities: A vector of floats with values in [-1,1]. Each element in the vector represents the utility of a
    #   single world.
    #  comparitor: A function that takes two utility vectors and outputs a value in [-1,1]. The output represents
    #   the similarity between the two inputs.
    #  threshold: A value between [-1,1]. Represents the minimum similarity (according to "comparitor") that a
    #   perturbed utility vector should have to the "utilities" parameter.
    def __init__(s, utilities, comparitor, threshold):
        # Validate parameters and save them into instantiated object if they're valid.
        if type(utilities) != list:
            raise StandardError(s.log('Utilities parameter is not a list'))
        for utility in utilities:
            if not s.utilities_within_range(utilities):
                raise StandardError(s.log('Given utilities must all be in the interval [-1,1]'))
        s.utilities = utilities[:]
        
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
            # For each utility, repeatedly try adding normal noise until perturbation falls within expected interval
            for utility in s.utilities:
                while True:
                    # Add normal noise with mu == 0 and sigma^2 == cur_var
                    cur_result = utility + numpy.random.randn() * math.sqrt(cur_var)
                    if s.utilities_within_range([cur_result]):
                        break
                result.append(cur_result)
            if s.comparitor(s.utilities, result) >= s.threshold:
                break
            cur_var /= 2  # Reduce variance on failure to increase chance that next iteration will meet threshold
            
        return result
   
    # Removes top 10% of utility values and replaces them with random values 
    def remove_max(s):
        remove_ratio = .1
          #replace_num is the number of elements in the list to be changed
        replace_num = int(math.ceil(len(s.utilities) * remove_ratio)) 
        top_ratio_index = sorted(range(len(s.utilities)), key=lambda i: s.utilities[i], reverse=True)[:replace_num] 
        
        #Replace top values with random values between -1 and 1
        while True:
            result = s.utilities
            for aa in top_ratio_index:
                result[aa] = random.random() * 2 - 1 
            if s.comparitor(s.utilities, result) >= s.threshold:
                break

        return result      

    # Replaces set proportion of random utility values with 1 
    def false_highs(s):
        replace_ratio = .1
        #replace_num says how many utilites to replace and rounds up
        replace_num = int(math.ceil(len(s.utilities) * replace_ratio)) 

        while True:
            result = s.utilities
            replace_list = []
            #For a random 10% of utilities, try to replace value with 1 until pertubation falls within expected interval 
            for i in range(replace_num):  
                index = int(len(s.utilities) * random.random())
                while index not in replace_list:
                    replace_list.append(index)   
            for value in replace_list:
                result[value] = 1
            if s.comparitor(s.utilities, result) >= s.threshold:
                break

        return result      

 

    def h_log(s, logtext):
        return '%s: %s' % (s.__class__.__name__, logtext)
    
    # Perturb by randomly swapping 2 utilities
    def random_swap(s):
        found_result = False
        
        # Only try 100 swaps so that the code doesn't run forever
        for i in range(100):
            # Get 2 unequal indexes
            indexes = range(len(s.utilities))
            c1 = random.choice(indexes)
            indexes.remove(c1)
            c2 = random.choice(indexes)
            
            # Swap them
            result = s.utilities[:]
            result[c1], result[c2] = result[c2], result[c1]
            
            if s.comparitor(s.utilities, result) >= s.threshold:
                found_result = True
                break
        
        # If we found a swap that meets the threshold requirement, return that. Else return the original list.
        if found_result:
            return result
        else:
            return s.utilities
    
    # Return list of perturbers
    def get_perturbers(s):
        return [s.normal, s.random_swap, s.remove_max, s.false_highs]
    
    # Log output
    def log(s, logtext):
        return '%s: %s' % (s.__class__.__name__, logtext)
    
    # True if all utilities in a vector are in the interval, else false
    def utilities_within_range(s, utilities):
        for utility in utilities:
            if utility < -1 or utility > 1:
                return False
        return True


# Used for testing
if __name__ == '__main__':
    comparitor = lambda x,y: 1 - sum([abs(x[i] - y[i]) for i in range(len(x))])/float(len(x))
    p = Perturber([random.random() * 2 -1 for i in range(10)], comparitor, 0.9)
    #p.normal()
    p.remove_max()
    p.false_highs()
    p = Perturber([i/10. for i in range(10)], comparitor, 0.999)
    print p.get_perturbers()[0]()

