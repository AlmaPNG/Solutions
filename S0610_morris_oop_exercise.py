"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Genbrug din oprindelige Morris-kode og omskriv den til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""



class Miner:
    def __init__(self, sleepiness, thirst, hunger, whisky, gold):
        self.sleepiness = sleepiness
        self.thirst = thirst
        self.hunger = hunger
        self.whisky = whisky
        self.gold = gold
        self.turn = 0

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hunger -= 20
        self.gold -= 2

    def buy_whisky(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.whisky += 1
        self.gold -= 1

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hunger -= 1
        self.whisky -= 1

    def dead(self):
        return self.sleepiness > 100 or self.thirst > 100 or self.hunger > 100

    def check_boundaries(self):
        self.sleepiness = max(0, self.sleepiness)
        self.thirst = max(0, self.thirst)
        self.hunger = max(0, self.hunger)
        self.whisky = max(0, min(10, self.whisky))
        self.gold = max(0, self.gold)

    def __str__(self):
        return f"Turn: {self.turn}, Gold: {self.gold}, Sleepiness: {self.sleepiness}, Thirst: {self.thirst}, Hunger: {self.hunger}, Whisky: {self.whisky}"

    def choose_action(self):
        if self.sleepiness > 80:
            return self.sleep
        elif self.thirst > 80:
            if self.whisky > 0:
                return self.drink
            elif self.gold > 0:
                return self.buy_whisky
        elif self.hunger > 80:
            if self.gold >= 2:
                return self.eat
        return self.mine


morris = Miner(0, 0, 0, 0, 0)
while not morris.dead() and morris.turn < 1000:
    morris.turn += 1
    action = morris.choose_action()
    action()
    morris.check_boundaries()
    print(morris)