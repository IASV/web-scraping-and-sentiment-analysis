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
    lines = contents.splitlines()
    new_data = []
    text = []
    isUser = False

    for line in lines:
        if len(text) > 0 and isUser:
            new_data.append({"user": user, "data": text})
            isUser = False

        # print(line)
        if R'";"' in str(line):
            print(line)
            isUser = True
            user = line
            text = []
        if (
            R"\"'" not in str(line)
            and R'";"' not in str(line)
            and R';"' not in str(line)
            and R'"' not in str(line)
            and R";user;comment" not in str(line)
        ):
            print(line)
            analyzer.setTextAnalizer(str(line))
            if len(str(line)) >= 512:
                text.append({"text": line, "analysis": f"invalid lenght characters"})
            else:
                text.append({"text": line, "analysis": analyzer.getSentimentAnalizer()})

    return new_data


@app.post("/")
async def text_sentiment_analyze(dato: Dato):
    analyzer.setTextAnalizer(dato.mensaje)
    return analyzer.getSentimentAnalizer()
