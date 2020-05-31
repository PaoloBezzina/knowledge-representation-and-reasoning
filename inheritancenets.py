"""
Task 2
Construction and Reasoning with Inheritance Networks
"""

import sys
import copy

import itertools



"""
Class Sub-Concept
"""

class concept(object):

    #Constructor
    def __init__(self, name):
        self.name = name
        self.outgoingEdges = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return "{} has outgoing edges: {}".format(self.name, self.outgoingEdges)


class edge(object):

    def __init__(self, superConcept, subConcept, polarity):
        self.superConcept = concept(superConcept)
        self.subConcept = concept(subConcept)
        self.polarity = polarity    #True = IS-A , False = IS-NOT-A

    def __str__(self):
        return "Subconcept: {} - Polarity: {} - Superconcept: {}".format(self.subConcept, self.polarity, self.superConcept)

    def __repr__(self):
        if(self.polarity == True):
            link = "IS-A"
        else:
            link = "IS-NOT-A"
        return "{} {} {}".format(self.subConcept, link, self.superConcept)

        #return "Subconcept: {} - Polarity: {} - Superconcept: {}".format(self.subConcept, self.polarity, self.superConcept)


class path(object):

    def __init__(self, edges):
        self.edges = [edges]

    def __str__(self):
        return ("{}".format(self.edges))

    def __repr__(self):
        return ("{}".format(self.edges))
        #("{}".format(self.edges))


def checkConcepts(p):
        max = len(p.edges)
        for i in range(0, max-1):
            if(p.edges[i].superConcept == p.edges[i+1].subConcept):
                print("valid edge pair")
                pass
            else:
                print("invalid pair")

"""
Data Parsing

"""

conceptList = []
edgeList = []
pathList = []


def parseKb(kb):

    numofEdges = len(kb)

    for i in range(0, numofEdges):
        edgeList.append(parseEdge(kb[i]))

    checkOutgoingEdges()


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

    concept1 = parseConcept(concepts[0])
    concept2 = parseConcept(concepts[1])

    newEdge.subConcept = concept1
    newEdge.superConcept = concept2


    return newEdge



def parseConcept(c):

    numOfConcepts = len(conceptList)

    for i in range(0, numOfConcepts):
        if c == conceptList[i].name:
     
            return conceptList[i]
    
    temp = concept(c)

    conceptList.append(temp)

    return temp




def checkOutgoingEdges():

    numOfConcepts = len(conceptList)
    numofEdges = len(edgeList)

    for i in range(0, numOfConcepts):
        for j in range(0, numofEdges):
            if conceptList[i].name == edgeList[j].subConcept.name :

                conceptList[i].outgoingEdges.append(edgeList[j].superConcept.name)


def findPath(first, last):

    pl = []
    fpl = []


    #Check for possible paths
    for e in edgeList:
        if(e.subConcept == first):

            p = path(e)
            pl.append(p)

    #For each path found
    for p in pl:

        #New Path Parse
        curConcept = p.edges[-1].superConcept
        curPolarity = p.edges[-1].polarity

        #Path stops here since we reached the end of the query
        if(curConcept == last):
            
            fpl.append(p)

        elif(curPolarity == True):

            npl = findPath(curConcept, last)

            #One edge found
            if (len(npl) == 1):

                p.edges.extend(npl)
                fpl.append(p)

            #Multiple Edges Found
            elif(len(npl) > 1):

                for np in npl:
                    cfp = copy.deepcopy(p)
                    cfp.edges.extend(np.edges)
                    fpl.append(cfp)

    return fpl

def findShortestPath(pl):

    numberOfPaths = len(pl)

    for i in range(numberOfPaths):
        for j in range(numberOfPaths-i-1):
            if(len(pl[i].edges) > len(pl[j+1].edges)):
                pl[i], pl[j+1] = pl[j+1],pl[i]

    return pl[0]

"""
Functions needed to return shortest path according to inferantial distance
"""

redundantEdge = []

def checkForRedundant(pe):

    for i in range(len(pe.edges)):
        sub = pe.edges[i].subConcept
        sup = pe.edges[i].superConcept

        conc = findPath(sub , sup)

    print(conc)

def checkForPreEmpted(pe):

    print(pe)

    for i in range(len(pe.edges)):
        for j in range(len(edgeList)):
            print(pe.edges[-1])
            print(edgeList[j].superConcept)
            if edgeList[j].subConcept == pe.edges[i].subConcept and edgeList[j].superConcept == pe.edges[-1].superConcept and edgeList[j].polarity != pe.edges[i].polarity:
                print("Pre-empted edge found")
                return True

    return False

def inferentialDistance(pl):

    for p in pl:

        r1 = checkForPreEmpted(p)
        r2 = checkForRedundant(p)

        if(r1 == True and r2 == True):
            print(p , "is admissable")
        else:
            print(p , "is not admissable")


"""
An attempt at flattenning the list. ie: remove the extra nested lists
"""

#doesnt work
def flattenList(pl):

    list(itertools.chain.from_iterable(x.edges for x in pl))


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

print("\nConcepts:")
print(conceptList)
print("\nEdges:")
print(edgeList)
print("\nPaths:")
print(pathList)

q = input("Enter Query: ")
query = parseEdge(q)

pathList = findPath(query.subConcept, query.superConcept)
print("\nPaths:")
for p in pathList:
    print(p)

"""
print("Flattened  List")
fpl = flattenList(pathList)
print(fpl)
"""

print("\nShortest Path:")
sp = findShortestPath(pathList)
print(sp)

"""
print("\nInferential Distance:")
id = inferentialDistance(pathList)
print(id)
"""