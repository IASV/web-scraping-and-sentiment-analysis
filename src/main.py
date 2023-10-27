# core
from fastapi import FastAPI, UploadFile

# script
from src.modules.sentiment_analizer import SentimentAnalizer
from src.modules.web_scraping import Scraper

# models
from src.models.sentiment_analyzer import Dato

app = FastAPI()
analyzer = SentimentAnalizer()
scraper = Scraper("https://red.infd.edu.ar/foros/", "li", "comment")


@app.get("/")
async def root():
    return {"messaje": "Hola mundo"}


@app.get("/scraping")
async def get_data_scraping():
    scraper.getData()
    return scraper.export_to_csv()


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    contents = await file.read()
    return contents.splitlines()


@app.post("/")
async def text_sentiment_analyze(dato: Dato):
    analyzer.setTextAnalizer(dato.mensaje)
    return analyzer.getSentimentAnalizer()
