# lxmlxtree

This lxml helper class give an easy way to wrap or insert a node to a certain text.


##Installation

pip install lxmlxtree

##Usage

- read and parse data

```
  from lxmlxtree import xtree

  doc = xtree('inputfile.xml')
  doc.parse(False)
  if not doc.is_valid:
    if not doc.errors is None: print(doc.errors)
```
- wrap

```

  for text in doc.tree.xpath('//text'):
    el = etree.Element('EL')
    el.set('atr', 'test')
    doc.wrap_text(text,'text',el)
```

input
```
<root>rs<text>some stuff in the text to be wrapped</text>re</root>
```
output
```
<root>rs<text>some stuff in the <EL atr="test">text</EL> to be wrapped</text>re</root>
```

- insert after

```
  for text in doc.tree.xpath('//text'):
    pi = etree.ProcessingInstruction('PI', 'Pb')
    doc.insert_node(text,'stuff',pi)
```
input
```
<root>rs<text>some stuff in the text to be wrapped</text>re</root>
```
output
```
<root>rs<text>some stuff<?PI Pb?> in the text to be wrapped</text>re</root>
```
- insert before

```
  for text in doc.tree.xpath('//text'):
    pi = etree.ProcessingInstruction('PI', 'Pb')
    doc.insert_node(text,'stuff',pi, True)
```
input
```
<root>rs<text>some stuff in the text to be wrapped</text>re</root>
```
output
```
<root>rs<text>some <?PI Pb?>stuff in the text to be wrapped</text>re</root>
```
##API


```
  parse(self, dtd_validation=True, encode_entities=True)
  serialise(self, output_file, decode_entities=True)
  insert_node(self, parent, text, node, before=False)
  wrap_text(self, parent, text, element)
```
##Test
```
  python test.py
```