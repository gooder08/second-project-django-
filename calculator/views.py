from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def omlet(requests):
    servings = int(requests.GET.get('servings', 1))
    DATA_new = {}   
    for ing, am in DATA['omlet'].items():
        DATA_new[ing] = am*servings
    print(DATA_new)
    context = {
        'recipe': DATA_new,
    }
    return render(requests, 'calculator/index.html', context)

def pasta(requests):
    servings = int(requests.GET.get('servings', 1))
    DATA_new = {}   
    for ing, am in DATA['pasta'].items():
        DATA_new[ing] = am*servings
    print(DATA_new)
    context = {
        'recipe': DATA_new,
    }
    return render(requests, 'calculator/index.html', context)

def buter(requests):
    servings = int(requests.GET.get('servings', 1))
    DATA_new = {}   
    for ing, am in DATA['buter'].items():
        DATA_new[ing] = am*servings
    print(DATA_new)
    context = {
        'recipe': DATA_new,
    }
    return render(requests, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
