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

def print_menu():
	print ("MENU\n\n")
	print ("0. set file")
	print ("1. display set file")
	print ("2. display files")
	print ("3. metrics")
	print ("4. commons")
	print("\n")

loop=True

while loop:
	os.system('cls')
	print_menu()
	choice = input("Make selection: ")

	if choice=='0':	
		os.system('cls')
		textFile = input("Enter name of text file: ")
		fileObj = nlp.inputFile(textFile)

	elif choice=='1':
		os.system('cls')
		print(fileObj)
		input("Press Enter to continue")

	elif choice=='2':
		os.system('cls')
		files = nlp.displayFiles()
		print(files)
		print("\n")
		input("Press Enter to continue")

	elif choice=='3':
		os.system('cls')
		metrics = nlp.metrics(fileObj)	
		print("\n")
		input("Press Enter to continue")

	elif choice=='4':
		os.system('cls')
		metrics = nlp.commons(fileObj)	
		print("\n")
		input("Press Enter to continue")

	elif choice=='5':
		os.system('cls')
		# translation = nlp.translate(fileObj)	
		# print("\n")
		# print(translation)
		nlp.translate()
		input("Press Enter to continue")


	else:
		input("Invalid. Try again: ")