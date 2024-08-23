import random
from datetime import datetime, timedelta

import requests
from test.baseclasses import GlobalErrorMesages,Response
from test.schemas import Map, ColorMap

SERVICE_URL = "https://rmkop-test.gis.by/api/"

def test_get_presented_days():
    response=requests.get(SERVICE_URL+'get_presented_days')
    assert response.status_code==200 , GlobalErrorMesages.WRONG_STATUS_CODE.value
    count_presented_day=len(response.json())
    assert count_presented_day > 0 , GlobalErrorMesages.WRONG_COUNT_PRESENTED_DAY.value


def test_get_palette():
    r = requests.get(SERVICE_URL + 'get_palette')
    resp=Response(r)
    resp.assert_status_code([200,201]).validate(ColorMap)

def test_get_map():
    """
    Test get_map checking code status and schema response
    """
    testDate = (datetime.today() - timedelta(days=random.randint(1, 5))).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
    r = requests.get(SERVICE_URL + 'get_map?datetime=' + testDate)
    resp = Response(r)
    resp.assert_status_code([200]).validate(Map)








