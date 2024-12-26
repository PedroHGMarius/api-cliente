from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'O número do CPF é inválido'})  

        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Não inclua números neste campo'})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'Este campo deve conter 8 dígitos'})

        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O celular precisa seguir este modelo 11 91234-1234 (respeitando os espaços e o traço)'})
        
        return data