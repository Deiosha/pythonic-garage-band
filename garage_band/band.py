class Band:

    def play_solos(self):
        play_solo = [member.play_solo() for member in self.members]
        return play_solo

    def __init__(self, name, members):
        self.name = name
        self.members = members


class Musician:

    def __init__(self, name, instrument, solo):
        self.name = name
        self.instrument = instrument
        self.solo = solo


class Musician:

    def __init__(self, name):
        self.name = name


class Guitarist(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return f'face melting guitar solo'


class Drummer(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def get_instrument(self):
        return 'drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    def play_solo(self):
        return f'rattle boom crash'


class Bassist(Musician):
    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def get_instrument(self):
        return 'bass'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    def play_solo(self):
        return f'bom bom buh bom'




if __name__ == "__main__":
    # joan = Guitarist("Joan Jett", "Guitar", "Solo")
    # print(joan.name)
    # print(joan.instrument)
    # sheila = Drummer("Sheila E.", "drums", "Solo")
    # print(sheila.name)
    # print(sheila.instrument)
    Meshell = Bassist("Meshell Ndegeocello", "Bassist", "Solo")
    print(Meshell.name)
