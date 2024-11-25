from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from piloto.models import Aluno
from piloto.models.Aluno import Aluno
from piloto.models.Campus import Campus
from piloto.models.Curso import Curso

class ListaAlunosAPIView(APIView):
    def get(self, request, *args, **kwargs):
        alunos = Aluno.objects.all().values('id', 'nomeCompleto', 'cpf', 'matricula', 'ativo', 'curso__nome', 'curso__campus__nome')
        return Response(list(alunos), status=status.HTTP_200_OK)
