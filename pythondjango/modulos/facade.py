from typing import List

from pythondjango.modulos.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por parâmetro order
    """    

    return list(Modulo.objects.order_by('order').all())
    
    
    
    