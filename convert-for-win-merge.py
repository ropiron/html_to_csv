from sys import argv
import os
from bs4 import BeautifulSoup
import csv
import subprocess

def main():
    for arg in argv[1:]:
        with open(arg, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            # テーブルを指定
            table = soup.find("table", {"class":"tree"})
            rows = table.find_all("tr")
            writer = csv.writer(f)
            path, ext = os.path.splitext(os.path.basename(arg))
            new_csv = path + ".csv"
            with open(new_csv, "w", encoding='utf-8') as file:
                writer = csv.writer(file)
                for row in rows:
                    csvRow = []
                    for cell in row.findAll(['td', 'th']):
                        csvRow.append(cell.get_text())
                        writer.writerow(csvRow)
    files = argv[1:]
    arg1 = os.path.splitext(os.path.basename(files[0]))[0]
    print('Compared')
    print(arg1 + '.csv')
    print('and')
    arg2 = os.path.splitext(os.path.basename(files[1]))[0]
    print(arg2 + '.csv')
    subprocess.call(['./WinMergeU.exe',arg1 + '.csv', arg2 + '.csv'])
    os.remove( arg1 + '.csv')
    os.remove( arg2 + '.csv')


if __name__ == "__main__":
    main()
