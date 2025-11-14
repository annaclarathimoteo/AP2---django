# isso serve para a gnt retornar so o que queremos 

from ninja import Schema
from typing import Optional

class AlunosSchema(Schema):
    nome: str
    email: Optional[str]
    nome_mae: Optional[str] = None # esse optional é para quando tiver nulo nao dar erro 


# Modelo Pydantic para atualizar aluno (todos opcionais)
class AlunoUpdate(Schema):
    matricula: Optional[str] = None
    nome: Optional[str] = None
    email: Optional[str] = None
    endereco_id: Optional[int] = None


class AlunoCreate(Schema):
    matricula: Optional[str] = None
    nome: Optional[str] = None
    email: Optional[str] = None
    endereco_id: Optional[int] = None
    nome_mae: Optional[str] = None




class EnderecosCreate(Schema):
    cep : Optional[str] = None
    endereco : Optional[str] = None
    bairro : Optional[str] = None
    cidade : Optional[str] = None
    estado : Optional[str] = None
    regiao : Optional[str] = None


class Enderecosconsulta(Schema):
    cep : Optional[str] = None
    endereco : Optional[str] = None
    bairro : Optional[str] = None
    cidade : Optional[str] = None
    estado : Optional[str] = None
    regiao : Optional[str] = None


class EnderecosUpdate(Schema):
    cep : Optional[str] = None
    endereco : Optional[str] = None
    bairro : Optional[str] = None
    cidade : Optional[str] = None
    estado : Optional[str] = None
    regiao : Optional[str] = None


class NotasConsulta(Schema):
    aluno : Optional[str] = None
    disciplina : Optional[str] = None
    nota : Optional[float] = None

class NotasCreate(Schema):
    aluno_id : Optional[int] = None
    disciplina_id : Optional[int] = None
    nota : Optional[float] = None

class NotasUpdate(Schema):
    aluno : Optional[int] = None
    disciplina : Optional[int] = None
    nota : Optional[float] = None

class Disciplinasconsulta(Schema):
    disciplina : Optional[str] = None
    carga : Optional[int] = None
    semestre : Optional[int] = None

class DisciplinasCreate(Schema):
    disciplina : Optional[str] = None
    carga : Optional[int] = None
    semestre : Optional[int] = None


class DisciplinasUpdate(Schema):
    disciplina : Optional[str] = None
    carga : Optional[int] = None
    semestre : Optional[int] = None


    