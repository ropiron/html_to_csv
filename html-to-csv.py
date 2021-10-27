from sys import argv
import os
from pathlib import Path
from bs4 import BeautifulSoup
import csv

def main():
    for arg in argv[1:]:
        with open(arg, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            # テーブルを指定
            table = soup.find("table", {"class":"tree"})
            rows = table.find_all("tr")
            writer = csv.writer(f)
            path, ext = os.path.splitext(os.path.basename(arg))
            new_csv = path + (".csv")
            with open(new_csv, "w", encoding='utf-8') as file:
                writer = csv.writer(file)
                for row in rows:
                    csvRow = []
                    for cell in row.findAll(['td', 'th']):
                        csvRow.append(cell.get_text())
                        writer.writerow(csvRow)

if __name__ == "__main__":
    main()
