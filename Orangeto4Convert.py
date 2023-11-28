import xml.etree.ElementTree as ET
import os
import colorsys

def change_color(input_file_name, target_color, hue_shift):
    new_file_name = input_file_name.replace("Orange", target_color)
    
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
    print(f"File for {target_color} has been created: {new_file_name}")

def process_directory(directory_path):
    # Assuming the fiery orange hue is around 30 degrees
    # The hue_shifts here are examples, you will need to adjust these values
    # based on the exact color you wish to achieve from your fiery orange base
    hue_shifts = {
        "Blue": 180,  # Shift from orange to blue
        "Red": 330,   # Shift from orange to red
        "Green": 90,  # Shift from orange to green
        "Purple": 270,  # Shift from orange to purple
    }
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".lsfx.lsx") and "Orange" in file_name:
            full_path = os.path.join(directory_path, file_name)
            for target_color, hue_shift in hue_shifts.items():
                change_color(full_path, target_color, hue_shift)

directory_path = os.path.dirname(__file__)
process_directory(directory_path)
