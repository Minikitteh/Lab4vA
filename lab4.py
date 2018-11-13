#Yamel Hernandez
#80590552
#CS 2302
#Diego Aguirre
#Anindita Nath
#Lab 4 Ver A
#Purpose of this lab was to understand how to use
#Hashtables and their implementation for the glove file
####################################################################

from ChainingHashTable import ChainingHashTable
from Node4 import Node4
import math


#2 SImilarity with embeddings & word mag

	#dot product
def dotProduct(x, y):
    sum = 0
    for i in range(len(x.embeddings)):
        sum += (float(x.embeddings[i]) * float(y.embeddings[i]))
    return sum

	#finds word magnitude of its embedding
def wordMagnitude(x):
    sum = 0
    for i in range(len(x.embeddings)):
        sum += (math.pow(float(x.embeddings[i]), 2))
    return math.sqrt(sum)

	#finds similarity
def similarTo(x, y):
        if x is None:
            print('x')
        if y is None:
            print('y')
        mag1 = wordMagnitude(x)
        mag2 = wordMagnitude(y)
        dotPro = dotProduct(x, y)
        similar = (dotPro) / (mag1 * mag2)
        return similar
 
#3 Finish the following to finish lab   

#Compute number of nodes in the tree
def countNodes (x):
    counter = 0
    for bucket in x.table:
        counter += len(bucket)
    return counter
    
#compute (height)longest list
def longestList(x):
    countMax = 0
    for i in x.table:
        if len(i) > countMax:
            countMax = len(i)
    return countMax 

#avg number of comparisions
def avgComparisons(x):
    counter = 0
    for bucket in x.table:
        counter += len(bucket)/2
    return counter
     
#load factor
def loadFactor(x):
    return countNodes(x)/len(x.table)
 
#print keys at an index
def printKeysAtIndex(x, k):
    pos = k%len(x)
    while x[pos] != None:
        print(x.item + " ")
        x = x.next

####################################################################

def main():
    use = "/home/yamel/Desktop/CS3/lab3/glove.6B.50d.txt"
    print("storing glove in a hashtable...")
    H = ChainingHashTable()
    with open(use) as f:
        for line in f:
            info = line.split(' ')
            if info[0][0].isalpha():
                node = Node4(info[0], info[1:])
                H.insert(node)
    print ("Number of Nodes: " + str(countNodes(H)))
    print("Longest list: " + str(longestList(H)))
    print("Avg Comparisions: " + str(avgComparisons(H)))
    print("Load Factor: " + str(loadFactor(H)))           
    use2 = "/home/yamel/Desktop/CS3/lab3/similarities.txt"
    with open(use2) as f:
        for line in f:
            words = line.split(' ')
            word1 = words[0]
            word2 = words[1].rstrip('\n')
            node1 = H.search(word1)
            node2 = H.search(word2)
            if node1 and node2:
                print(word1 + ' ' + word2 + ' ' + str(similarTo(node1, node2)))
    
    
    
main()