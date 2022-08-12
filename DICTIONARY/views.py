from django.shortcuts import render
from pydictionary import Dictionary

# Create your views here.
def home(request):
    return render(request, 'home.html')

def word(request):

    search = request.GET['search']
    dictionary = Dictionary(search)
    meaning = dictionary.meanings()
    synonyms = dictionary.synonyms()
    antonyms= dictionary.antonyms()
    
    context = {
        'meaning':meaning,
        'synonyms':synonyms,
        'antonyms':antonyms,
        'search':search
    }
    
    return render(request, 'word.html', context)