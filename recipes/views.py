from django.shortcuts import render

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
}

def default_view(request):
    my_list = {
        'title': 'Список приложений'
    }
    return render(request, 'recipes/default_page.html', my_list)


def recipes_view(request):
    my_dict = {
        'title': 'Страница с рецептами',
        'data': DATA

    }
    return render(request, 'recipes/index.html', my_dict)


def calcul_view(request, name_dish):
    if str(request.GET.get('servings', 1)).isdigit():
        count = int(request.GET.get('servings', 1))
    else:
        count = 1
    if count <= 0:
        count = 1
    dish_cal = dict()
    for k, i in DATA.items():
        if k == name_dish:
            for key, val in i.items():
                dish_cal[key] = f'{val * count:.2f}'

            my_dict = {
                'title': f'Состав блюда {name_dish}',
                'calc_dict': dish_cal,
                'name_dish': name_dish,
                'count': count
            }

            return render(request, 'recipes/calculation.html', my_dict)
