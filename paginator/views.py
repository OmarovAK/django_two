from django.shortcuts import render
import os
import csv
from django.core.paginator import Paginator


def pagin_view(request):
    file = os.path.join(os.getcwd(), 'data-398-2018-08-30.csv')
    my_list = list()
    with open(file, mode='r', encoding='utf-8') as f:
        file_reader = csv.DictReader(f, delimiter=",")
        for i in file_reader:
            my_list.append(i)
    for i in my_list:
        print(i)
    paginator = Paginator(my_list, 20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    my_dict = {
        'title': 'Страница со станциями',
        'list': page_obj,
    }
    return render(request, 'paginator/index.html', my_dict)
