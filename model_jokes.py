import random

jokes_data = []
joke_list = [{'GME': [{'2021-1-1:': 4.75}, {'2021-2-1:': 79.14}, {'2021-3-1:': 26.135},
                        {'2021-4-1:': 48.34}, {'2021-5-1:': 44.3725}, {'2021-6-1:': 58.37},
                        {'2021-7-1:': 53.35}, {'2021-8-1:': 40.5}, {'2021-9-1:': 56},
                        {'2021-10-1:': 44.85}, {'2021-11-1:': 45.6325}, {'2021-12-1:': 49.85}]},
              {'AAPL': [{'2021-1-1:': 133.52}, {'2021-2-1:': 133.75}, {'2021-3-1:': 123.75},
                         {'2021-4-1:': 123.66}, {'2021-5-1:': 132.04}, {'2021-6-1:': 125.08},
                         {'2021-7-1:': 136.6}, {'2021-8-1:': 146.36}, {'2021-9-1:': 152.83},
                         {'2021-10-1:': 141.9}, {'2021-11-1:': 148.985}, {'2021-12-1:': 167.48}]},
              {'GOOGL': [{'2021-1-1:': 88}, {'2021-2-1:': 92.2293}, {'2021-3-1:': 102.4},
                          {'2021-4-1:': 104.6125}, {'2021-5-1:': 118.2455}, {'2021-6-1:': 118.722},
                          {'2021-7-1:': 121.725}, {'2021-8-1:': 135.117}, {'2021-9-1:': 145},
                          {'2021-10-1:': 134.4475}, {'2021-11-1:': 148.046}, {'2021-12-1:': 144}]},
              {'TSLA': [{'2021-1-1:': 239.82}, {'2021-2-1:': 271.43}, {'2021-3-1:': 230.0367},
                         {'2021-4-1:': 229.4567}, {'2021-5-1:': 234.6}, {'2021-6-1:': 209.2667},
                         {'2021-7-1:': 227.9733}, {'2021-8-1:': 233.3333}, {'2021-9-1:': 244.6933},
                         {'2021-10-1:': 259.4667}, {'2021-11-1:': 381.6667}, {'2021-12-1:': 386.8983}]},]

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