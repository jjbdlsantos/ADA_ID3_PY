from ID3 import *
import pandas
import math
from fractions import Fraction
import operator
from TreeStructure import *
from ID3Apply import *


tree = Tree()

'''
@description
    reads a dataset. For the sake of simplicity, no user input is given, rather data is assumed to be mushroom set

@return 
    dataframe of csv file
'''
def readMushroomSet():
    return pandas.read_csv("C:\\Users\\user\\Desktop\\mushrooms.csv")

def percentage(percent, whole):
  return (percent * whole) / 100.0

'''
@description
    partitions given dataframe into training and test

@return
    returns a list of partitioned data
'''
def partitionSet(df):
    dflen = len(df)
    partition = []
    part60 = int(percentage(70, dflen))
    part30 = int(percentage(30, dflen))
    partition.append(df.iloc[0:part60])
    partition.append(df.iloc[part60:dflen])
    return partition

'''
@description
    ID3 algorithm recursively implemented

@param df
    dataframe to analyse

@param root
    node currently focused on to derive next branches or if end

@param lvl
    Layer of decision tree currently at
'''
columnIgnore = []
def ID3Func(df, root, lvl):
    level = lvl + 1
    branches = findBranches(df, root, columnIgnore)
    columnIgnore.append(root)
    for branch in branches:
        if branches[branch] == 'p' or branches[branch] == 'e':
            print level, "IF", root, "EQUALS", branch, "THEN", branches[branch]
            continue
        nextNode = max(branches[branch].iteritems(), key=operator.itemgetter(1))[0]
        if len(df.columns) != 1:
            print level, "IF", root, "EQUALS", branch, "THEN GO", nextNode
            ID3Func(df, nextNode, level)
        else:
            #Catch errors or skips
            return

'''
@description
    print confusion matrix

@param df
    dataframe to analyse WITH predicted data
'''
def printConfusionMatrix(df):
    correctE = 0
    correctP = 0
    totalE = 0
    totalP = 0
    unidentified = 0

    for index, row in df.iterrows():
        if df.loc[index]['prediction'] == 'e':
            totalE += 1
        if df.loc[index]['prediction'] == 'p':
            totalP += 1
        if pandas.isnull(df.loc[index]['prediction']):
            unidentified += 1
        if df.loc[index]['prediction'] == df.loc[index]['class']:
            if df.loc[index]['class'] == 'e':
                correctE += 1
            if df.loc[index]['class'] == 'p':
                correctP += 1
    accuracy = float(correctE + correctP)/float(len(df))

    print "True E: ", correctE, "False P: ", totalP - correctP
    print "False E: ", totalE - correctE, "True P: ", correctP
    print "Total elements: ", len(df)
    print "Unidentified: ", unidentified
    print "Accuracy = {:.1%}".format(accuracy)

'''
@description
    function to call necessary methods in intended order for ID3 to  work
'''
def treeGeneration():
    level = 0
    mushSet = readMushroomSet()
    partition = partitionSet(mushSet)
    trainMushSet = partition[0]
    testMushSet = partition[1]

    #find root node
    root = calcNode(trainMushSet, "class")
    columnIgnore.append(root)

    ID3Func(trainMushSet, root, level)

    rowCount = 0
    
    testMushSet['prediction'] = testMushSet['class']
    for index, row in testMushSet.iterrows():
        testMushSet.loc[index]['prediction'] = runDecisionTree(testMushSet, rowCount)
        rowCount += 1
    
    printConfusionMatrix(testMushSet)
treeGeneration()

