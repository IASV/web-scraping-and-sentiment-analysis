# core
from datetime import datetime
from os import getcwd, path
import requests
from bs4 import BeautifulSoup
import pandas as pd


class Scraper:
    def __init__(self, base_url, html_component, class_name):
        self.base_url = base_url
        self.html_component = html_component
        self.class_name = class_name
        self.extract_data = []

    def getData(self):
        res = requests.get(self.base_url)
        soup = BeautifulSoup(res.text, "html.parser")
        content = soup.find_all(self.html_component, class_=self.class_name)

        print(f"Pagina #1 {self.base_url}")
        print("Fin del scraping")

        for post in content:
            user = post.find(class_="comment-author vcard").text
            comment = post.find(class_="comment-content").text
            self.extract_data.append({"user": user, "comment": comment})

    def export_to_csv(self):
        data_frame = pd.DataFrame(self.extract_data)
        doc_name = f"{datetime.now()}.csv"
        doc_path = path.join(getcwd(), "src", "documents", doc_name)
        data_frame.to_csv(doc_path, sep=";")

        return {"path": doc_path, "file_name": doc_name}


if __name__ == "__main__":
    scraper = Scraper("https://red.infd.edu.ar/foros/", "li", "comment")
    scraper.getData()
    scraper.export_to_csv()
