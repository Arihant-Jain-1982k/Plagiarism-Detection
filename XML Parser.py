import nltk.data
import XMLDocument as xml

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        
source = []
sus = []
"""
for i in range(11093):
    doc = xml.Document(i)
    doc.parse()
    source.append(doc)
    print(i)
"""
for i in range(750):
    doc = xml.Document(i, Type = "suspicious")
    doc.parse()
    sus.append(doc)
    print(i)

sources = []

for i in sus:
    sources = sources + i.source_doc
    
s = sorted(set(sources))
"""
for doc in sus:
    if len(doc.source_doc) != 0:
        for i in range(len(doc.source_doc)):
            source_file = open(source[doc.source_doc[i]-1].name + '.txt', encoding = 'utf8')
            sus_file = open(doc.name + '.txt', encoding = 'utf8')
            
            Offset = source_file.read(doc.source_offset[i])
            Length = source_file.read(doc.source_length[i])
            Offset = tokenizer.tokenize(Offset)
            Length = tokenizer.tokenize(Length)
            doc.source_offset[i] = len(Offset)
            doc.source_length[i] = len(Length)
            
            Offset = sus_file.read(doc.offset[i])
            Length = sus_file.read(doc.length[i])
            Offset = tokenizer.tokenize(Offset)
            Length = tokenizer.tokenize(Length)
            doc.offset[i] = len(Offset)
            doc.length[i] = len(Length)
            
            source_file.close()
            sus_file.close()
            
            print(doc.name)
        
    doc.commit()
"""
