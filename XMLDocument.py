import xml.etree.ElementTree as ET

class Document :
    def __init__(self, index, Type = "source"): #DISCLAIMER: START INDEX FROM 0 INSTEAD OF 1
        self.Type = Type
        self.name = "Dataset/" + Type + "-document/part" + str(int(index/500) + 1) + "/" + Type + "-document (" + str(int(index%500 + 1)) + ")"
        self.title = "None"
        self.author = "None"
        if Type == "suspicious":
            self.source_doc = []
            self.source_length = []
            self.source_offset = []
            self.length = []
            self.offset = []
            self.slice = slice(-9, -4)
        
    def parse(self):
        tree = ET.parse(self.name + ".xml")
        root = tree.getroot()
        self.title = root[0].get('title')
        self.author = root[0].get('authors')
        if self.Type=="suspicious":
            for child in root:
                if child.tag == "plagiarism":
                    self.source_doc.append(int(child.get("source")))
                    self.source_length.append(int(child.get("source_length")))
                    self.source_offset.append(int(child.get("source_offset")))
                    self.length.append(int(child.get("length")))
                    self.offset.append(int(child.get("offset")))
                    
    def commit(self):
        root = ET.Element("document")
        ET.SubElement(root, 'details', title = self.title, authors = self.author)
        for i in range(len(self.source_doc)):
            ET.SubElement(root, 'plagiarism',
                                 source_length = str(self.source_length[i]),
                                 source_offset = str(self.source_offset[i]),
                                 length = str(self.length[i]),
                                 offset = str(self.offset[i]),
                                 source = str(self.source_doc[i]))
        tree = ET.ElementTree(root)
        tree.write(self.name + '.xml')
