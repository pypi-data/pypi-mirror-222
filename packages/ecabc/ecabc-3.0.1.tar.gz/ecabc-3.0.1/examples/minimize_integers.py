#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# examples/minimize_integers.py
#
# Example showing how to tune three integer values to minimize their sum
#

# Import the `ABC` object
from ecabc import ABC


# Define the objective function the colony will use
def minimize_integers(integers: list) -> int:
    ''' minimize_integers: returns the sum of supplied integers

    Args:
        integers (list): list of integers

    Returns:
        int: sum of the supplied integers
    '''

    return sum(integers)


def main():

    # Create the colony with 10 employer bees and the above objective function
    abc = ABC(10, minimize_integers)

    # Add three integers, randomly initialized between 0 and 10 for each bee
    abc.add_param(0, 10, name='Int_1')
    abc.add_param(0, 10, name='Int_2')
    abc.add_param(0, 10, name='Int_3')

    # Initialize 10 employer bees, 10 onlooker bees
    abc.initialize()

    # Run the search cycle 10 times
    for _ in range(10):
        abc.search()
        print('Average fitness: {}'.format(abc.average_fitness))
        print('Average obj. fn. return value: {}'.format(abc.average_ret_val))
        print('Best fitness score: {}'.format(abc.best_fitness))
        print('Best obj. fn. return value: {}'.format(abc.best_ret_val))
        print('Best parameters: {}\n'.format(abc.best_params))


if __name__ == '__main__':

    main()
