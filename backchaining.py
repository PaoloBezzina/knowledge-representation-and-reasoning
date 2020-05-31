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

    def __str__(self):
        return self.literals

    def __repr__(self):
        return ("{}".format(self.literals))


"""
Class Literal
"""

class literal(object):

    #Constructor
    def __init__(self, name, negated):
        self.name = name
        self.negated = negated

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name



"""
Data Parsing
"""

#parsing kb
def parseKB(kb):
    
    numOfClauses = len(kb)
    #print(numOfClauses)

    clauseList = [None] * numOfClauses

    for i in range(0,numOfClauses):
        print(kb[i])
        clauseList[i] = parseClause(kb[i])

    return clauseList


def parseClause(c):

    literalList = []
    
    c = c[1:-1]

    literals = c.split(",")
    #print(literals) #outputs "['Male']" ie. array of literals

    numOfLiterals = len(literals)
    #print(numOfLiterals)

    for i in range(0, numOfLiterals):

        lit = literal("null", False)

        #print(literals[i]) #outputs "Male" ie.Outputs one literal from array of literals
        if("!" in literals[i]):
            lit.name = literals[i][1:]
            lit.negated = True
        else:
            lit.name = literals[i]
            lit.negated = False

        #print(lit) #outputs "<class '__main__.literal'>"
        #print(lit.name) #outputs "Male"
        #print(lit.negated)  #outputs "False"
        literalList.append(lit)
    
    cl = clause(literalList)

    #print(cl.literals)

    return cl

"""
Backchaining
"""

def reasoning(c, Kb):
    recBc = False
    if len(c.literals) == 0:
        return True
    else:
        for l in c.literals:
            for c in Kb:
                for i in range(0, len(c.literals)):
                    
                    if (c.literals[i].name == l.name) and (c.literals[i].negated != l.negated):

                        newlit = []
                        j = 0

                        while not c.literals[i] == c.literals[j]:
                            
                            newlit.append(c.literals[j])

                            """
                            #un-comment this area to check which literals are being checked upon recursion

                            if newlit[j].negated:
                                print("recursion !{}".format(newlit[j].name))
                            else:
                                print("recursion normal{}".format(newlit[j].name))
                            """

                            j = j + 1

                        newClause = clause(newlit)
                        recBc = reasoning(newClause, Kb)

                    if recBc == True:
                        return True
    return False
            


"""
Main
"""

#open read only file (read and write = "w+")
print(f"Script being run    : {sys.argv[0]=}")
print(f"Knowledge Base      : {sys.argv[1:]=}")

file = sys.argv[1:]
print(file)

f= open("%s" %file[0],"r")

kb = f.read().splitlines()

KnowledgeBase = parseKB(kb)

print(KnowledgeBase)#temp

query = input("Please input the query: ")

query = parseClause(query)

res = reasoning(query, KnowledgeBase)

if res:
    print("Query Succesfuly Solved")
else:
    print("Query has been unsuccessful")
