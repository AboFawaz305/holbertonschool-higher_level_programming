#!/usr/bin/python3
"""
serialize and deserialize using XML
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        # Convert value to string for XML text
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}

    for child in root:
        text = child.text

        # Try to convert text to int, float, bool, or leave as string
        # if text is None:
        #     value = None
        # elif text.lower() == "true":
        #     value = True
        # elif text.lower() == "false":
        #     value = False
        # else:
        #     try:
        #         value = int(text)
        #     except ValueError:
        #         try:
        #             value = float(text)
        #         except ValueError:
        #             value = text  # fallback to string

        # result[child.tag] = value
        result[child.tag] = text

    return result


def main():
    sample_dict = {"name": "John", "age": "28", "city": "New York"}

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)


if __name__ == "__main__":
    main()
