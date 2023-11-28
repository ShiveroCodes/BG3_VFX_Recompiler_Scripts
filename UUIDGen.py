import uuid

# Funktion zum Erstellen einer UUID und Konvertierung in einen String
def create_uuid():
    return str(uuid.uuid4())

# Hauptfunktion, die 200 UUIDs generiert und in einer Datei speichert
def save_uuids_to_file(file_name, number_of_uuids):
    with open(file_name, 'w') as file:
        for _ in range(number_of_uuids):
            file.write(create_uuid() + '\n')

# Setze den Namen der Datei und die Anzahl der zu generierenden UUIDs
file_name = 'uuids.txt'
number_of_uuids = 200

# Führe die Hauptfunktion aus
save_uuids_to_file(file_name, number_of_uuids)

print(f"{number_of_uuids} UUIDs wurden in '{file_name}' gespeichert.")