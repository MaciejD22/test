# Napisz program który pyta użytkownika o wiek. Jeśli wiek użytkownika jest mniejszy od 18
# niech program wyświetli komunikat "Strona tylko dla osób pełnletnich! Nie możesz wejść."
#
# Jeśli użytkownik ma więcej jak 18 lat niech wyświetli komunikt "Zapraszamy"

wiek = int(input("Podaj swój wiek: "))
if wiek < 18: print("Strona tylko dla osób pełnoletnich! Nie możesz wejść")
if wiek >= 18: print("Zapraszamy")