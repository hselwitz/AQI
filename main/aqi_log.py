import time

import aqi

from sds011 import SDS011
from main.models import AqiData

sensor = SDS011("COM1", use_query_mode=True)


def get_data(n=3):
    sensor.sleep(sleep=False)
    pmt_25 = 0
    pmt_100 = 0
    time.sleep(10)
    for i in range(n):
        x = sensor.query()
        pmt_25 = pmt_25 + x[0]
        pmt_100 = pmt_100 + x[1]
        time.sleep(2)
    pmt_25 = round(pmt_25 / n, 1)
    pmt_100 = round(pmt_100 / n, 1)
    sensor.sleep(sleep=True)
    time.sleep(2)
    return pmt_25, pmt_100


def conv_aqi(pmt_2_5, pmt_10):
    aqi_2_5 = aqi.to_iaqi(aqi.POLLUTANT_PM25, str(pmt_2_5))
    aqi_10 = aqi.to_iaqi(aqi.POLLUTANT_PM10, str(pmt_10))
    return aqi_2_5, aqi_10


def main_logger():
    pmt_25, pmt_100 = get_data()
    aqi_25, aqi_100 = conv_aqi(pmt_25, pmt_100)
    AqiData(aqi_25=aqi_25, aqi_100=aqi_100).save()
