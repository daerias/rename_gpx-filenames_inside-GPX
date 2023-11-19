# Dateiname: rename_gpx-filenames_inside-GPX.py

import os
import glob
import shutil
from lxml import etree as ET

def rename_gpx_files():
    path = './GPX/*.gpx'
    files = glob.glob(path)

    # Erstelle die Ordner "done" und "fail", wenn sie noch nicht existieren
    if not os.path.exists('./done'):
        os.makedirs('./done')
    if not os.path.exists('./fail'):
        os.makedirs('./fail')

    for file in files:
        try:
            parser = ET.XMLParser(remove_blank_text=True)
            tree = ET.parse(file, parser)
            root = tree.getroot()

            # Get filename without extension
            filename = os.path.splitext(os.path.basename(file))[0]

            # Replace content between <name> and </name> tags, regardless of namespace
            for elem in root.iter():
                if elem.tag.endswith('name'):
                    elem.text = filename

            # Write changes back to the file
            tree.write(file, pretty_print=True)

            # Verschiebe die erfolgreich umbenannte Datei in den "done"-Ordner
            shutil.move(file, './done/' + os.path.basename(file))
        except Exception as e:
            print(f"Failed to rename {file} - Error: {str(e)}")

            # Verschiebe die nicht erfolgreich umbenannte Datei in den "fail"-Ordner
            shutil.move(file, './fail/' + os.path.basename(file))

if __name__ == "__main__":
    rename_gpx_files()
