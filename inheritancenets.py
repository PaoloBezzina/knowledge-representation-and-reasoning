"""
Task 2
Construction and Reasoning with Inheritance Networks
"""

import sys

"""
Class Sub-Concept
"""

class concept(object):

    #Constructor
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class edge(object):

    def __init__(self, superConcept, subConcept, polarity):
        self.superConcept = superConcept
        self.subConcept = subConcept
        self.polarity = polarity    #true = IS-A , false = IS-NOT-A

    def __str__(self):
        return "Subconcept: {}, Superconcept: {}, Polarity {}".format(self.subConcept, self.superConcept, self.polarity)

    def __repr__(self):
        return self.name


class path(object):

    def __init__(self, edges):
        self.edges = edges

    def __str__(self):
        return self.edges

    def __repr__(self):
        return self.edges
    
    def checkConcepts(self):
        max = len(self.edges)
        for i in range(0, max-1):
            if(self.edges[i].superConcept == self.edges[i+1].subConcept):
                print("valid edge pair")
                pass
            else:
                print("invalid pair")

"""
Data Parsing
"""
def parseKb(kb):

    numofEdges = len(kb)

    for i in range(0, numofEdges):
        print(kb[i])
        parseEdge(kb[i])



def parseEdge(e):

    newEdge = edge(None, None, False)

    if "IS-A" in e:

        newEdge.polarity = True

        concepts = e.split(" IS-A ")

    elif "IS-NOT-A" in e:

        newEdge.polarity = False

        concepts = e.split(" IS-NOT-A ")

    else:
        print("error in Kb")

    newEdge.subConcept = concepts[0]
    newEdge.superConcept = concepts[1]

    print(newEdge)

    return newEdge






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

parseKb(kb)