class Animalia:
    def __init__(self):
        self.kingdom = 'Animalia'

    def __str__(self):
        return 'Kingdom: ' + self.kingdom


class Porifera(Animalia):
    def __init__(self):
        super().__init__()
        self.phylum = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nPhylum: ' + self.phylum


class Cnidaria(Animalia):
    def __init__(self):
        super().__init__()
        self.phylum = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nPhylum: ' + self.phylum


class Platyhelminthes(Animalia):
    def __init__(self):
        super().__init__()
        self.phylum = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nPhylum: ' + self.phylum


class Nematoda(Animalia):
    def __init__(self):
        super().__init__()
        self.phylum = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nPhylum: ' + self.phylum


class Annelida(Animalia):
    def __init__(self):
        super().__init__()
        self.phylum = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nPhylum: ' + self.phylum


class Arthropoda(Animalia):
    def __init__(self):
        super().__init__()
        self.phylum = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nPhylum: ' + self.phylum


class Mollusca(Animalia):
    def __init__(self):
        super().__init__()
        self.phylum = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nPhylum: ' + self.phylum


class Echinodermata(Animalia):
    def __init__(self):
        super().__init__()
        self.phylum = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nPhylum: ' + self.phylum


class Chordata(Animalia):
    def __init__(self):
        super().__init__()
        self.phylum = 'Chordata'

    def __str__(self):
        return super().__str__() + '\nPhylum: ' + self.phylum


class Urochordata(Chordata):
    def __init__(self):
        super().__init__()
        self.subphylum = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nSub Phylum: ' + self.subphylum


class Cephalochordata(Chordata):
    def __init__(self):
        super().__init__()
        self.subphylum = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nSub Phylum: ' + self.subphylum


class Vertebrata(Chordata):
    def __init__(self):
        super().__init__()
        self.subphylum = 'Vertebrata'

    def __str__(self):
        return super().__str__() + '\nSub Phylum: ' + self.subphylum


class Cyclostomata(Vertebrata):
    def __init__(self):
        super().__init__()
        self._class = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nClass: ' + self._class


class Chondrichthyes(Vertebrata):
    def __init__(self):
        super().__init__()
        self._class = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nClass: ' + self._class


class Osteichthyes(Vertebrata):
    def __init__(self):
        super().__init__()
        self._class = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nClass: ' + self._class


class Amphibia(Vertebrata):
    def __init__(self):
        super().__init__()
        self._class = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nClass: ' + self._class


class Reptilia(Vertebrata):
    def __init__(self):
        super().__init__()
        self._class = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nClass: ' + self._class


class Aves(Vertebrata):
    def __init__(self):
        super().__init__()
        self._class = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nClass: ' + self._class


class Mammalia(Vertebrata):
    def __init__(self):
        super().__init__()
        self._class = self.__class__.__name__

    def __str__(self):
        return super().__str__() + '\nClass: ' + self._class
