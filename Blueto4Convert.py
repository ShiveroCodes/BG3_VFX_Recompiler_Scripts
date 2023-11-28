import xml.etree.ElementTree as ET
import os
import colorsys

def change_color(input_file_name, target_color, hue_shift):
    new_file_name = input_file_name.replace("Blue", target_color)
    
    tree = ET.parse(input_file_name)
    root = tree.getroot()

    for frame_node in root.findall(".//node[@id='Frames']/children/node[@id='Frame']/attribute[@id='Color']"):
        color_attribute = frame_node.get('value')
        if color_attribute:
            r, g, b, a = map(float, color_attribute.split())
            h, l, s = colorsys.rgb_to_hls(r, g, b)
            new_h = (h * 360 + hue_shift) % 360 / 360
            new_r, new_g, new_b = colorsys.hls_to_rgb(new_h, l, s)
            frame_node.set('value', f"{new_r:.6f} {new_g:.6f} {new_b:.6f} {a}")

    tree.write(new_file_name, xml_declaration=True, encoding='utf-8')
    print(f"Datei für {target_color} wurde erstellt: {new_file_name}")

def process_directory(directory_path):
    hue_shifts = {
        "Red": 145,
        "Green": -120,
        "Purple": 30,
        "Yellow": -180,
    }
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".lsfx.lsx") and "Blue" in file_name:
            full_path = os.path.join(directory_path, file_name)
            for target_color, hue_shift in hue_shifts.items():
                change_color(full_path, target_color, hue_shift)

directory_path = os.path.dirname(__file__)
process_directory(directory_path)