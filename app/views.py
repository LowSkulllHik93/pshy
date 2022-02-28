from pynames.generators.elven import DnDNamesGenerator
from django.shortcuts import render
from .models import Controller
from .forms import *

elven_generator = DnDNamesGenerator()
magicpeople = Controller()
a=1

def start(request):
    request.session['psy'] = elven_generator.get_name_simple()
    request.session['psy_num'] = []
    return render (request, 'start.html')

def input_number(request):
    name = request.session['psy']
    nubmer = int(request.POST['number'])
    request.session['psy_num'].append(nubmer)
    responce = {'username': name,
                'user_numbers': request.session['psy_num'],
                'magicpeople': magicpeople.check(nubmer,name),
                }
    return render(request, 'index.html', context=responce)

def answer(request):
    name = request.session['psy']
    request.session.modified = True
    form = InputNumberForm()
    if request.method == 'POST':
        form = InputNumberForm(request.POST)
        if form.is_valid():
            return render(request, 'index.html' , {'form': form})
        else:
            form = InputNumberForm()
    responce = {'username': name,
                'magicpeople': magicpeople.add_answer(name),
                'form': form
                }
    return render(request, 'answer.html', context=responce)