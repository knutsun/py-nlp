import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import FreqDist
from nltk.tokenize import *
from nltk.corpus import stopwords
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import nlp

def inputFile(textFile):

	filenames = os.listdir("C:\\Users\\tristans\\Development\\python\\texts")
	pathname = os.path.join("C:\\Users\\tristans\\Development\\python\\texts", textFile)
	f = open(pathname, "r+", encoding="utf-8")
	inputfile = f.read()

	return inputfile

def displayFiles():
	filenames = os.listdir("texts")

	return filenames


def metrics(fileObj):
	fileObj = fileObj.lower()
	numberOfSentences = 0
	numberOfWords = 0
	for i in sent_tokenize(fileObj):
		numberOfSentences = numberOfSentences+1
	print('Number of sentences = ' + str(numberOfSentences))
	for i in word_tokenize(fileObj):
		numberOfWords = numberOfWords+1
	print('Number of words = ' + str(numberOfWords))
	averageTimeToRead = 4.166 # 300 wpm
	secondsToRead = numberOfWords / averageTimeToRead
	minutesToRead = secondsToRead / 60
	hoursToRead = minutesToRead / 60
	print('Seconds to read text = ' + str(round(int(secondsToRead))))
	print('Minutes to read text = ' + str(round(int(minutesToRead))))
	print('Hours to read text = ' + str(round(hoursToRead, 2)))
