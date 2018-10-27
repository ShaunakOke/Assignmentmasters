# Example of kNN implemented from Scratch in Python
# By Jason Brownlee
#http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

import csv
import random
import math
import operator
import matplotlib.pyplot as plt
import numpy as np
def loadDataset(filename, split, split2 ,trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for x in range((len(dataset)-1)):
			for y in range(4):
				dataset[x][y] = float(dataset[x][y])

		for x in range((len(dataset) - 1)):
			t=x*split
			if(t<(x*split2)):
				t=t
				testSet.append(dataset[x])
			else:
				trainingSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	dc = {}
	l = []
	l2 = []

	split =0.75
	for i in range(4):
		loadDataset('iris.csv', (0.2*i),0.2*i+0.2, trainingSet, testSet)
		print('Train set: ' + repr(len(trainingSet)))
		print('Test set: ' + repr(len(testSet)))
		# generate predictions
		predictions=[]
		k=19
		for x in range(len(testSet)):
			neighbors = getNeighbors(trainingSet, testSet[x], k)
			result = getResponse(neighbors)
			predictions.append(result)
			#print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
		accuracy = getAccuracy(testSet, predictions)
		print('Accuracy: ' + repr(accuracy) + '%'+'k:',k)
		#dc[split]=repr(accuracy)
		l.append(float(repr(accuracy)))
		print(l2)
		l2.append(i)
		#print(dc[split],split)


		plt.plot(l2,l,'-')
		#plt.axis([1,20,93,98])
		plt.show()

main()
