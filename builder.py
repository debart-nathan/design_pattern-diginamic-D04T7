# Classe Categorie
class Categorie:
    def __init__(self, nom: str):
        self.nom = nom

    def __repr__(self):
        return f"Categorie(nom={self.nom!r})"

# Classe Element
class Element:
    def __init__(self, name: str, value: float, unit: str):
        self.name = name
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, Valeur: {self.value} {self.unit}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, value={self.value}, unit={self.unit!r})"

# Classe Additif
class Additif(Element):
    def __init__(self, nom: str, qt_milligrammes: float):
        super().__init__(nom, qt_milligrammes, "mg")

# Classe Marque
class Marque:
    def __init__(self, nom: str):
        self.nom = nom

    def __repr__(self):
        return f"Marque(nom={self.nom!r})"

# Classe Ingredient
class Ingredient(Element):
    def __init__(self, nom: str, qt_milligrammes: float):
        super().__init__(nom, qt_milligrammes, "mg")

# Classe Allergene
class Allergene(Element):
    def __init__(self, nom: str, qt_milligrammes: float):
        super().__init__(nom, qt_milligrammes, "mg")

# Classe Produit
class Produit:
    def __init__(self, nom: str, grade: str, categorie: Categorie, 
                 additifs: list[Additif], marque: Marque, 
                 ingredients: list[Ingredient], allergenes: list[Allergene]):
        self.nom = nom
        self.grade = grade
        self.categorie = categorie
        self.additifs = additifs
        self.marque = marque
        self.ingredients = ingredients
        self.allergenes = allergenes

    def __str__(self):
        return (f"Produit(nom={self.nom}, grade={self.grade}, "
                f"categorie={self.categorie.nom}, "
                f"additifs={[str(additif) for additif in self.additifs]}, "
                f"marque={self.marque.nom}, "
                f"ingredients={[str(ingredient) for ingredient in self.ingredients]}, "
                f"allergenes={[str(allergene) for allergene in self.allergenes]})")

    def __repr__(self):
        return (f"Produit(nom={self.nom!r}, grade={self.grade!r}, "
                f"categorie={repr(self.categorie)}, "
                f"additifs={repr(self.additifs)}, "
                f"marque={repr(self.marque)}, "
                f"ingredients={repr(self.ingredients)}, "
                f"allergenes={repr(self.allergenes)})")


# Classe ProduitBuilder
class ProduitBuilder:
    def __init__(self):
        self.nom: str | None = None
        self.grade: str | None = None
        self.categorie: Categorie | None = None
        self.additifs: list[Additif] = []
        self.marque: Marque | None = None
        self.ingredients: list[Ingredient] = []
        self.allergenes: list[Allergene] = []

    def set_nom(self, nom: str):
        self.nom = nom
        return self

    def set_grade(self, grade: str):
        self.grade = grade
        return self

    def set_categorie(self, nom: str):
        self.categorie = Categorie(nom)
        return self

    def add_additif(self, nom: str, qt_milligrammes: float):
        self.additifs.append(Additif(nom, qt_milligrammes))
        return self

    def set_marque(self, nom: str):
        self.marque = Marque(nom)
        return self

    def add_ingredient(self, nom: str, qt_milligrammes: float):
        self.ingredients.append(Ingredient(nom, qt_milligrammes))
        return self

    def add_allergene(self, nom: str, qt_milligrammes: float):
        self.allergenes.append(Allergene(nom, qt_milligrammes))
        return self

    def build(self) -> Produit:
        if not all([self.nom, self.grade, self.categorie, self.marque, self.ingredients, self.allergenes]):
            raise ValueError("Tous les attributs doivent être définis")
        return Produit(self.nom, self.grade, self.categorie, 
                       self.additifs, self.marque, 
                       self.ingredients, self.allergenes)

# Exemple d'utilisation
if __name__ == "__main__":
    produit = (ProduitBuilder()
               .set_nom("Chips Salees")
               .set_grade("A")
               .set_categorie("Snacks")
               .add_additif("Conservateur", 50.0)
               .set_marque("SnackCo")
               .add_ingredient("Chips de pomme de terre", 200.0)
               .add_allergene("Gluten", 20.00)
               .build())
    
    print(produit)
