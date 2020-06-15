from rest_framework.viewsets import ModelViewSet

from solicitacoes.models import Solicitacao
from solicitacoes.serializers import SolicitacaoSerializer


class SolicitacoesViewSet(ModelViewSet):
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer