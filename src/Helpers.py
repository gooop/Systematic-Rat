"""
HELPERS CLASS:
A class to put helper functions used in Systematic Rat

Originally written for Systematic Rat
https://github.com/gooop/Systematic-Rat

Copyright 2025 Gavin Castaneda
"""

# ==== Includes ====
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def open_file(filename):
    """A simple function to return the contents of a file
    
    Args:
        filename (str): the filename to read

    Returns:
        contents (str): The contents of the file read"""
    try:
        with open(filename, 'rt') as f:
            contents = f.read()
            f.close()
    except Exception as e:
        print(f"Error in open_file: {e}")
        raise e
    return contents


def write_file(filename, contents, overwrite=True):
    """A simple function to write to a file
    
    Args:
        filename (str): the filename to write to
        contents (str): The contents of the file write
    """
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


async def try_delete_message(context):
    try:
        await context.message.delete()
    except Exception as e:
        print(f"Failed to delete message: {e}")
