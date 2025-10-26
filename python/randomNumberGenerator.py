import random

def random_list():
    """
    generate a random number from 0 to 100 in 100 random numbers directory 
    """
    return [random.randint(0, 100) for _ in range(100)]


