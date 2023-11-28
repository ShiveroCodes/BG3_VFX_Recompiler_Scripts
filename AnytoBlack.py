import xml.etree.ElementTree as ET
import os
import re

def change_color_to_black(input_file_name):
    color_names = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Brown", "Gray", "White"]
    
    # Replace the first occurrence of any color name with "Black"
    new_file_name = re.sub("|".join(color_names), "Black", input_file_name, flags=re.IGNORECASE)
    
    
    tree = ET.parse(input_file_name)
    root = tree.getroot()

    for frame_node in root.findall(".//node[@id='Frames']/children/node[@id='Frame']/attribute[@id='Color']"):
        # Set color to black (0 0 0)
        frame_node.set('value', "0.000000 0.000000 0.000000 1.0")

    tree.write(new_file_name, xml_declaration=True, encoding='utf-8')
    print(f"File has been created: {new_file_name}")

def process_directory(directory_path):
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".lsfx.lsx") and "Black" not in file_name:
            full_path = os.path.join(directory_path, file_name)
            change_color_to_black(full_path)

directory_path = os.path.dirname(__file__)
process_directory(directory_path)