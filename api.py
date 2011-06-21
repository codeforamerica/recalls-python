from urllib import urlencode, urlopen
import json

class RecallsAPI(object):
    """Wrapper for USA.gov Product Recalls Data API."""
    apikey = None
    base_url = 'http://search.usa.gov/search/recalls?' 

    def _apicall(self, params):
        if RecallsAPI.apikey is None:
            url = RecallsAPI.base_url + '%s&format=json' % \
                (urlencode(params, True))
        else: 
            url = base_url + '%sapi_key=%s&format=json' % \
                (urlencode(params, True), RecallsAPI.apikey)
        #print 'url:' + url
        response = urlopen(url).read()
        return json.loads(response)

    def search(self, **keywords):
        return RecallsAPI()._apicall(keywords)

RecallsAPI().search(startdate='2010-03-19', enddate='2010-03-19')
