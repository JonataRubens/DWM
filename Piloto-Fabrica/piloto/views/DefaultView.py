from django.views.generic import TemplateView
from piloto.models import Aluno, Campus, Curso
from django.db.models import Count

class DefaultView(TemplateView):
    template_name = 'index/Index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Contar alunos, campi e cursos
        total_alunos = Aluno.objects.count()
        total_campus = Campus.objects.count()
        total_cursos = Curso.objects.count()
        total_ativo = Aluno.objects.filter(ativo=True).count()
        total_inativo = Aluno.objects.filter(ativo=False).count()

        
        # Obter a quantidade de alunos por campus
        # Aqui acessamos o campus através do curso relacionado ao aluno
        alunos_por_campus = Aluno.objects.values('curso__campus__nome').annotate(total=Count('curso__campus')).order_by('curso__campus__nome')
        
        campus_names = [campus['curso__campus__nome'] for campus in alunos_por_campus]
        alunos_counts = [campus['total'] for campus in alunos_por_campus]

        context['total_alunos'] = total_alunos
        context['total_campus'] = total_campus
        context['total_cursos'] = total_cursos
        context['campus_names'] = campus_names
        context['alunos_counts'] = alunos_counts
        context['total_ativo'] = total_ativo
        context['total_inativo'] = total_inativo
        
        return context
