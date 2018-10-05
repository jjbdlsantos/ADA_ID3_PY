import pandas
import math
from fractions import Fraction
import operator

columnToPredict = 'class'

###Debug
def readDataset():
    return pandas.read_csv("C:\\Users\\user\\Desktop\\tennis.csv")

'''
@description
    calculates entropy

@param total
    Total number of instances

@param attr1
    Number of instances for first attribute

@param attr2
    Number of instances for second attribute

@return
    Returns entropy
'''
def calcEntropy(total, attr1, attr2):
    p1 = Fraction(attr1, total)
    p1 = p1 * math.log(p1, 2)
    if attr2 > 0:
        p2 = Fraction(attr2, total)
        p2 = p2 * math.log(p2, 2)
    else:
        p2 = 0
    return -(p1 + p2)

'''
@description
    calculate information gain

@param column
    Column being focused on for information gain

@param dataset
    Dataframe to be analysed on

@return
    returns information gain
'''
def calcInfoGain(column, dataset):
    #split by column
    columnSubsets = []
    for region, df_region in dataset.groupby(column):
        columnSubsets.append(df_region)
    px = 0
    for subset in columnSubsets:
        series = subset[columnToPredict].value_counts()
        if len(series) == 1:
            entropy = calcEntropy(len(subset), series[0], 0)
        else:
            entropy = calcEntropy(len(subset), series[0], series[1])
        pEntropy = (Fraction(len(subset), len(dataset))) * entropy
        px -= pEntropy
    return columnEntropy(dataset, columnToPredict) + px 

'''
@description
    Wrapper for calcEntropy which applies a dataframe and column to focus on

@param df
    dataframe to be analysed

@param column
    column to calculate entropy off of

@return
    entropy of column
'''
def columnEntropy(df, column):
    series = df[column].value_counts()
    if len(series) == 1:
        return calcEntropy(len(df), series[0], 0)
    return calcEntropy(len(df), series[0], series[1])

'''
@description
    initial function to be called to find first root

@param dataframe
    Dataframe to be analysed

@param toClassify
    label intended to be classified

@return
    column which yields highest information gain
'''
def calcNode(dataframe, toClassify):
    currEnt = columnEntropy(dataframe, toClassify)
    infoGainDict = {}
    for column in list(dataframe):
        if column == toClassify:
            pass
        else:
            infoGainDict[column] = calcInfoGain(column, dataframe)
    return (max(infoGainDict.iteritems(), key=operator.itemgetter(1))[0])

'''
@description
    Basic check to see if entire column is uniform

@param iterator
    column intended to be analysed

@return
    bool
'''
def checkUniformity(iterator):
   return len(set(iterator)) <= 1

'''
@description
    Returns a dictionary of "branches" which contain either next nodes or a decision

@param dataframe
    dataframe to be analysed

@param root
    the root node to derive branches from

@param ignore
    list of columns to ignore

@return
    dictionary of branches
'''
def findBranches(dataframe, root, ignore):
    dfs = dict(tuple(dataframe.groupby(root)))
    branches = {}
    for attr in dataframe[root].unique():
        del dfs[attr][root]
        attributes = {}
        for column in dfs[attr]:
            if column == columnToPredict or column in ignore:
                pass
            else:
                attributes[column] = (calcInfoGain(column, dfs[attr]))
        if(checkUniformity(attributes.values())):
            branches[attr] = dfs[attr].iloc[0]['class']
        else:
            branches[attr] = attributes
    return branches

###Debug
def main(): 
    dataframe = readDataset()
    currEnt = columnEntropy(dataframe, 'Decision')
    infoGainDict = {}
    for column in list(dataframe):
        if column == 'Decision' or column == 'Day':
            pass
        else:
            infoGainDict[column] = calcInfoGain(column, dataframe)
    analysedColumns = []
    root = (max(infoGainDict.iteritems(), key=operator.itemgetter(1))[0])
    analysedColumns.append(root)
    branches = findBranches(dataframe, root)
    for branch in branches.keys():
        return





