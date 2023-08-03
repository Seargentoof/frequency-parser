"""
Utilities for the freqencyParser program. 

Dawson Lin, 8/1/2023
"""

"""
Reads a file line-by-line and returns it as a list lines. 
"""
def read_file_lines(filePath):
    try:
        with open(filePath, 'r') as file:
            lines = [line.rstrip('\n') for line in file.readlines()]
        return lines
    except FileNotFoundError:
        print(f"File '{filePath}' not found.")
        return []
    except IOError:
        print(f"Error reading file '{filePath}'.")
        return []