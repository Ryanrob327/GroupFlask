import random

jokes_data = []
joke_list = [{'TSLA': [{'date': '2021-1-1', 'open': 239.82, 'high': 300.1333, 'low': 239.0632, 'close': 264.51},
                      {'date': '2021-2-1', 'open': 271.43, 'high': 293.5, 'low': 206.3333, 'close': 225.1667},
                      {'date': '2021-3-1', 'open': 230.0367, 'high': 291.3133, 'low': 179.83, 'close': 222.6433},
                      {'date': '2021-4-1', 'open': 229.4567, 'high': 260.2633, 'low': 219.8067, 'close': 236.48},
                      {'date': '2021-5-1', 'open': 234.6, 'high': 235.3333, 'low': 182.3267, 'close': 208.4067},
                      {'date': '2021-6-1', 'open': 209.2667, 'high': 232.54, 'low': 190.4067, 'close': 226.5667},
                      {'date': '2021-7-1', 'open': 227.9733, 'high': 233.3333, 'low': 206.82, 'close': 229.0667},
                      {'date': '2021-8-1', 'open': 233.3333, 'high': 246.7967, 'low': 216.28, 'close': 245.24},
                      {'date': '2021-9-1', 'open': 244.6933, 'high': 266.3333, 'low': 236.2833, 'close': 258.4933},
                      {'date': '2021-10-1', 'open': 259.4667, 'high': 371.7367, 'low': 254.53, 'close': 371.3333},
                      {'date': '2021-11-1', 'open': 381.6667, 'high': 414.4967, 'low': 326.2, 'close': 381.5867},
                      {'date': '2021-12-1', 'open': 386.8983, 'high': 390.9466, 'low': 295.3733, 'close': 352.26}]},
              {'AAPL': [{'date': '2021-1-1', 'open': 133.52, 'high': 145.09, 'low': 126.382, 'close': 131.96},
                        {'date': '2021-2-1', 'open': 133.75, 'high': 137.877, 'low': 118.39, 'close': 121.26},
                        {'date': '2021-3-1', 'open': 123.75, 'high': 128.72, 'low': 116.21, 'close': 122.15},
                        {'date': '2021-4-1', 'open': 123.66, 'high': 137.07, 'low': 122.49, 'close': 131.46},
                        {'date': '2021-5-1', 'open': 132.04, 'high': 134.07, 'low': 122.25, 'close': 124.61},
                        {'date': '2021-6-1', 'open': 125.08, 'high': 137.41, 'low': 123.13, 'close': 136.96},
                        {'date': '2021-7-1', 'open': 136.6, 'high': 150, 'low': 135.76, 'close': 145.86},
                        {'date': '2021-8-1', 'open': 146.36, 'high': 153.49, 'low': 144.5, 'close': 151.83},
                        {'date': '2021-9-1', 'open': 152.83, 'high': 157.26, 'low': 141.27, 'close': 141.5},
                        {'date': '2021-10-1', 'open': 141.9, 'high': 153.165, 'low': 138.27, 'close': 149.8}
                        , {'date': '2021-11-1', 'open': 148.985, 'high': 165.7, 'low': 147.48, 'close': 165.3},
                        {'date': '2021-12-1', 'open': 167.48, 'high': 182.13, 'low': 157.8, 'close': 177.57}]},
              {'GOOGL': [{'date': '2021-1-1', 'open': 88, 'high': 96.604, 'low': 84.8051, 'close': 91.368},
                         {'date': '2021-2-1', 'open': 92.2293, 'high': 107.257, 'low': 92.2293, 'close': 101.0955},
                         {'date': '2021-3-1', 'open': 102.4, 'high': 105.687, 'low': 99.7, 'close': 103.126},
                         {'date': '2021-4-1', 'open': 104.6125, 'high': 121.569, 'low': 104.5715, 'close': 117.675},
                         {'date': '2021-5-1', 'open': 118.2455, 'high': 119.4525, 'low': 109.681, 'close': 117.8425},
                         {'date': '2021-6-1', 'open': 118.722, 'high': 123.0955, 'low': 116.476, 'close': 122.0895},
                         {'date': '2021-7-1', 'open': 121.725, 'high': 138.297, 'low': 121.5315, 'close': 134.7265},
                         {'date': '2021-8-1', 'open': 135.117, 'high': 145.9705, 'low': 133.3195, 'close': 144.6975},
                         {'date': '2021-9-1', 'open': 145, 'high': 146.2538, 'low': 133.556, 'close': 133.676},
                         {'date': '2021-10-1', 'open': 134.4475, 'high': 148.65, 'low': 131.05, 'close': 148.046},
                         {'date': '2021-11-1', 'open': 148.046, 'high': 150.9665, 'low': 141.6015, 'close': 141.8975},
                         {'date': '2021-12-1', 'open': 144, 'high': 149.1, 'low': 139.321, 'close': 144.852}]},
              {'GME': [{'date': '2021-1-1', 'open': 4.75, 'high': 120.75, 'low': 4.27, 'close': 81.25},
                       {'date': '2021-2-1', 'open': 79.14, 'high': 80.5, 'low': 9.625, 'close': 25.435},
                       {'date': '2021-3-1', 'open': 26.135, 'high': 87.125, 'low': 24.9925, 'close': 47.455},
                       {'date': '2021-4-1', 'open': 48.34, 'high': 49.2423, 'low': 33, 'close': 43.3975},
                       {'date': '2021-5-1', 'open': 44.3725, 'high': 67.2, 'low': 34.125, 'close': 55.5},
                       {'date': '2021-6-1', 'open': 58.37, 'high': 86.165, 'low': 49.25, 'close': 53.535},
                       {'date': '2021-7-1', 'open': 53.35, 'high': 54.2075, 'low': 39.5025, 'close': 40.28},
                       {'date': '2021-8-1', 'open': 40.5, 'high': 56.75, 'low': 36.305, 'close': 54.56},
                       {'date': '2021-9-1', 'open': 56, 'high': 57.8598, 'low': 41.6975, 'close': 43.8675},
                       {'date': '2021-10-1', 'open': 44.85, 'high': 48.045, 'low': 41.4525, 'close': 45.8775},
                       {'date': '2021-11-1', 'open': 45.6325, 'high': 63.9225, 'low': 45.5125, 'close': 49.0525},
                       {'date': '2021-12-1', 'open': 49.85, 'high': 50.0263, 'low': 32.375, 'close': 37.0975}]
},]

# Initialize jokes
def initJokes():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in joke_list:
        jokes_data.append({"id": item_id, "stock": joke_list[item_id]})
        item_id += 1
        
# Return all jokes from jokes_data
def getJokes():
    return(jokes_data)

# Joke getter
def getJoke(id):
    return(jokes_data[id])

# Return random joke from jokes_data
def getRandomJoke():
    return(random.choice(jokes_data))

# Pretty Print joke
def printJoke(joke):
    print(joke['id'], joke['joke'])

# Number of jokes
def countJokes():
    return len(jokes_data)

# Test Joke Model
if __name__ == "__main__": 
    initJokes()  # initialize jokes
    
    # Random joke
    print("Random joke")
    printJoke(getRandomJoke())
    
    # Count of Jokes
    print("Jokes Count: " + str(countJokes()))