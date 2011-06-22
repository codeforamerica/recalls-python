#!/usr/bin/env python

"""Unit tests for Python API wrapper."""

import unittest

from mock import Mock

#from api import RecallsAPI
import api


def set_up_tests():
    """Cut down on boilerplate setup testing code."""
    api.urlopen = Mock()
    api.json = Mock()


def called_url():
    """Test what URL was called through the mocked urlopen."""
    url = api.urlopen.call_args[0][0]
    return url


#class TestRecallsAPI(unittest.TestCase):

    #def setUp(self):
        #set_up_tests()

    #def test_base_url(self):
        #example = RecallsAPI() 
        #self.assertEquals(example.base_url,
                #'http://search.usa.gov/search/recalls?')


#class TestApiMethod(unittest.TestCase):

    #def setUp(self):
        #set_up_tests()

    #def test_empty_api_method_fails(self):
        #self.assertRaises(TypeError, RecallsAPI())


class TestMethod_RecallsAPI(unittest.TestCase):

    #def setUp(self):
        #set_up_tests()

    #def testmethod_startdate_enddate(self):
        #RecallsAPI().search(startdate='2010-03-19', enddate='2010-03-19')
        #url = called_url()
        #expected_url = ('http://search.usa.gov/search/recalls?startdate=2010-03-19&enddate=2010-03-19&format=json')
        #self.assertEquals(url, expected_url)

    def testmethod_apikey(self):
        api.RecallsAPI('my_testapikey').search(startdate='2010-03-19', enddate='2010-03-19')
        url = called_url()
        expected_url = ('')
        self.assertEquals(url, expected_url)

if __name__ == '__main__':
    unittest.main()
