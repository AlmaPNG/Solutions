"""
Opgave "Reading from a file":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Opret en tekstfil med en editor efter eget valg (pycharm, notepad, notepad++ osv.)
Hver række skal bestå af en persons navn efterfulgt af et mellemrum og et tal, der repræsenterer personens alder.
gem filen i din løsningsmappe

Skriv et program, der læser filen til en liste af strings.
Derefter brug indholdet af hver string til at udskrive en række som f.eks:
    <navn> er <alder> år gammel.

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

minData = ["Mario 30\n", "Luigi 29\n", "Peach 30\n", "Toad 1\n"]  # this is a list of strings
minFil = "S0166_input.txt"  # the name of the file.

with open(minFil, "w") as file:
    for line in minData:
        file.write(line)

with open(minFil, "r") as file:
    for line in file:
        name, age = line.split()
        print(f"{name} er {age} år gammel")