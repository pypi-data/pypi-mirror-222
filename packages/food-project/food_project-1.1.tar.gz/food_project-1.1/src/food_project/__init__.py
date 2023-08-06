"""
мясная котлета гриль
мясная котлета гриль
специальный соус
сыр
огурцы
салат
и лук
булочка с кунжутом
"""
"""
Напишите программу, использующую
- import
- функции и классы, объявленные в текущем модуле
которая напечатает

мясная котлета гриль
мясная котлета гриль
специальный соус
сыр
огурцы
салат
и лук
булочка с кунжутом
"""

import meat.kotleta
from importlib import reload
reload(meat.kotleta)
import extra.sause
import extra.cheese
from extra.vegetables import Vegetables
vegs = Vegetables()
vegs('и')
from bread.bulo4ka.bulo4ka_s_kunjutom import bulo4ka, s_kunjutom
bulo4ka = s_kunjutom(bulo4ka)
bulo4ka(end=' ')

# print('lol\n\blol')

