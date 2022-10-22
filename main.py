import fileWork as fW
from telBook import changeTelBook

# delete, add, new, change (все удаляем, добавляем новый)
TelBook = fW.ReadTelBook("telBook.csv")
changeTelBook("input.csv", TelBook)
fW.WriteTelBook(TelBook)
