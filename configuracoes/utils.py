from .models import Parametro

def exibir_dados_ficticios():
    param = Parametro.objects.filter(chave='exibir_dados_ficticios').first()
    return bool(param and str(param.valor).lower() == 'true') 