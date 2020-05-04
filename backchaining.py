"""
Parsing of Horn Clauses, and Reasoning using Back-Chaining
"""
import sys

#open read only file (read and write = "w+")

print(f"Name of the script      : {sys.argv[0]=}")
print(f"Arguments of the script : {sys.argv[1:]=}")

file = sys.argv[1:]
print(file)

f= open("%s" %file[0],"r")


kb = f.read().splitlines()

print(kb)



