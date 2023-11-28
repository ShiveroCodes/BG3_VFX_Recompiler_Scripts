import xml.etree.ElementTree as ET
import os
import colorsys

def is_grey_scale(r, g, b):
    return 0.2 <= r <= 1 and r == g == b

def get_target_rgb(color_name):
    colors = {
        "Blue": (0, 0, 1),   # RGB for Blue
        "Red": (1, 0, 0),    # RGB for Red
        "Green": (0, 1, 0),  # RGB for Green
        "Purple": (0.5, 0, 0.5)  # RGB for Purple
    }
    return colors.get(color_name, (1, 1, 1))  # Default to white if color not found

def change_color(input_file_name):
    tree = ET.parse(input_file_name)
    root = tree.getroot()

    color_name = input_file_name.split('.')[0]  # Assuming the color name is part of the file name
    target_rgb = get_target_rgb(color_name)

    for frame_node in root.findall(".//node[@id='Frames']/children/node[@id='Frame']/attribute[@id='Color']"):
        color_attribute = frame_node.get('value')
        if color_attribute:
            r, g, b, a = map(float, color_attribute.split())
            if is_grey_scale(r, g, b):
                new_r, new_g, new_b = target_rgb
                frame_node.set('value', f"{new_r:.6f} {new_g:.6f} {new_b:.6f} {a}")

    tree.write(input_file_name, xml_declaration=True, encoding='utf-8')
    print(f"File has been updated: {input_file_name}")

def process_directory(directory_path):
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".lsfx.lsx"):
            full_path = os.path.join(directory_path, file_name)
            change_color(full_path)

directory_path = os.path.dirname(__file__)
process_directory(directory_path)