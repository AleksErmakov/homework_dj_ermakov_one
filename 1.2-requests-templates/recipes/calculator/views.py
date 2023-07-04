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
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def some_recipe(request, name_recipe):
    count = int(request.GET.get('servings', 1))
    goods_for_person = {}
    if name_recipe in DATA.keys():
        values = DATA.get(name_recipe)
        for elem, item in values.items():
            new_elem = item * count
            goods_for_person[elem] = new_elem

        context = dict.fromkeys((name_recipe,), goods_for_person)
        context['recipe'] = context.pop(name_recipe)
        return render(request, 'calculator/index.html', context)
