import yaml
from pydub import AudioSegment
from typing import List

def effet_echo(pistes: List[AudioSegment], delai=500)-> List[AudioSegment]:
    for index in range(len(pistes)):
        pistes[index] = pistes[index] * (pistes[index].silent(delai) + pistes[index])
    return pistes

def effet_inverser(pistes: List[AudioSegment], kwargs)-> List[AudioSegment]:
    for index in range(len(pistes)):
        pistes[index] = pistes[index].reverse()
    return pistes

def effet_combiner(pistes: List[AudioSegment], kwargs)-> List[AudioSegment]:
    resultat = pistes[0]
    for index in range(1,len(pistes)):
        resultat = resultat * pistes[index]
    return [resultat]



audio_entree = AudioSegment.from_wav("input/monologue.wav")
pistes = [audio_entree]
pistes = effet_echo(pistes, {"delai": 300})
pistes = effet_inverser(pistes, {})
pistes = effet_combiner(pistes, **{})
pistes[0].export("output/resultat.wav", format="wav")

# Une petite “registry” de fonctions
REGISTRY = {
    "effet_echo": effet_echo,
    "effet_inverser": effet_inverser,
    "effet_combiner": effet_combiner
}

with open("pipeline.yaml", "r") as f:
    config = yaml.safe_load(f)

audio = "mon_audio"

for step in config["pipeline"]:
    fn_name = step["step"]
    params = step.get("params", {})

    fn = REGISTRY[fn_name]  # Récupère la fonction Python
    audio = fn(audio, **params)
