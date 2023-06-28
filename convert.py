import pandas as pd 

import xml.etree.ElementTree as ET 

def excel_to_tally_xml(excel_file,xml_file):
    df=pd.read_excel(excel_file)
    root=ET.Element('{http://www.tallysolutions.com/XMLSchema}TALLYMESSAGE')
    for _,row in df.iterrows():
        data_element=ET.SubElement(root,'DATA')
    
        for column_name,value,in row.items():
        
            field_element=ET.SubElement(data_element,'FIELD',{'NAME':column_name})
            field_element.text=str(value)
    tree=ET.ElementTree(root)
    with open(xml_file,'wb')as f:
        tree.write(f,encoding='utf-8',xml_declaration=True)
        

excel_file_path = 'smaple.xlsx'
xml_file_path = 'output.xml'
excel_to_tally_xml(excel_file_path, xml_file_path)