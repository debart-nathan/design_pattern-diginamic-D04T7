import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()
    

    def __new__(cls):
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

    def charger_fichier(self, fichier_config):
        try:
            with open(fichier_config, "r") as f:
                for ligne in f:
                    ligne = ligne.strip()
                    if ligne and '=' in ligne:
                        key, value = ligne.split('=', 1)
                        self._config_data[key.strip()] = value.strip()
        except FileNotFoundError:
            print(f"Le fichier {fichier_config} n'a pas été trouvé.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")

    def get(self, key):
        return self._config_data.get(key, None)

# Exemple d'utilisation
if __name__ == "__main__":
    singleton1 = Singleton()
    print(singleton1.get('db.url'))  # Affiche l'URL de la base de données

    singleton2 = Singleton()
    print(singleton2.get('db.user'))  # Affiche l'utilisateur de la base de données

    print(singleton1 is singleton2)  # Affiche True, prouvant que c'est le même objet
