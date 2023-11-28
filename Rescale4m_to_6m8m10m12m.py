import xml.etree.ElementTree as ET
import os

def rescale_vfx(input_file_name, scale_factor, new_size_tag):
    new_file_name = input_file_name.replace("4m", new_size_tag)

    tree = ET.parse(input_file_name)
    root = tree.getroot()

    # Rescale radius in the Frames node
    for property_node in root.findall(".//node[@id='Property']"):
        attribute_name = property_node.find("attribute[@id='AttributeName']")
        if attribute_name is not None and attribute_name.get('value') == 'Radius':
            for frame_node in property_node.findall(".//node[@id='Frame']/attribute[@id='Value']"):
                radius_value = float(frame_node.get('value'))
                new_radius_value = radius_value * scale_factor
                frame_node.set('value', f"{new_radius_value:.6f}")

    # Rescale scale modifiers
    for scale_modifier_node in root.findall(".//node[@id='Property']"):
        attribute_name = scale_modifier_node.find("attribute[@id='AttributeName']")
        if attribute_name is not None and 'Scale Modifier' in attribute_name.get('value'):
            value_node = scale_modifier_node.find("attribute[@id='Value']")
            if value_node is not None:
                scale_value = float(value_node.get('value'))
                new_scale_value = scale_value * scale_factor
                value_node.set('value', f"{new_scale_value:.6f}")

    tree.write(new_file_name, xml_declaration=True, encoding='utf-8')
    print(f"File for {new_size_tag} created: {new_file_name}")

def process_directory_for_rescaling(directory_path):
    size_tags = ["6m", "8m", "10m", "12m"]
    scale_factors = [1.5, 2, 2.5, 3]  # 1.5^1, 1.5^2, 1.5^3, 1.5^4

    for file_name in os.listdir(directory_path):
        if file_name.endswith(".lsfx.lsx") and "4m" in file_name:
            full_path = os.path.join(directory_path, file_name)
            for new_size_tag, scale_factor in zip(size_tags, scale_factors):
                rescale_vfx(full_path, scale_factor, new_size_tag)

# Use the directory of the script itself
directory_path = os.path.dirname(os.path.realpath(__file__))
process_directory_for_rescaling(directory_path)