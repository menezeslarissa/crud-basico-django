from django.db import models
# Create your models here.
class Curso(models.Model):
	sigla = models.CharField(max_length=10)
	nome = models.CharField(max_length=200)

	def __str__(self):
		return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.nome