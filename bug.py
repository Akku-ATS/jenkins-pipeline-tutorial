   #! /usr/bin/env python
 #'Example errors caught by PyChecker'
test1910
import string
metaslash = 1
def printNames():
       neal = 'neal'
       michelle = 'michele'
       eric = 5
       print "Local values: %(neal)S %(michele)s %(eric)" % locals()
class Nothing:
       def printValue(value):
           print value
       def set(self, value):
           self.value = value
def tryToDoSomething(self, value):
       try:
           import string
           if not value:
               raise RuntimeError, "Hey, there's no value"
           printNames('a, b, c')
       except:
           traceback.print_exc()
def setGlobal(value=None):
       print 'Old MetaSlash value is:', metaslash
       metaslash = value
       useless = Nothing(5)
       print 'a useless value is:', useless.valeu
just testing 1910
Test 2
test 3
test 211020

def setGlobal(value=None):
       print 'Old MetaSlash value is:', metaslash
       metaslash = value
       useless = Nothing(5)
       print 'a useless value is:', useless.valeu
