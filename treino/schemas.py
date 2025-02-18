from ninja import ModelSchema, Schema
from .models import Alunos
from typing import Optional

class AlunosSchema(ModelSchema):
    class Meta:
        model = Alunos
        fields = ['nome','email','data_nascimento','faixa']

class ProgressoAlunoSchema(Schema):
    email: str
    nome: str
    faixa: str
    total_aulas: int
    aulas_necessarias_para_proxima_faixa: int

class AulaRealizadaSchema(Schema):
    qtd: Optional[int]
    email_aluno: str
