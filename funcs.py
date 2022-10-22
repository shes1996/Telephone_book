def delete_contact(line, TelBook : dict):
    if line[0] in TelBook.keys():
        TelBook.pop(line[0])
        return True
    return False

def add_tel(line, TelBook : dict):
    if line[0] in TelBook.keys():
        for x in line[1].split():
            if x in TelBook[line[0]]:
                return 2
        TelBook[line[0]].append(*line[1].split())
        return 0
    return 1

def new_contact(line, TelBook : dict):
    if line[0] not in TelBook.keys():
        TelBook[line[0]] = list(line[1].split())
        return True
    return False


def change_tel(line, TelBook : dict):
    if line[0] in TelBook.keys():
        TelBook[line[0]] = list(line[1].split())
        return True
    return False
