# Classe Categorie
class Categorie:
    def __init__(self, nom: str):
        self.nom = nom

# Classe Additif
class Additif:
    def __init__(self, nom: str, qt_milligrammes: float):
        self.nom = nom
        self.qt_milligrammes = qt_milligrammes

# Classe Marque
class Marque:
    def __init__(self, nom: str):
        self.nom = nom

# Classe Ingredient
class Ingredient:
    def __init__(self, nom: str, qt_milligrammes: float):
        self.nom = nom
        self.qt_milligrammes = qt_milligrammes

# Classe Allergene
class Allergene:
    def __init__(self, nom: str, qt_milligrammes: float):
        self.nom = nom
        self.qt_milligrammes = qt_milligrammes  # Fixed typo here

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
                f"additifs={[additif.nom for additif in self.additifs]}, "
                f"marque={self.marque.nom}, "
                f"ingredients={[ingredient.nom for ingredient in self.ingredients]}, "
                f"allergenes={[allergene.nom for allergene in self.allergenes]})")

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

    def set_categorie(self, categorie: Categorie):
        self.categorie = categorie
        return self

    def add_additif(self, additif: Additif):
        self.additifs.append(additif)
        return self

    def set_marque(self, marque: Marque):
        self.marque = marque
        return self

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)
        return self

    def add_allergene(self, allergene: Allergene):
        self.allergenes.append(allergene)
        return self

    def build(self) -> Produit:
        if not all([self.nom, self.grade, self.categorie, self.marque, self.ingredients, self.allergenes]):
            raise ValueError("Tous les attributs doivent être définis")
        return Produit(self.nom, self.grade, self.categorie, 
                       self.additifs, self.marque, 
                       self.ingredients, self.allergenes)

# Exemple d'utilisation
if __name__ == "__main__":
    categorie = Categorie("Snacks")
    marque = Marque("SnackCo")
    additif1 = Additif("Conservateur", 50.0)
    ingredient1 = Ingredient("Chips de pomme de terre", 200.0)
    allergene1 = Allergene("Gluten", 20.00)

    produit = (ProduitBuilder()
               .set_nom("Chips Salees")
               .set_grade("A")
               .set_categorie(categorie)
               .add_additif(additif1)
               .set_marque(marque)
               .add_ingredient(ingredient1)
               .add_allergene(allergene1)
               .build())
    
    print(produit)
