import pandas
import math
from fractions import Fraction
import operator

def readDataset():
    return pandas.read_csv("C:\\Users\\user\\Desktop\\tennis.csv")

def calcEntropy(total, attr1, attr2):
    p1 = Fraction(attr1, total)
    p1 = p1 * math.log(p1, 2)
    if attr2 > 0:
        p2 = Fraction(attr2, total)
        p2 = p2 * math.log(p2, 2)
    else:
        p2 = 0
    return -(p1 + p2)

def calcInfoGain(column, dataset):
    #split by column
    columnSubsets = []
    for region, df_region in dataset.groupby(column):
        columnSubsets.append(df_region)
    px = 0
    for subset in columnSubsets:
        series = subset['Decision'].value_counts()
        if len(series) == 1:
            entropy = calcEntropy(len(subset), series[0], 0)
        else:
            entropy = calcEntropy(len(subset), series[0], series[1])
        pEntropy = (Fraction(len(subset), len(dataset))) * entropy
        px -= pEntropy
    return zentropy(dataset, 'Decision') + px 

def zentropy(df, column):
    series = df[column].value_counts()
    if len(series) == 1:
        return calcEntropy(len(df), series[0], 0)
    return calcEntropy(len(df), series[0], series[1])

def main(): 
    dataframe = readDataset()
    currEnt = zentropy(dataframe, 'Decision')
    infoGainDict = {}
    for column in list(dataframe):
        if column == 'Decision' or column == 'Day':
            pass
        else:
            infoGainDict[column] = calcInfoGain(column, dataframe)
    print(infoGainDict)
    
    root = (max(infoGainDict.iteritems(), key=operator.itemgetter(1))[0])
    
    dfs = dict(tuple(dataframe.groupby(root)))
    nextBranch = {}
    for attr in dataframe[root].unique():
        del dfs[attr]['Day']
        del dfs[attr][root]
        attributes = {}
        for column in dfs[attr]:
            if column == 'Decision':
                pass
            else:
                attributes[column] = (calcInfoGain(column, dfs[attr]))
        nextBranch[attr] = attributes
    for key in nextBranch.keys():
        print key, nextBranch[key]

def findNextNodes(dataframe, root):
    dfs = dict(tuple(dataframe.groupby(root)))
    nextBranch = {}
    for attr in dataframe[root].unique():
        del dfs[attr]['Day']
        del dfs[attr][root]
        attributes = {}
        for column in dfs[attr]:
            if column == 'Decision':
                pass
            else:
                attributes[column] = (calcInfoGain(column, dfs[attr]))
        nextBranch[attr] = attributes
    for key in nextBranch.keys():
        print key, nextBranch[key]
    return nextBranch


main()
