#    print_file_on_screen(my_filename)
#        som öppnar filen med namnet my_filename (en sträng) och skriver ut innehållet på skärmen
#        Exempel på användning: print_file_on_screen("min_superfil.txt")

def print_file_on_screen(my_filename):
    with open(my_filename, "r") as file:
        content = file.read()
        print(content)

print_file_on_screen("min_superfil.txt")