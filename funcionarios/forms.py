from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'nome',
            'cargo',
            'salario',
            'telefone',
            'email',
            'endereco',
            'contato_emergencia',
            'data_admissao',
            'data_demissao',
            'ativo',
        ]
        widgets = {
            'data_admissao': forms.DateInput(attrs={'type': 'date'}),
            'data_demissao': forms.DateInput(attrs={'type': 'date'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(00) 0 0000-0000', 'data-mask': '(00) 0 0000-0000'}),
        } 