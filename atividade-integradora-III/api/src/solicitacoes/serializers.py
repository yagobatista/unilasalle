from rest_framework.serializers import ModelSerializer
from solicitacoes.models import Solicitacao

class SolicitacaoSerializer(ModelSerializer):
    class Meta:
        model= Solicitacao
        fields = '__all__'