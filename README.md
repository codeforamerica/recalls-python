Python wrapper for USA.gov Product Recalls Data API. 
http://search.usa.gov/api/recalls

Usage example:
<pre><code>
from api import RecallsAPI
foo = RecallsAPI(api_key='9c63bbbfcd985314b245ef92ab37a792')
foo.search(query='tires')
</pre></ocde>
If you give an incorrect API key, you will get an error like so:
<pre><code>
ValueError: No JSON object could be decoded
</pre></code>

No API key is actually needed for this API
<pre><code>
from api import RecallsAPI
bar = RecallsAPI()
bar.search(query='tires')

24 Jun 2011
Todo: add error checking e.g. for incorrect API key

Third Party Libraries
---------------------

Current third-party libraries we're using include:

* `mock` -- Create test stubs and mocks.
<pre><code>
    >>> from mock import Mock
    >>> from api import api
    >>> api.urlopen = Mock()
</code></pre>

* `coverage` -- Check test code coverage.
<pre><code>
    $ coverage run test.py
    .................
    -----------------
    Ran 17 tests in 0.010s

    $ coverage report -m
    Name                          Stmts   Miss  Cover   Missing
    -----------------------------------------------------------
    test                            113      0   100%   
    api/__init__                      2      0   100%   
    api/api                          42      0   100%   
    api/api_key                       2      0   100%   
    -----------------------------------------------------------
    TOTAL                           159      0   100%   
</code></pre>

* `pep8` -- Check Python files are following the PEP 8 Style Guide.
<pre><code>
    $ pep8 test.py
    test.py:12:1: E302 expected 2 blank lines, found 1
</code></pre>
