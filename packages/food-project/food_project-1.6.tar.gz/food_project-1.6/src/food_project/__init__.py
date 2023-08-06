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

import food_project.meat.kotleta
from importlib import reload
reload(food_project.meat.kotleta)
import food_project.extra.sause
import food_project.extra.cheese
from food_project.extra.vegetables import Vegetables
vegs = Vegetables()
vegs('и')
from food_project.bread.bulo4ka.bulo4ka_s_kunjutom import bulo4ka, s_kunjutom
bulo4ka = s_kunjutom(bulo4ka)
bulo4ka(end=' ')

# print('lol\n\blol')

