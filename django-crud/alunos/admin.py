from django.contrib import admin

# Register your models here.
from .models import Curso
from .models import Aluno

admin.site.register(Curso)
admin.site.register(Aluno)