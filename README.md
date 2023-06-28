
# Excel to Tally XML Converter

This Python script converts an Excel file into Tally XML format. It reads the data from the Excel file and generates an XML file compatible with Tally software.

## Installation

1. Make sure you have Python 3 installed on your system. If you don't have Python installed, you can download it from the official website: [Python Downloads](https://www.python.org/downloads/)

2. Clone this repository to your local machine or download the script file (`excel_to_tally_xml.py`) directly.

3. Install the required dependencies by running the following command:

   ```bash
   pip install pandas
   ```

   This will install the Pandas library, which is used for reading the Excel file.

4. Additionally, ensure that the `tkinter` library is installed. `tkinter` is used for the file dialog functionality. It is usually included with Python, but if it's not available, you may need to install it separately.

## Usage

1. Open a command-line or terminal window and navigate to the directory where the `excel_to_tally_xml.py` script is located.

2. Run the following command to start the script:

   ```bash
   python excel_to_tally_xml.py
   ```

3. The script will prompt you to select the Excel file you want to convert. Choose the desired file from the file dialog window that appears.

4. Next, the script will ask you to provide the output XML file path. Select the location and provide a name for the XML file. The file extension `.xml` will be added automatically.

5. Once the conversion is complete, the script will display a success message along with the path to the generated XML file.

## Example

Here's an example demonstrating the usage of the Excel to Tally XML Converter:

```python
import pandas as pd
import xml.etree.ElementTree as ET
from tkinter import Tk, filedialog

# Rest of the code...

# Call the function to convert Excel to Tally XML
excel_to_tally_xml()
```
