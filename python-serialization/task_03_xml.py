#!/usr/bin/env python3
"""xplore serialization and deserialization using XML"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    vrbl = ET.element("data")

    for key, value in _dict_
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

