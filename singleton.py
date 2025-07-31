import re
import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()
    

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
                    cls._instance.init = False
        return cls._instance

    def __init__(self, fichier_config='configuration.ini'):
        if not self.init:
            self._config_data= {}
            self.charger_fichier(fichier_config)
            self.init = True

    def charger_fichier(self, fichier_config: str) -> None:
        try:
            with open(fichier_config, "r") as f:
                content = f.read()
                
                # Remove multiline strings
                content = re.sub(r'(?s)""".*?"""|\'\'\'.*?\'\'\'', '', content)

                # Process each line
                for ligne in content.splitlines():
                    ligne = ligne.strip()
                    if ligne:
                        # Split at the first '#' to ignore comments outside of strings
                        if not self._is_inside_string(ligne):
                            ligne = ligne.split('#', 1)[0].strip()
                        if '=' in ligne:
                            key, value = ligne.split('=', 1)
                            self._config_data[key.strip()] = value.strip()
        except FileNotFoundError:
            print(f"Le fichier {fichier_config} n'a pas été trouvé.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")

    def _is_inside_string(self, ligne: str) -> bool:
        """Check if the '#' character is inside a string."""
        in_single_quote = False
        in_double_quote = False
        for char in ligne:
            if char == "'" and not in_double_quote:
                in_single_quote = not in_single_quote
            elif char == '"' and not in_single_quote:
                in_double_quote = not in_double_quote
            elif char == '#' and not (in_single_quote or in_double_quote):
                return False
        return True

    def get(self, key):
        return self._config_data.get(key, None)

# Exemple d'utilisation
if __name__ == "__main__":
    singleton1 = Singleton()
    print(singleton1.get('db.url'))  # Affiche l'URL de la base de données

    singleton2 = Singleton()
    print(singleton2.get('db.user'))  # Affiche l'utilisateur de la base de données

    print(singleton1 is singleton2)  # Affiche True, prouvant que c'est le même objet
