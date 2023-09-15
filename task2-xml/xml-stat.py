import xml.etree.ElementTree as ET
import re
from collections import Counter
import math

def qname(tag):
    return re.sub(r'^{([^}]+)}', lambda x: ns2[x.group(1)] + ':', tag)

ns = {
  'europeana': 'http://www.europeana.eu/schemas/ese/', 
  'dcterms': 'http://purl.org/dc/terms/',
  'oai': 'http://www.openarchives.org/OAI/2.0/',
  'doc': 'http://www.lyncode.com/xoai',
  'dc': 'http://purl.org/dc/elements/1.1/',
  'xml': 'http://www.w3.org/XML/1998/namespace'
}
ns2 = {}
for (k,v) in ns.items():
    ns2[v] = k

tree = ET.parse('ddb.xml')
root = tree.getroot()

recordNumber = 0
counter = Counter()
for record in root:
    recordNumber += 1
    tags = set()
    for tag in record:
        tagname = qname(tag.tag)
        if len(tag.attrib) > 0:
            attributes = []
            for attrib in tag.attrib:
                qattrib = qname(attrib)
                if qattrib == 'type' or qattrib == 'xml:lang':
                    attributes.append(tag.attrib[attrib])
            if len(attributes) > 0:
                tags.add('%s (%s)' % (tagname, ','.join(attributes)))
            else:
                tags.add(tagname)
        else:
            tags.add(tagname)
    counter.update(tags)

for (k,v) in counter.items():
    print('%s: %d%%' % (k, math.floor(v * 100 / recordNumber)))

