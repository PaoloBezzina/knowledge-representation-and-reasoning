"""
Task 2
Construction and Reasoning with Inheritance Networks
"""

import sys
import copy

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
        self.polarity = polarity    #true = IS-A , false = IS-NOT-A

    def __str__(self):
        return "Subconcept: {} - Polarity: {} - Superconcept: {}".format(self.subConcept, self.polarity, self.superConcept)

    def __repr__(self):
        return "Subconcept: {} - Polarity: {} - Superconcept: {}".format(self.subConcept, self.polarity, self.superConcept)


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
        #print(kb[i])
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

    #print(newEdge)

    return newEdge



def parseConcept(c):

    numOfConcepts = len(conceptList)

    for i in range(0, numOfConcepts):
        if c == conceptList[i].name:
            #print("existing concept found: {}".format(conceptList[i]))      
            return conceptList[i]
    
    #print("creating new concept")
    temp = concept(c)

    conceptList.append(temp)

    return temp




def checkOutgoingEdges():

    numOfConcepts = len(conceptList)
    numofEdges = len(edgeList)

    for i in range(0, numOfConcepts):
        for j in range(0, numofEdges):
            if conceptList[i].name == edgeList[j].subConcept.name :

                #print("{} is an outgoing edge of {}".format(edgeList[j].superConcept.name, conceptList[i].name))

                conceptList[i].outgoingEdges.append(edgeList[j].superConcept.name)

"""
def findPath(first, last):

    pl = []
    fpl = []

    for c in conceptList:

        if(c == last):
            pl.append
            print("reached end of query")
            return pl
        elif( c == first):
            print("First is:")
            print(c)

            if(len(c.outgoingEdges) == 0):
                print("concept has no outgoing edges")
                return None
            else:
                for e in c.outgoingEdges:
                    findPath(e, last)
                    
    return fpl
"""
def findPath(first, last):

    pl = []
    fpl = []


    for e in edgeList:
        if(e.subConcept == first):

            p = path(e)
            print("path found")
            print(p)
            pl.append(p)

    print("path list")
    print(pl)

    for p in pl:

        print("\nNew Path Parse")
        print(p)
        
        curConcept = p.edges[-1].superConcept
        curPolarity = p.edges[-1].polarity

        print("curConcept:")
        print(curConcept)
        print(curPolarity)


        if(curConcept == last):
            #path stops here since we reached the end of the query
            print("pass")
            print(p)
            fpl.append(p)

            return fpl

        elif(curPolarity == True):

            npl = findPath(curConcept, last)

            #nahseb li problemi jibdew hawn

            print("new path list:")
            print(npl)
            print(len(npl))

            if(len(npl) == 0):
                ("No edges found")
                fpl.pop()
            elif (len(npl) == 1):
                print("One edge found")
                p.edges.append(npl)
                fpl.append(p)

            elif(len(npl) > 1):
                print("Multiple Edges Found")
                for np in npl:
                    cfp = copy.deepcopy(p)
                    cfp.edges.append(np)
                    print("Cfp is:")
                    print(cfp)
                    fpl.append(cfp)

    print("Current fpl")
    print(fpl)
    return fpl
 

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
