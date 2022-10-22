import csv

def ReadTelBook(name_file : str) -> dict:
    global dict
    dict = {}
    with open(name_file, 'r', newline='', encoding="utf-8") as csvfile:
        for line in csv.reader(csvfile, delimiter=';'):
            dict[line[0]] = list(line[1].split())
    return dict


def WriteTelBook(TelBook: dict):
    with open("telBook.csv", 'w', newline='', encoding="utf-8") as csvfile:
        for key in TelBook:
            out = csv.writer(csvfile, delimiter=';')
            out.writerow([key, str_out(TelBook[key])])


def str_out(lst:list)-> str:
    return ' '.join(lst)