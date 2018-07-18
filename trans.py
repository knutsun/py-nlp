#-*- coding: utf-8 -*-

from google.cloud import translate

def translateText(text, target='en'):
	translateClient = translate.Client()
	output = translateClient.translate(text, target_language=target)
	print(output['translatedText'])
# 	print('Text: ', output['input'])
# 	print('Translation: ', output['translatedText'])
# 	# print('Detected source language: ', output['detectedSourceLanguage'])


# # inputText = input("What to translate?: ")
# # outputText = translateText(inputText)
# print(outputText)