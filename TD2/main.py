import re


def match_prenom_composer(prenom):
    if re.search(r"^[a-zA-Z]+-[a-zA-Z ]+$", prenom):
        return True

def match_domaine(domaine):
    if re.search(r"^[a-zA-Z]+\.[a-zA-Z]{2,3}$", domaine):
        return True

def nbr_de_bash(txt):
    count = 0
    list_de_gens=[]
    result = []
    with open(txt) as f:
        lines = f.readlines()
    for val in lines:
        if re.search(r"/bin/bash", val):
            count += 1
            list_de_gens.append(val)
    for ligne in list_de_gens:
        temptemp = ligne.split(':')
        result.append(temptemp[0])
    return f'{count} presonne(s) ont pour interpréteur bash: {result}'

def two_o_user(txt):
    result=[]
    two_o = []
    with open(txt) as f:
        lines = f.readlines()
    for val in lines:
        temptemp = val.split(':')
        result.append(temptemp[0])
    for val in result:
        if re.search(r"\w*o\w*o\w*", val):
            two_o.append(val)
    return f'les utilisateur ayant deux "o" dans leur nom sont {two_o}'

def test_mdp(mdp):
    if re.search(r"[a-zA-Z0-9+-?.*]*[A-Z]{2}[a-zA-Z0-9+-?.*]*[0-9]{3}[a-zA-Z0-9+-?.*]*[+-?.*][a-zA-Z0-9+-?.*]*", mdp):
            return True
print(nbr_de_bash('c:/Users/theso/Documents/python/R2.08/TD2/utilisateur.txt'))
print(two_o_user('c:/Users/theso/Documents/python/R2.08/TD2/utilisateur.txt'))
print(test_mdp(''))
#C:\Users\theso\Documents\python\R2.08\TD2