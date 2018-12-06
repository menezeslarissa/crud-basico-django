from django.shortcuts import render
from .models import Aluno
from .form import AlunoForm
import datetime


def home(request):
    data={}
    data['now'] = datetime.datetime.now()
    data['transacoes'] = ['t1', 't2', 't3']
    #html = "<html><body>Isso é agora %s</body></html>" % now
    return render(request,'alunos/home.html', data)

def listagem(request):
    data={}
    data['alunos'] = Aluno.objects.all
    return render(request,'alunos/listagem.html', data)

def novo_aluno(request):
    data={}
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return listagem(request)
    data['form']=form
    return render(request,'alunos/form.html', data)

def update(request, pk):
    data = {}
    aluno = Aluno.objects.get(pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return listagem(request)
    data['form']=form
    data['aluno']= aluno
    return render(request,'alunos/form.html', data)

def delete(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    aluno.delete()
    return listagem(request)