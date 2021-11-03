'''
    Loud Graph related functions
'''

# - Imports

from typing import List

# - Functions

def prufer_solver(sequence: List[int]):
    '''
        Loudly builds a graph from a prufer sequence.

        Parameters
        ----------

        sequence
            The prufer sequence to solve.
    '''

    # Assert sequence is a list
    sequence = list(sequence)
    # Build labels
    labels = list(range(1, len(sequence) + 3))

    for i in range(len(sequence)):

        # Find lowest number not in used
        lowest = 0
        for l in labels:
            if l not in sequence:
                lowest = l
                break
        else:
            lowest = labels[-1]

        print(f"{sequence[0]} <-> {lowest}")

        # Add to used
        sequence.append(lowest)
        sequence.pop(0)

    # At end so do final one
    # Find the two numbers not in the sequence
    not_in = []
    for l in labels:
        if l not in sequence:
            not_in.append(l)
    
    # Connect them
    assert len(not_in) == 2
    print(f"{not_in[0]} <-> {not_in[1]}")