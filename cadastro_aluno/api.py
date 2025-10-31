from ninja import Router
from cadastro_aluno.models import TbAlunos, TbEnderecos, TbNotas, TbDisciplinas
from typing import List
from cadastro_aluno.schemas import AlunosSchema, AlunoUpdate, AlunoCreate, EnderecosCreate, Enderecosconsulta, NotasConsulta, Disciplinasconsulta, NotasCreate, DisciplinasCreate, EnderecosUpdate
router = Router()


#-------------------------------------------------
# consultar --> método get 
#-------------------------------------------------

# consultar todos os endereços, todos os alunos, todas as notas e todas as disciplinas

@router.get("/consultar-alunos/")
def consultar_alunos(request):
    qs = TbAlunos.objects.all().values()
    return list(qs)


@router.get("/consultar-enderecos/")
def consultar_endereco(request):
    qs = TbEnderecos.objects.all().values()
    return list(qs)


@router.get("/consultar-notas/")
def consultar_endereco(request):
    qs = TbNotas.objects.all().values()
    return list(qs)


@router.get("/consultar-disciplinas/")
def consultar_disciplinas(request):
    qs = TbDisciplinas.objects.all().values()
    return list(qs)

# consultar um aluno ou um endereço ou uma nota ou uma disciplina pelo seu id 

@router.get("/aluno-por-id/{aluno_id}", response=list[AlunosSchema])
def consultar_aluno_id(request, aluno_id:int):
    qs = TbAlunos.objects.filter(id=aluno_id).all().values()
    return list(qs)


@router.get("/endereco-id/{id}", response=list[Enderecosconsulta])
def consultar_endereco_id(request, id:int):
    qs = TbEnderecos.objects.filter(id=id).all().values()
    return list(qs)


@router.get("/nota-por-aluno/{id}", response = list[NotasConsulta])
def consultar_nota_id(request, id:int):
    qs = TbNotas.objects.filter(id=id).all().values()
    return list(qs)


@router.get("/nota-por-aluno/{id}", response = list[Disciplinasconsulta])
def consultar_disciplina_id(request, id:int):
    qs = TbDisciplinas.objects.filter(id=id).all().values()
    return list(qs)

#-------------------------------------------------
# atualizar --> método put  
#-------------------------------------------------

@router.put("/alunos-por-id/{aluno_id}", response=dict)
def atualizar_aluno(request, aluno_id: int, dados: AlunoUpdate):
    atualizado = TbAlunos.objects.filter(id=aluno_id).update(**dados.dict())
    if atualizado:
        return {"mensagem": "Aluno atualizado com sucesso."}
    else:
        return {"erro": "Aluno não encontrado."}


@router.put("/endereco-por-id/{id}", response=dict[str, str])
def atualizar_endereco(request, id: int, dados: EnderecosUpdate):
    # Atualiza apenas os campos enviados no corpo da requisição
    dados_dict = dados.dict(exclude_unset=True)
    atualizado = TbEnderecos.objects.filter(id=id).update(**dados_dict)
    
    if atualizado:
        return {"mensagem": "Endereço atualizado com sucesso."}
    else:
        return {"erro": "Endereço não encontrado."}


#-------------------------------------------------
# Post --> método cadastrar
#-------------------------------------------------

@router.post("/aluno-cadastrado/", response=dict)
def cadastrar_aluno(request, dados: AlunoCreate):
    cadastrado = TbAlunos.objects.create(**dados.dict())
    if cadastrado:
        return {"mensagem": "Aluno cadastrado com sucesso."}
    else:
        return {"erro": "Aluno não cadastrado."}
    

@router.post("/endereco-cadastro/", response=dict)
def cadastrar_endereco(request, dados: EnderecosCreate):
    cadastrado = TbEnderecos.objects.create(**dados.dict())
    if cadastrado:
        return {"mensagem": "Endereço cadastrado com sucesso."}
    else:
        return {"erro": "Endereço não cadastrado."}

# nota tem chave secundaria e no json tem que entrar com a chave secundaria 
@router.post("/nota-cadastro/", response=dict)
def cadastrar_nota(request, dados: NotasCreate):
    cadastrado = TbNotas.objects.create(**dados.dict())
    if cadastrado:
        return {"mensagem": "Nota cadastrada com sucesso."}
    else:
        return {"erro": "Nota não cadastrada."}
    

@router.post("/disciplina-cadastro/", response=dict)
def cadastrar_disciplina(request, dados: DisciplinasCreate):
    cadastrado = TbDisciplinas.objects.create(**dados.dict())
    if cadastrado:
        return {"mensagem": "Disciplina cadastrada com sucesso."}
    else:
        return {"erro": "Disciplina não cadastrada."}

#-------------------------------------------------
# deletar --> método delete 
#-------------------------------------------------
@router.delete("/aluno-deletar/{aluno_id}", response=dict)
def deletar_aluno(request, aluno_id:int):
    qs = TbAlunos.objects.filter(id=aluno_id).delete()
    return {"mensagem": "Aluno deletado"}


@router.delete("/endereco-deletar/{id}", response= dict)
def deletar_endereco(request, id:int):
    qs = TbEnderecos.objects.filter(id=id).delete()
    return {"mensagem": "Endereço deletado"}

# testar notas no postman
@router.delete("/nota-deletar/{id}", response= dict)
def deletar_nota(request, id:int):
    qs = TbNotas.objects.filter(id=id).delete()
    return {"mensagem": "Nota deletada"}

@router.delete("/disciplina-deletar/{id}", response= dict)
def deletar_disciplina(request, id:int):
    qs = TbDisciplinas.objects.filter(id=id).delete()
    return {"mensagem": "Disciplina deletada"}