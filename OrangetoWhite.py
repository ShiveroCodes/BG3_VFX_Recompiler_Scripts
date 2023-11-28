import xml.etree.ElementTree as ET
import os

def change_color_to_white(input_file_name):
    # Replace "Orange" with "White" in the file name
    new_file_name = input_file_name.replace("Orange", "White")
    
    # Parse the XML file
    tree = ET.parse(input_file_name)
    root = tree.getroot()

    # Find all the color attributes and set them to white
    for frame_node in root.findall(".//node[@id='Frames']/children/node[@id='Frame']/attribute[@id='Color']"):
        color_attribute = frame_node.get('value')
        if color_attribute:
            # Set color to white
            frame_node.set('value', "1 1 1 1")

    # Write the modified content to the new file name
    tree.write(new_file_name, xml_declaration=True, encoding='utf-8')
    print(f"File has been created: {new_file_name}")

def process_directory(directory_path):
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".lsfx.lsx") and "Orange" in file_name:
            full_path = os.path.join(directory_path, file_name)
            change_color_to_white(full_path)

# Replace with your directory path
directory_path = os.path.dirname(__file__)
process_directory(directory_path)
