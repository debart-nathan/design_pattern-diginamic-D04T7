from enum import Enum

# Définition de l'énumération pour les types d'éléments
class ElementType(Enum):
    INGREDIENT = "ingrédient"
    ALLERGENE = "allergène"
    ADDITIF = "additif"

# Définition de l'énumération pour les unités
class Unit(Enum):
    MICRO_GRAMME = "microgramme"
    MILLI_GRAMME = "milligramme"

# Classe mère représentant un élément
class Element:
    def __init__(self, name, value, unit):
        self.name = name
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, Valeur: {self.value} {self.unit.value}"

# Classes représentant les différents types d'éléments
class Ingredient(Element):
    pass

class Allergene(Element):
    pass

class Additif(Element):
    pass

# La Factory qui retourne un élément en fonction du type
class ElementFactory:
    @staticmethod
    def create_element(element_type, name, value, unit):
        if element_type == ElementType.INGREDIENT:
            return Ingredient(name, value, unit)
        elif element_type == ElementType.ALLERGENE:
            return Allergene(name, value, unit)
        elif element_type == ElementType.ADDITIF:
            return Additif(name, value, unit)
        else:
            raise ValueError(f"Type d'élément non reconnu: {element_type}")

# Exemple d'utilisation
if __name__ == "__main__":
    ingredient = ElementFactory.create_element(ElementType.INGREDIENT, "Tomate", 100, Unit.MILLI_GRAMME)
    allergene = ElementFactory.create_element(ElementType.ALLERGENE, "Gluten", 0.5, Unit.MICRO_GRAMME)
    additif = ElementFactory.create_element(ElementType.ADDITIF, "Conservateur", 0.1, Unit.MILLI_GRAMME)

    print(ingredient)
    print(allergene)
    print(additif)
