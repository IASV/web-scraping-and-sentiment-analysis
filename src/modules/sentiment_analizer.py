#core
from transformers import pipeline

class SentimentAnalizer:
    def __init__(self):
        self.text = ""
        self.task = "text-classification"
        self.model = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"
        self.classifier = pipeline(self.task, self.model)
    
    def setTextAnalizer(self, text):
        self.text = text

    def getSentimentAnalizer(self):
        return self.classifier(self.text) 