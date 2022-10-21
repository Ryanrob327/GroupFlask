from polygon import RESTClient
from typing import cast
from urllib3 import HTTPResponse
import time

client = RESTClient("w4oXBFSyC3bTkpJeVwSnKt8iuwBgMeMy") # api_key is used

aggs = client.get_aggs("AAPL", 1, "month", "2021-01-01", "2021-12-01")

Appledata = []

for i in range (12):
    data.append({"2021-" +str(i + 1) + "-1:": aggs[i].open})
    data.append({"2021-" + str(i + 1) + "-1:": aggs[i].close})
    time.sleep(12)


aggs = client.get_aggs("TSLA", 1, "month", "2021-01-01", "2021-12-01")

Tesladata = []

for i in range (12):
    data.append({"2021-" +str(i + 1) + "-1:": aggs[i].open})
    data.append({"2021-" + str(i + 1) + "-1:": aggs[i].close})
    time.sleep(12)


aggs = client.get_aggs("GME", 1, "month", "2021-01-01", "2021-12-01")

Gamestopdata = []

for i in range (12):
    data.append({"2021-" +str(i + 1) + "-1:": aggs[i].open})
    data.append({"2021-" + str(i + 1) + "-1:": aggs[i].close})
    time.sleep(12)


aggs = client.get_aggs("GOOGL", 1, "month", "2021-01-01", "2021-12-01")

Googledata = []

for i in range (12):
    data.append({"2021-" +str(i + 1) + "-1:": aggs[i].open})
    data.append({"2021-" + str(i + 1) + "-1:": aggs[i].close})
    time.sleep(12)


aggs = client.get_aggs("AMZN", 1, "month", "2021-01-01", "2021-12-01")

Amazondata = []

for i in range (12):
    data.append({"2021-" +str(i + 1) + "-1:": aggs[i].open})
    data.append({"2021-" + str(i + 1) + "-1:": aggs[i].close})
    time.sleep(12)
