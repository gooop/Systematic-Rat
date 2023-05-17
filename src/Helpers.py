"""
HELPERS CLASS:
A class to put helper functions used in Systematic Rat

Originally written for Systematic Rat
https://github.com/gooop/Systematic-Rat

Copyright 2023 Gavin Castaneda
"""

# ==== Includes ====
from cryptography.fernet import Fernet

# ==== Class ====
class Helpers:
    # ==== Static Methods ====
    @staticmethod
    def open_file(filename):
        """A simple function to return the contents of a file"""
        try:
            with open(filename, 'rt') as f:
                contents = f.read()
                f.close()
        except Exception as e:
            print(f"Error in open_file: {e}")
            raise e
        return contents
    
    @staticmethod
    def write_file(filename, contents, overwrite=True):
        """A simple function to write to a file"""
        if overwrite:
            try:
                with open(filename, 'wb') as f:
                    f.write(contents)
                    f.close()
            except TypeError:
                with open(filename, 'w') as f:
                    f.write(contents)
                    f.close()
            except Exception as e:
                print(f"Error in write_file: {e}")
                raise e
        else:
            try:
                with open(filename, 'a') as f:
                    f.write(contents)
                    f.close()
            except Exception as e:
                print(f"Error in write_file: {e}")
                raise e
