import unittest
from lxmlxtree import xtree
from lxml import etree
from lxml.doctestcompare import LXMLOutputChecker

class TestLxmlFuncs(unittest.TestCase):

	def test_wrap(self):  
		doc = xtree('testdata/test_wrap.xml')
		doc.parse(False)
		if not doc.is_valid:
			if not doc.errors is None: print(doc.errors)
		for text in doc.tree.xpath('//text'):
			el = etree.Element('EL')
			el.set('atr', 'test')
			doc.wrap_text(text,'text',el)
		r = xtree('testdata/r_test_wrap.xml')
		r.parse(False)
		checker = LXMLOutputChecker()
		self.assertTrue(checker.compare_docs(r.tree.getroot(),doc.tree.getroot()))

		
	def test_insertPIAfter(self):
		doc = xtree('testdata/test_wrap.xml')
		doc.parse(False)
		for text in doc.tree.xpath('//text'):
			pi = etree.ProcessingInstruction('PI', 'Pb')
			doc.insert_node(text,'stuff',pi)
		r = xtree('testdata/r_test_insertPIAfter.xml')
		r.parse(False)
		checker = LXMLOutputChecker()
		self.assertTrue(checker.compare_docs(r.tree.getroot(),doc.tree.getroot()))
		
	def test_insertPIBefore(self):  
		doc = xtree('testdata/test_wrap.xml')
		doc.parse(False)
		for text in doc.tree.xpath('//text'):
			pi = etree.ProcessingInstruction('PI', 'Pb')
			doc.insert_node(text,'stuff',pi,True)
		r = xtree('testdata/r_test_insertPIBefore.xml')
		r.parse(False)
		checker = LXMLOutputChecker()
		self.assertTrue(checker.compare_docs(r.tree.getroot(),doc.tree.getroot()))
		
	
	def test_encodeEntities(self):
		doc = xtree('testdata/test_data.xml')
		doc.parse(False)
		r = xtree('testdata/r_test_encode.xml')
		r.parse(False)
		checker = LXMLOutputChecker()
		self.assertTrue(checker.compare_docs(r.tree.getroot(),doc.tree.getroot()))

	def test_serialise(self):
		doc = xtree('testdata/r_test_encode.xml')
		doc.parse(False)
		filename = 'testdata/test_data.xml'
		doc.serialise(filename)
		f = open(filename,'r').read()
		r = open('testdata/r_test_ser.xml','r').read()
		self.assertEqual(f,r)
	def test_integration(self):
		doc = xtree('testdata/test_integ_data.xml')
		doc.parse(False)		
		for text in doc.tree.xpath('//text'):
			el = etree.Element('EL1')
			el.set('target', 'stuff')
			doc.wrap_text(text,'stuff',el)
			pi = etree.ProcessingInstruction('PI1', 'Pb')
			doc.insert_node(text,'text',pi,True)
			pi = etree.ProcessingInstruction('PI2', 'Pb')		
			doc.insert_node(text,'wrapped',pi)	
			el = etree.Element('EL2')
			el.set('target', 'wrap')
			doc.wrap_text(text,'wrapped',el)
		filename = 'testdata/test_data.xml'
		doc.serialise(filename)
		f = open(filename,'r').read()
		
		r = open('testdata/r_test_integ_data.xml','r').read()
		self.assertEqual(f,r)
	# def test_rootSort(self):
		# xmlstr = '<root>asdf<text>some stuff in the text to be wrapped</text><text>1some stuff in the text to be wrapped</text><text>another stuff in the text to be wrapped</text></root>'
		# resstr = '<root>asdf<text>1some stuff in the text to be wrapped</text><text>another stuff in the text to be wrapped</text><text>some stuff in the text to be wrapped</text></root>'
		# doc = lxmlfn(xmlstr, type='string')
		# tree=doc.parse()
		# doc.sort(tree.getroot(),'text')
		# rs = doc.outputString()
		# self.assertEqual(resstr, rs)
		
if __name__ == '__main__':
    #unittest.main()
		
	suite = unittest.TestLoader().loadTestsFromTestCase(TestLxmlFuncs)
	unittest.TextTestRunner(verbosity=2).run(suite)

