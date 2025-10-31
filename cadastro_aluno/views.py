# # trata tabelas como se fosse objetos 
# # Model e orm

from cadastro_aluno.models import TbAlunos, TbEnderecos
import pandas as pd

qs = TbAlunos.objects.all().values()
df_alunos = pd.DataFrame(qs)


qs = TbEnderecos.objects.all().values()
df_enderecos = pd.DataFrame(qs)

# # criando filtro 
TbAlunos.objects.filter(id=16).values()

TbAlunos.objects.create(** {
                            'matricula': '99999',
                            'nome': 'laerte django',
                            'email': 'laert@ficticio.org',
                            'endereco_id': None,
                            'nome_mae': "laete"})



TbAlunos.objects.filter(id=16).delete()
TbAlunos.objects.filter(id=16).update(**{"nome_mae": "Dona Maria"})
