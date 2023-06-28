import pandas as pd
import xml.etree.ElementTree as ET
from tkinter import Tk, filedialog

def excel_to_tally_xml():
    root = Tk()
    root.withdraw()
    
    # Ask user to upload Excel file
    excel_file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel Files", "*.xlsx")])
    
    if not excel_file_path:
        print("No file selected. Exiting...")
        return
    
    # Specify the output XML file path
    xml_file_path = filedialog.asksaveasfilename(title="Save XML File", defaultextension=".xml", filetypes=[("XML Files", "*.xml")])
    
    if not xml_file_path:
        print("No output file path provided. Exiting...")
        return
    
    df = pd.read_excel(excel_file_path)
    root = ET.Element('{http://www.tallysolutions.com/XMLSchema}TALLYMESSAGE')
    
    for _, row in df.iterrows():
        data_element = ET.SubElement(root, 'DATA')
    
        for column_name, value in row.items():
            field_element = ET.SubElement(data_element, 'FIELD', {'NAME': column_name})
            field_element.text = str(value)
    
    tree = ET.ElementTree(root)
    
    with open(xml_file_path, 'wb') as f:
        tree.write(f, encoding='utf-8', xml_declaration=True)
    
    print("XML file created successfully!")

# Call the function to convert Excel to Tally XML
excel_to_tally_xml()
