"""
This module will generate randomized educational assignments for studying Python.
"""

"""
Architecture:
  Structure storing lists of assignments (strings)
    - Weights for which assignments should be offered more frequently
    - Functions to list, add, remove, change weights of assignments
    - Functions to store and print assignment history
    - Random assignment picker that uses weights
    - Completed assingments are removed from the random pool unless reset
    - Program can be pickled for storage of current state

"""
from numpy.random import choice


class RandomEd(object):
    """This class generates random education assignments"""
    def __init__(self, **args):
        """Initialize with a tuple of dictionary key=assignment, value=weights"""
        print("Init: ", self.__class__.__name__)
        self.assignments = args

        # Which assignments have been completed
        self.history = {}

    def normalize_weights(self):
        """Normalize weights to sum to 1 for numpy choice selection
           Return the assignment values with normalized weights
        """
        sumweights = sum(self.assignments.values())
        keys = list(self.assignments)
        normweights = [(i/float(sumweights)) for i in self.assignments.values()]
        return dict(zip(keys, normweights))

    def print_list(self):
        """Print a list of all possible assignments"""
        print(self.assignments)

    def pick_ed(self):
        """Pick the next educational assignment"""
        weightedvals = self.normalize_weights()

        next_ed = choice(list(weightedvals), p=list(weightedvals.values()))
        choicestring = "Next assignment is " + next_ed + ". Accept(Y/N):"
        reply = input(choicestring)
        if reply == 'Y':
            ni = self.assignments.pop(next_ed)
            self.history[next_ed] = ni

    def print_history(self):
        """Print the history of assignments selected"""
        print(self.history)

    def add_ed(self, **args):
        """Add new assignments"""
        self.assignments.update(args)

    def remove_ed(self, *args):
        """Remove assignments from the list"""
        for item in args:
            del self.assignments[item]

    def reset_list(self):
        """Restore all previously completed assignments to list"""
        self.assignments.update(self.history)
        self.history = {}

if __name__ == "__main__":
    print("This is main")
    r = RandomEd(a=0.2, b=0.3, c=0.4)
    r.print_list()
    r.pick_ed()
    print("Assignments completed:")
    r.print_history()
    print("After assignments reset:")
    r.reset_list()
    r.print_list()
    r.print_history()
    print("Adding new assignments, d, e, f")
    r.add_ed(d=1, e=2, f=3)
    r.print_list()
    print("Deleting assignments, e, c")
    r.remove_ed('e', 'c')
    r.print_list()
