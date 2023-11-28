import xml.etree.ElementTree as ET
import os
import re

def change_color(input_file_name):
    # Replace original color name with 'White' in the file name
    new_file_name = re.sub(r'(Red|Green|Blue|Yellow|Purple|Orange|Pink|Brown|Gray)', 'White', input_file_name, flags=re.IGNORECASE)
    
    tree = ET.parse(input_file_name)
    root = tree.getroot()

    for frame_node in root.findall(".//node[@id='Frames']/children/node[@id='Frame']/attribute[@id='Color']"):
        color_attribute = frame_node.get('value')
        if color_attribute:
            # Overwrite every color with white (1, 1, 1)
            frame_node.set('value', "1.000000 1.000000 1.000000 1.000000")

    tree.write(new_file_name, xml_declaration=True, encoding='utf-8')
    print(f"File has been created: {new_file_name}")

def process_directory(directory_path):
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".lsfx.lsx"):
            full_path = os.path.join(directory_path, file_name)
            change_color(full_path)

directory_path = os.path.dirname(__file__)
process_directory(directory_path)