import os

from traitementDeDonnee import get_file_name, isExisteFile, isEmptyFile, checkDataNumberForEachLine, process_client_data

# Chemin du fichier client.txt utilisé pour les tests
CLIENT_FILE_PATH = "./client.txt"

# Tests pour la fonction get_file_name
def test_get_file_name():
    file_path = "./client.txt"
    expected_file_name = "client.txt"
    assert get_file_name(file_path) == expected_file_name

# Tests pour la fonction isExisteFile
def test_isExisteFile_existing_file():
    assert isExisteFile(CLIENT_FILE_PATH) == True

def test_isExisteFile_non_existing_file():
    assert isExisteFile("path/to/non_existing_file.txt") == False

# Tests pour la fonction isEmptyFile
def test_isEmptyFile_empty_file(tmp_path):
    empty_file_path = os.path.join(tmp_path, "empty_file.txt")
    with open(empty_file_path, "w"):
        pass  # Crée un fichier vide
    assert isEmptyFile(empty_file_path) == True

def test_isEmptyFile_non_empty_file(tmp_path):
    non_empty_file_path = os.path.join(tmp_path, "non_empty_file.txt")
    with open(non_empty_file_path, "w") as file:
        file.write("Some data")  # Crée un fichier non vide
    assert isEmptyFile(non_empty_file_path) == False

# Tests pour la fonction checkDataNumberForEachLine
def test_checkDataNumberForEachLine():
    assert checkDataNumberForEachLine(CLIENT_FILE_PATH) == True

# Tests pour la fonction process_client_data
def test_process_client_data(tmp_path):
    # Crée un fichier client.txt avec des données de test
    client_file_path = os.path.join(tmp_path, "./client.txt")
    with open(client_file_path, "w") as file:
        file.write("01,Frederic,Masson,12 rue de la république 69002\n")
        file.write("02,Arthur,Durant,11 rue de la paix 75002\n")
    
    # Appelle la fonction process_client_data avec le fichier créé
    processed_data = process_client_data(client_file_path)

    # Vérifie si les données traitées correspondent aux données attendues
    expected_data = [
        ('01', 'Frederic', 'Masson', '12 rue de la république 69002'),
        ('02', 'Arthur', 'Durant', '11 rue de la paix 75002')
    ] 

    assert processed_data == expected_data