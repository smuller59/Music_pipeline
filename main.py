import yaml
from pydub import AudioSegment
from typing import List

def charger_pistes(liste_path: List[str])-> List[AudioSegment]:
    resultat = []
    for chemin in liste_path:
        resultat.append(AudioSegment.from_wav(chemin))
    return resultat

def effet_echo(pistes: List[AudioSegment], delai=500)-> List[AudioSegment]:
    for index in range(len(pistes)):
        pistes[index] = pistes[index] * (pistes[index].silent(delai) + pistes[index])
    return pistes

def effet_inverser(pistes: List[AudioSegment], **kwargs)-> List[AudioSegment]:
    for index in range(len(pistes)):
        pistes[index] = pistes[index].reverse()
    return pistes

def effet_combiner(pistes: List[AudioSegment], **kwargs)-> List[AudioSegment]:
    resultat = pistes[0]
    for index in range(1,len(pistes)):
        resultat = resultat * pistes[index]
    return [resultat]


REGISTRY = {
    "effet_echo": effet_echo,
    "effet_inverser": effet_inverser,
    "effet_combiner": effet_combiner
}

with open("orchestration.yml", "r") as f:
    orchestration = yaml.safe_load(f)

for pipeline in orchestration.values():
    liste_pistes = []
    for etape in pipeline:
        if etape.get("load") is not None:
            liste_pistes = charger_pistes(etape["load"])
        elif etape.get("step") is not None:
            fct = REGISTRY[etape["step"]]
            params = etape.get("params", {})
            liste_pistes = fct(liste_pistes, **params)
        elif etape.get("export") is not None:
            for index in range(len(liste_pistes)):
                extension = etape["export"][index].split('.')[-1]
                liste_pistes[index].export(etape["export"][index], format=extension)