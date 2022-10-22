import csv
import funcs


def changeTelBook(name_file : str, TelBook : dict) -> None:
    with open(name_file, newline='') as csvfile:
        for line in csv.reader(csvfile, delimiter=';'):
            if line[2] == "delete":
                flag = funcs.delete_contact(line, TelBook)
                if flag is False:
                    print(*line, ': Contact not found')
            if line[2] == "add":
                flag = funcs.add_tel(line, TelBook)
                if flag == 1:
                    print(*line, ': Contact not found')
                if flag == 2:
                    print(*line, ': One of this numbers already exists')
            if line[2] == "new":
                flag = funcs.new_contact(line, TelBook)
                if flag is False:
                    print(*line, ': Contact already exists')
            if line[2] == "change":
                flag = funcs.change_tel(line, TelBook)
                if flag is False:
                    print(*line, ': Contact not found')



