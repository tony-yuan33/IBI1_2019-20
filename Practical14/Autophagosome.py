# -*- coding: utf-8 -*-
from xml.dom.minidom import parse
from pandas import DataFrame

parents, table = {}, {}
id_strs, name_strs, defstrs = [], [], []
terms = parse("go_obo.xml").getElementsByTagName("term")

for term in terms:
    id_str = term.getElementsByTagName("id")[0].childNodes[0].data
    name_str = term.getElementsByTagName("name")[0].childNodes[0].data
    defstr = term.getElementsByTagName("def")[0].getElementsByTagName("defstr")[0].childNodes[0].data
    
    # Add parent strings
    parents[id_str] = []
    for parent in term.getElementsByTagName("is_a"):
        parents[id_str].append(parent.childNodes[0].data)
    
    if defstr.find("autophagosome") >= 0:
        id_strs.append(id_str)
        name_strs.append(name_str)
        defstrs.append(defstr)

def recursive_update_parents(idstr):
    if idstr != None:
        for parent in parents[idstr]:
            if table.get(parent) == None:
                table[parent] = 1
            else:
                table[parent] += 1
            recursive_update_parents(parent)

for term in terms:
    idstr = term.getElementsByTagName("id")[0].childNodes[0].data
    recursive_update_parents(idstr)

childnodes = [table.setdefault(idstr, 0) for idstr in id_strs]

df = DataFrame({'id':id_strs, 'name':name_strs, 'definition':defstrs, 'childnodes':childnodes})
df.to_excel("autophagosome.xlsx", index=False)