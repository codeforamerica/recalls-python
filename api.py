#!/usr/bin/env python

"""
    Python wrapper for USA.gov Product Recall Data API.
    http://search.usa.gov/api/recalls
"""

try:
    import json
except ImportError:  # pragma: no cover
    # For older versions of Python.
    import simplejson as json

try:
    from urllib import urlencode
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.parse import urlencode

try:
    from urllib2 import urlopen
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.request import urlopen

class RecallsAPI(object):
    def __init__(self, api_key=''):
        self.api_key = api_key
        self.base_url = 'http://search.usa.gov/search/recalls?' 

    def _apicall(self, params):
        if not self.api_key:
            url = self.base_url + '%s&format=json' % \
                (urlencode(params, True))
        else: 
            url = self.base_url + '%sapi_key=%s&format=json' % \
                (urlencode(params, True), self.api_key)
        response = urlopen(url).read()
        return json.loads(response)

    def search(self, **keywords):
        """
        API Documentation: http://search.usa.gov/api/recalls   

        Parameters:
        api_key: your API key. You can get a key by signing up for an account.
        Example: http://search.usa.gov/search/recalls?api_key=9c63bbbfcd985314b245ef92ab37a792
        >>> RecallsAPI().search(api_key='9c63bbbfcd985314b245ef92ab37a792')

        format: json. This parameter is required. The most recent recalls are 
        returned as the default if no other parameters are given.
        Example: http://search.usa.gov/search/recalls?format=json
        ('format=json' is appended to URL by default by this wrapper)

        query: keywords. Query terms for the search. Add more terms to narrow
        the search with spaces between terms; use "quotes for multi-word search
        terms". (query='"CERTAIN PASSENGER VEHICLES"' gives different results
        than query='CERTAIN PASSENGER VEHICLES')
        Example: http://search.usa.gov/search/recalls?query=tires&format=json
        >>> RecallsAPI().search(query='tires')
        >>> RecallsAPI().search(query='tires "durability testing"')

        start_date: yyyy-mm-dd. Start date of the recall.
        Example: http://search.usa.gov/search/recalls?start_date=2010-01-01&end_date=2010-03-19&format=json
        >>> RecallsAPI().search(start_date='2010-01-01', end_date='2010-03-19'

        end_date: yyyy-mm-dd. End date of the recall.
        Example: http://search.usa.gov/search/recalls?start_date=2010-01-01&end_date=2010-03-19&format=json
        >>> RecallsAPI().search(start_date='2010-01-01', end_date='2010-03-19'

        organization: Government organization providing the recall data. 
        Valid values are: (1) NHTSA. National Highway Traffic Safety 
        Administration; (2) CPSC. Consumer Product Safety Commission; or 
        (3) CDC. Centers for Disease Control and Prevention. Values must be 
        entered in all caps.
        Example: http://search.usa.gov/search/recalls?format=json&organization=CDC
        >>> RecallsAPI().search(organization='CDC')

        upc: UPC code. This parameter is only relevant for Product Safety. 
        Not all products have UPC code.
        Example: http://search.usa.gov/search/recalls?upc=3826959035&format=json
        >>> RecallsAPI().search(organization='3826959035')

        sort: Sort order. Add '&sort=date' to sort by date, or leave blank to
        sort by relevance.
        Example: http://search.usa.gov/search/recalls?format=json&organization=CDC&sort=date
        >>> RecallsAPI().search(organization='CDC', sort='date')

        code: NHTSA code for auto recalls. Valid values are E, V [for vehicles], 
        I, T, C, or X. Values are single letters, which must be entered in 
        all caps.
        Example: http://search.usa.gov/search/recalls?format=json&make=Toyota&code=V
        >>> RecallsAPI().search(make='Toyota', code='V')

        make: NHTSA make information for auto recalls.
        Example: http://search.usa.gov/search/recalls?format=json&make=Toyota
        >>> RecallsAPI().search(make='Toyota', code='V')

        model: NHTSA model information for auto recalls.
        Example: http://search.usa.gov/search/recalls?format=json&model=Camry
        >>> RecallsAPI().search(model='Camry')

        year: yyyy. NHTSA year information for auto recalls.
        Example: http://search.usa.gov/search/recalls?format=json&year=2002
        >>> RecallsAPI().search(year='2002')

        page: Pagination of search results. Ten results are displayed on each 
        search results page. Paginate search results pages by adding '&page=#' 
        to the query string.
        Example: http://search.usa.gov/search/recalls?format=json&page=3
        >>> RecallsAPI().search(page='3')
        """
        return self._apicall(keywords)
