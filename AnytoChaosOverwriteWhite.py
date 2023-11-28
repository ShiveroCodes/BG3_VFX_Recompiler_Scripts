import xml.etree.ElementTree as ET
import os
import random
import re

def change_color(input_file_name):
    # Define a list of color names that might appear in the file name
    color_names = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Brown", "Gray", "White", "Black"]
    
    # Use a regular expression to find a color name in the file name
    color_name_match = re.search("|".join(color_names), input_file_name, re.IGNORECASE)
    
    # If a color name is found, replace it with "Chaos"
    if color_name_match:
        new_file_name = re.sub(color_name_match.group(), "Chaos", input_file_name, flags=re.IGNORECASE)
    else:
        base_name, ext = os.path.splitext(input_file_name)
        new_file_name = f"{base_name}_Chaos{ext}"
    
    tree = ET.parse(input_file_name)
    root = tree.getroot()

    # Define the possible replacement colors as RGB tuples
    replacement_colors = [
        (1, 0, 0), (1, 1, 0), (0, 1, 0),
        (0, 1, 1), (1, 0, 1), (0, 0, 1)
    ]

    for frame_node in root.findall(".//node[@id='Frames']/children/node[@id='Frame']/attribute[@id='Color']"):
        color_attribute = frame_node.get('value')
        if color_attribute:
            r, g, b, a = map(float, color_attribute.split())
            # Check if the color is white
            if r == 1 and g == 1 and b == 1:
                # Pick a random replacement color
                new_r, new_g, new_b = random.choice(replacement_colors)
                frame_node.set('value', f"{new_r} {new_g} {new_b} {a}")

    tree.write(new_file_name, xml_declaration=True, encoding='utf-8')
    print(f"File has been created: {new_file_name}")

def process_directory(directory_path):
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".lsfx.lsx") and "Chaos" not in file_name:
            full_path = os.path.join(directory_path, file_name)
            change_color(full_path)

directory_path = os.path.dirname(__file__)
process_directory(directory_path)
