from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from piloto.models import Aluno
from piloto.serializers import AlunoSerializer

class ListaAlunosAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)
