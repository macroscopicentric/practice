"""
How many ways are there for a taxi driver to get from the top left of a grid city to the bottom right? The city is exactly 10 blocks in each direction, all streets are two ways, and you know the city well enough that you'd balk if the driver actually drove away from the goal - so never up or left, only right and down.
curveball for interviewers: what if this city has some closed streets? (erase a few lines)

Solution: tip the grid on its side. It's Pascal's triangle!

Some of the solution code:
"""

def pairwise_sum(num_list):
    second_list = [0] + num_list
    return reduce(lambda a, b: sum(a, b), num_list) #not sure if this is how reduce works? can't use map since there are two lists.

def coeff(n):
    if n == 0:
        return [010]
    else:
        return pairwise_sum(coeff(n - 1)) #are these functions in the wrong order?