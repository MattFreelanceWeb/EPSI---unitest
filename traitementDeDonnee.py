import os

def get_file_name(file_path):
    """
    Renvoie le nom du fichier à partir du chemin complet du fichier.
    
    Args:
        file_path (str): Le chemin complet du fichier.
    
    Returns:
        str: Le nom du fichier.
    """
    return os.path.basename(file_path)

def isExisteFile(file_path):
    """
    Vérifie si le fichier existe dans le chemin spécifié.
    
    Args:
        file_path (str): Le chemin complet du fichier.
    
    Returns:
        bool: True si le fichier existe, False sinon.
    """
    return os.path.exists(file_path)

def isEmptyFile(file_path):
    """
    Vérifie si le fichier spécifié est vide.
    
    Args:
        file_path (str): Le chemin complet du fichier.
    
    Returns:
        bool: True si le fichier est vide, False sinon.
    """
    return os.path.exists(file_path) and os.path.getsize(file_path) == 0

def checkDataNumberForEachLine(file_path):
    """
    Vérifie si chaque ligne du fichier a le bon nombre de données.
    
    Args:
        file_path (str): Le chemin complet du fichier.
    
    Returns:
        bool: True si toutes les lignes ont le bon nombre de données, False sinon.
    """
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if len(data) != 4:  # Vérifie si le nombre d'éléments sur chaque ligne n'est pas égal à 4
                return False
    return True

def process_client_data(file_path):
    """
    Traite les données des clients à partir du fichier spécifié.
    
    Args:
        file_path (str): Le chemin complet du fichier contenant les données des clients.
    
    Returns:
        list: Une liste de tuples contenant les données des clients valides à insérer dans la base de données.
    """
    valid_client_data = []

    with open(file_path, 'r') as file:
        for line in file:
            # Affiche la ligne lue à partir du fichier
            print("Ligne lue à partir du fichier:", line)
            # Parse les données de chaque ligne
            client_info = line.strip().split(',')
            print("Données parsées:", client_info)  # Affiche les données après le split
            if checkDataNumberForEachLine(file_path) :
            # Si le nombre de données est correct, ajoute les données à la liste des données valides
                valid_client_data.append(tuple(client_info))

    return valid_client_data


# # Exemple d'utilisation

print("number",checkDataNumberForEachLine("./client.txt"))

if __name__ == "__main__":
    client_data_file = "./client.txt"
    clients_to_insert = process_client_data(client_data_file)
    print(" client to insert:", clients_to_insert)