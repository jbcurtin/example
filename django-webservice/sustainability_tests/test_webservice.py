BASE_URL = 'http://localhost:8000'
TEST_INDEX = 'test-0'

def test_restaurant_list():
    import requests

    from urllib.parse import urlencode

    url = f'{BASE_URL}/webservice/restaurants.json?namespace={TEST_INDEX}'
    resp = requests.get(url)


def test_search__force_error():
    import requests

    from urllib.parse import urlencode

    url = f'{BASE_URL}/webservice/search.json'
    params = urlencode({
        'ns': 'noop',
    })
    url = '?'.join([url, params])
    resp = requests.get(url)
    assert resp.status_code != 200


def test_search__no_terms():
    import requests

    from urllib.parse import urlencode

    url = f'{BASE_URL}/webservice/search.json'
    params = urlencode({
        'ns': TEST_INDEX,
    })
    url = '?'.join([url, params])
    content = requests.get(url).json()
    assert TEST_INDEX in content.keys()
    assert len(content[TEST_INDEX]) > 0


def test_search__geom():
    import requests

    from urllib.parse import urlencode

    url = f'{BASE_URL}/webservice/search.json'
    params = urlencode({
        'geom': '26.307068,127.7625403',
        'ns': TEST_INDEX,
    })
    url = '?'.join([url, params])
    content = requests.get(url).json()
    assert TEST_INDEX in content.keys()
    assert len(content[TEST_INDEX]) > 0
    # Additional tests against specific data


def test_search__name():
    import requests

    from urllib.parse import urlencode

    url = f'{BASE_URL}/webservice/search.json?name=Community Trade'
    params = urlencode({
        'name': 'Community Trade',
        'ns': TEST_INDEX,
    })
    url = '?'.join([url, params])
    content = requests.get(url).json()
    assert TEST_INDEX in content.keys()
    assert len(content[TEST_INDEX]) > 0
    # Additional tests against specific data


def test_search__keywords():
    import requests

    from urllib.parse import urlencode

    url = f'{BASE_URL}/webservice/{TEST_INDEX}/search.json?keywords=Osaka'
    params = urlencode({
        'name': 'Community Trade',
        'ns': TEST_INDEX,
    })
    url = '?'.join([url, params])
    content = requests.get(url).json()
    assert TEST_INDEX in content.keys()
    assert len(content[TEST_INDEX]) > 0
    # Additional tests against specific data


def test_segment__none():
    import requests

    from urllib.parse import urlencode

    url = f'{BASE_URL}/webservice/segment.json'
    params = urlencode({
        'ns': TEST_INDEX,
    })
    url = '?'.join([url, params])
    content = requests.get(url).json()
    assert TEST_INDEX in content.keys()
    assert len(content[TEST_INDEX]) > 0
    # Additional tests against specific data


def test_segment__jp_ipaddress():
    import requests

    from urllib.parse import urlencode

    url = f'{BASE_URL}/webservice/{TEST_INDEX}/segment.json'
    params = urlencode({
        'ipaddress': '211.11.141.21',
        'ns': TEST_INDEX,
    })
    url = '?'.join([url, params])
    content = requests.get(url).json()
    assert TEST_INDEX in content.keys()
    assert len(content[TEST_INDEX]) > 0
    # Additional tests against specific data


