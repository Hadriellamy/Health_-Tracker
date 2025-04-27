 # Fonctions utilitaires

from datetime import datetime


def is_valid_date(date_str):
    """Vérifie si une chaîne de caractères est une date au format YYYY-MM-DD."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def input_int(prompt, min_val=0, max_val=None):
    """Demande à l'utilisateur un entier dans un intervalle donné."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_val or (max_val is not None and value > max_val):
                print("Valeur hors limites.")
                continue
            return value
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.")

def input_float(prompt, min_val=0.0, max_val=None):
    """Demande à l'utilisateur un flottant dans un intervalle donné."""
    while True:
        try:
            value = float(input(prompt))
            if value < min_val or (max_val is not None and value > max_val):
                print("Valeur hors limites.")
                continue
            return value
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre décimal.")




# Explications 

"""
is_valid_date("2024-08-01") : permet de vérifier les dates.
input_int("Nombre de pas : ") : pour éviter les bugs quand l’utilisateur tape n’importe quoi.
input_float("Heures de sommeil : ") : pour sécuriser les saisies utilisateurs.

"""