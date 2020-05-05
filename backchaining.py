"""
Task 1
Parsing of Horn Clauses, and Reasoning using Back-Chaining
"""
import sys

"""
Class Clause
"""

class clause(object):

    #Constructor
    def __init__(self, num):
        self.num = name


"""
Class Literal
"""

class literal(object):

    #Constructor
    def __init__(self, name, polarity):
        self.name = name
        self.polarity = polarity


"""
Main
"""

#open read only file (read and write = "w+")

print(f"Name of the script      : {sys.argv[0]=}")
print(f"Arguments of the script : {sys.argv[1:]=}")

file = sys.argv[1:]
print(file)

f= open("%s" %file[0],"r")


kb = f.read().splitlines()

print(kb)



