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
        return self.edges

    def __repr__(self):
        return ("{}".format(self.edges))
    
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

conceptList = []
edgeList = []
pathList = []

def parseKb(kb):

    numofEdges = len(kb)

    for i in range(0, numofEdges):
        print(kb[i])
        edgeList.append(parseEdge(kb[i]))

    checkOutgoingEdges()

    print(edgeList)





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

    print(newEdge)
    print("\n")

    return newEdge



def parseConcept(c):

    numOfConcepts = len(conceptList)

    for i in range(0, numOfConcepts):
        if c == conceptList[i].name:
            print("existing concept found: {}".format(conceptList[i]))      
            return conceptList[i]
    
    print("creating new concept")
    temp = concept(c)

    conceptList.append(temp)

    return temp




def checkOutgoingEdges():

    numOfConcepts = len(conceptList)
    numofEdges = len(edgeList)



    for i in range(0, numOfConcepts):
        for j in range(0, numofEdges):
            if conceptList[i].name == edgeList[j].subConcept.name :

                print("{} is an outgoing edge of {}".format(edgeList[j].superConcept.name, conceptList[i].name))

                conceptList[i].outgoingEdges.append(edgeList[j].superConcept.name)


"""
def checkConcepts(self):
        max = len(self.edges)
        for i in range(0, max-1):
            if(self.edges[i].superConcept == self.edges[i+1].subConcept):
                print("valid edge pair")
                pass
            else:
                print("invalid pair")



def parsePaths():

    for con in conceptList:

        pe = []

        for oe in con.outgoingEdges:
            for e in edgeList:
                if((oe == e.superConcept.name) and (con.name == e.subConcept.name)):

                    print("{} , {}".format(oe, e.superConcept) )
                    pe.append(e)

            p = path(pe)            
            pathList.append(p)

"""

def findPath(first, last):

    pl = []

    for e in edgeList:
        if(e.subConcept.name == first.name):

            p = path(e)
            pl.append(p)

    print(pl)
    for p in pl:
        if(p.edges[-1].polarity == False):
            #path stops here since it cannot continue after Is-Not-A
            print("False")
            return False

        print(p.edges[-1].superConcept)

        if(p.edges[-1].superConcept == last):
            #path stops here since we reached the end of the query
            print("pass")
            return True
            
        pn = []
        for ed in edgeList:
            if(p.edges[-1].superConcept == ed.subConcept):
                print("found e")
                pn.append(ed)
        
        if (len(pn) <= 0):
            #delete the current path
            pl.remove(pn)
            #not sure if we should have return here
        elif (len(pn) == 1):
            #add this edge to the path
            p.edges.append(pn)
        elif (len(pn) > 1):
            #copy path for each edge
            #add each edge to the copy of the path
            for em in pn:
                temp = copy(p)
                temp.edges.append(em)

                print("temp")


        #repeat
                    



        

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

findPath(query.subConcept, query.superConcept)


