from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    print('meaning')
    print(meaning)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)
    key = list(meaning.keys()) 
    context = {
        'meaning': meaning[key[0]][0],
        'synonyms': synonyms,
        'antonyms': antonyms
    }
    return render(request, 'word.html', context)