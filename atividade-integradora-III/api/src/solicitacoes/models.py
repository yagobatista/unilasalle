from django.db.models import (PROTECT, CharField, DateTimeField, EmailField,
                              ForeignKey, ManyToManyField, Model,
                              PositiveSmallIntegerField, TextField, TimeField, CASCADE)

# atribuição de solicitação
# chat de mensagem


class Usuario(Model):
    email = EmailField(unique=True)
    nome = CharField('Nome do usuario', max_length=46)
    senha = CharField(max_length=100)


class Tecnico(Model):
    departamento = CharField('Departamento', max_length=46)


class AtribuicaoTecnico(Model):
    tecnico = ForeignKey('solicitacoes.Tecnico', on_delete=PROTECT)
    solicitacao = ForeignKey('solicitacoes.Solicitacao', on_delete=PROTECT)
    horario = DateTimeField('Horário da atribuição')


class Solicitacao(Model):
    descricao = TextField()
    status = ManyToManyField(
        'solicitacoes.Status',
        through='solicitacoes.MudancaStatus',
    )
    responsavel = ManyToManyField(
        'solicitacoes.Tecnico',
        through='solicitacoes.AtribuicaoTecnico',
    )
    usuario = ForeignKey('solicitacoes.Usuario', on_delete=PROTECT)


class Avaliacao(Model):
    solicitacao = ForeignKey('solicitacoes.Solicitacao', on_delete=CASCADE)
    satifacao = PositiveSmallIntegerField('Satifação com o atendimento')
    tempo = PositiveSmallIntegerField('Tempo da solução')
    qualidade = PositiveSmallIntegerField('Satifação qualidade da solução')


class Status(Model):
    nome = CharField('Nome do status', max_length=46)
    descricao = TextField()


class MudancaStatus(Model):
    solicitacao = ForeignKey('solicitacoes.Solicitacao', on_delete=CASCADE)
    status = ForeignKey('solicitacoes.Status', on_delete=PROTECT)
    horario = DateTimeField('Horário da mudança do status')
    descricao = TextField('Descrição')
    estimativa_tempo = TimeField('tempo estimado', null=True, blank=True)
