from django.forms import ModelForm
from .models import Aluno

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','matricula', 'curso']