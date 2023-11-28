import xml.etree.ElementTree as ET
import os
import colorsys

def make_necrotic(input_file_name, output_suffix="_necrotic"):
    new_file_name = os.path.splitext(input_file_name)[0] + output_suffix + os.path.splitext(input_file_name)[1]
    
    tree = ET.parse(input_file_name)
    root = tree.getroot()

    for frame_node in root.findall(".//node[@id='Frames']/children/node[@id='Frame']/attribute[@id='Color']"):
        color_attribute = frame_node.get('value')
        if color_attribute:
            r, g, b, a = map(float, color_attribute.split())
            h, l, s = colorsys.rgb_to_hls(r, g, b)
            
            # Check if the color is white or a very light shade, then turn it to black.
            if s == 0 and l > 0.9:
                r, g, b = 0, 0, 0  # Black
            else:
                # Adjust the lightness and saturation to create a 'necrotic' green.
                # These values may need to be adjusted to fit your definition of 'necrotic'.
                if h > 0.22 and h < 0.45:  # Assuming this range captures greens
                    l *= 0.5  # Darken
                    s *= 0.5  # Desaturate

            new_r, new_g, new_b = colorsys.hls_to_rgb(h, l, s)
            frame_node.set('value', f"{new_r:.6f} {new_g:.6f} {new_b:.6f} {a}")

    tree.write(new_file_name, xml_declaration=True, encoding='utf-8')
    print(f"Necrotic file has been created: {new_file_name}")

def process_directory(directory_path):
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".lsfx.lsx"):
            full_path = os.path.join(directory_path, file_name)
            make_necrotic(full_path)

directory_path = os.path.dirname(__file__)
process_directory(directory_path)