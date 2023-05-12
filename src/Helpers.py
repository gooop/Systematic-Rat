"""
HELPERS CLASS:
A class to put helper functions used in Systematic Rat

Originally written for Systematic Rat
https://github.com/gooop/Systematic-Rat

Copyright 2023 Gavin Castaneda
"""

# ==== Includes ====

class Helpers:
    @staticmethod
    def open_file(filename):
        """A simple function to return the contents of a file"""
        with open(filename, 'rt') as f:
            contents = f.read()
            f.close()
        return contents