import random
import search_google.api
import json

config = json.load(open('config.json'))

cse_key = config['cse_key']
cse_id = config['cse_id']


# Search image based on query and return random image
def imagesearch(query):

    # Randomize image
    i = random.randint(0, 20)

    buildargs = {
      'serviceName': 'customsearch',
      'version': 'v1',
      'developerKey': cse_key
    }

    # Custom search engine args
    cseargs = {
      'q': query,
      'cx': cse_id,
      'num': 1,
      'searchType': 'image',
      'safe': 'high',
      'start': i
    }

    result = search_google.api.results(buildargs, cseargs)
    link = str(result.links[0])

    return link


# Search text based on query and return top n results
def textsearch(query):

    # Number of results
    num_results = 5

    buildargs = {
        "serviceName": "customsearch",
        "version": "v1",
        "developerKey": cse_key
    }

    # Custom search engine args
    cseargs = {
        "q": query,
        "cx": cse_id,
        "num": num_results
    }

    final = []

    results = search_google.api.results(buildargs, cseargs)
    links = results.get_values('items', 'link')
    snippets = results.get_values('items', 'snippet')

    for i in range(0, num_results):
        final += ['='*40 + '\n\n' + str(i+1) + ':  ' + links[i]+ '\n' + snippets[i] + '\n']

    return '\n'.join(final)
