from polygon import RESTClient
from typing import cast
from urllib3 import HTTPResponse
import time

def yearly_data(stock):
    client = RESTClient("w4oXBFSyC3bTkpJeVwSnKt8iuwBgMeMy") # api_key is used
    aggs = client.get_aggs(stock, 1, "month", "2021-01-01", "2021-12-01")

    data = []

    for i in range (12):
        data.append({"date": "2021-" +str(i + 1) + "-1","open": aggs[i].open, "high": aggs[i].high,
                     "low": aggs[i].low, "close": aggs[i].close})
        time.sleep(12)
        
    return(data)
