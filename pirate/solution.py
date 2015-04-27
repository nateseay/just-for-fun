#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

"""
A pirate walks into a bar...
"""

__author__ = 'Nate Seay (nate.seay@gmail.com)'

def recursive_walk(numbers, pos, depth, depth_dict):
    # This is actually a bad solution- with the full sized list, I'd hit a
    # stackoverflow
    if pos in depth_dict:
        return depth - depth_dict[pos]
    depth_dict[pos] = depth
    depth +=1
    pos = numbers[pos]
    return recursive_walk(numbers, pos, depth, depth_dict)

class PirateIter():
    
    def __init__(self, pirate_list):
        self.pirate_list = pirate_list
        self.pos = 0

    def __iter__(self):
        return self

    def next(self):
        self.pos = self.pirate_list[self.pos]
        return self.pos 

def walk(numbers):
    depth_dict = {}
    walker = PirateIter(numbers)
    for depth, pos in enumerate(walker):
        if pos in depth_dict:
            return depth - depth_dict[pos]
        depth_dict[pos] = depth


def answer(numbers):
    # Doctest 
    '''
    >>> answer([1, 3, 0, 1])
    (2, 2)
    >>> answer([1,0])
    (2, 2)
    >>> answer([1,2,1])
    (2, 2)
    >>> answer([0])
    (1, 1)
    >>> answer([1,2,3,4,5,6,7,8,9,2])
    (8, 8)
    '''
    depth_dict = {}
    pos, depth = 0,0
    return recursive_walk(numbers, pos, depth, depth_dict), walk(numbers)
