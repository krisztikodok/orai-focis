"""
csapatok

1.felsorolni a csapatokat
2.hányan vannak csapatokban
3.milyen posztok vannak
4.ki volt a leghatékonyabb
5.kapusok felsorolása,névsor szerint növekvő sorrendbe
6.soroljuk fel a posztokhoz rendelt neveket
pl. átlövő: x y, z zs
"""

import json

f=open('kezi.json')

data=json.load(f)

"""
for i in data["Pick Szeged"]:
  print(i)
"""

#1.
object_names = list(data.keys())
print(", ".join(object_names))

#2.


f.close()