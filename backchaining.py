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
    def __init__(self, literals):
        self.literals = literals




"""
Class Literal
"""

class literal(object):

    #Constructor
    def __init__(self, name, negated):
        self.name = name
        self.negated = negated


"""
Main
"""

#parsing kb
def parseKB(kb):
    
    numOfClauses = len(kb)
    print(numOfClauses)

    clauseList = [None] * numOfClauses

    for i in range(0,numOfClauses):
        print(kb[i])
        c = kb[i]
        clause = parseClause(c)
        clauseList[i] = clause

    return clauseList


def parseClause(c):

    literalList = []

    c = c[1:-1]

    literals = c.split(",")

    numOfLiterals = len(literals)
    print(numOfLiterals)

    for i in range(0, numOfLiterals):
        if("!" in literals[i]):
            literal.name = literals[i][1:]
            literal.negated = True
        else:
            literal.name = literals[i]
            literal.negated = False

        literalList.append(literal)
    
    clause.literals = literalList

    return clause

def reasoning(clause):

    



#open read only file (read and write = "w+")
print(f"Name of the script      : {sys.argv[0]=}")
print(f"Arguments of the script : {sys.argv[1:]=}")

file = sys.argv[1:]
print(file)

f= open("%s" %file[0],"r")

kb = f.read().splitlines()

parseKB(kb)




