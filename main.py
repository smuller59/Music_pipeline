import yaml
from pydub import AudioSegment
from typing import List

def charger_pistes(liste_path: List[str])-> List[AudioSegment]:
    """Charge une liste de fichiers audio WAV en tant qu'objets AudioSegment.

    Args:
        liste_path (List[str]): Une liste de chemins d'accès (strings) vers les fichiers WAV.

    Returns:
        List[AudioSegment]: Une liste d'objets AudioSegment chargés.

    Raises:
        FileNotFoundError: Si un chemin de fichier n'existe pas.
        pydub.exceptions.CouldntDecodeError: Si le fichier n'est pas un WAV valide.
    """
    resultat = []
    for chemin in liste_path:
        resultat.append(AudioSegment.from_wav(chemin))
    return resultat

def effet_echo(pistes: List[AudioSegment], delai=500)-> List[AudioSegment]:
    """Applique un effet d'écho simple à chaque piste audio.

    L'écho est créé en multipliant chaque piste par elle-même, précédée d'un silence.
    La formule appliquée est: piste * (silence + piste).

    Args:
        pistes (List[AudioSegment]): La liste des pistes AudioSegment à modifier.
        delai (int, optional): Le délai de l'écho en millisecondes.
                               Par défaut à 500 ms.

    Returns:
        List[AudioSegment]: La liste des pistes AudioSegment modifiées avec l'effet d'écho.
    """
    for index in range(len(pistes)):
        # pydub permet de multiplier un segment pour le répéter et d'utiliser '+' pour la concaténation
        pistes[index] = pistes[index] * (pistes[index].silent(delai) + pistes[index])
    return pistes

def effet_inverser(pistes: List[AudioSegment], **kwargs)-> List[AudioSegment]:
    """Inverse la lecture de chaque piste audio.

    Args:
        pistes (List[AudioSegment]): La liste des pistes AudioSegment à inverser.
        **kwargs: Arguments supplémentaires ignorés (pour la compatibilité avec le pipeline).

    Returns:
        List[AudioSegment]: La liste des pistes AudioSegment inversées.
    """
    for index in range(len(pistes)):
        pistes[index] = pistes[index].reverse()
    return pistes

def effet_combiner(pistes: List[AudioSegment], **kwargs)-> List[AudioSegment]:
    """Combine toutes les pistes audio en un seul segment en les superposant.

    La combinaison est effectuée par multiplication pydub (équivalent à la superposition
    mixée des pistes). Le résultat est une liste contenant une seule piste combinée.

    Args:
        pistes (List[AudioSegment]): La liste des pistes AudioSegment à combiner.
        **kwargs: Arguments supplémentaires ignorés (pour la compatibilité avec le pipeline).

    Returns:
        List[AudioSegment]: Une liste contenant un seul objet AudioSegment résultant de la combinaison.

    Raises:
        IndexError: Si la liste 'pistes' est vide.
    """
    if not pistes:
        return []
    resultat = pistes[0]
    for index in range(1,len(pistes)):
        # La multiplication pydub (*) combine les pistes en les superposant.
        resultat = resultat * pistes[index]
    return [resultat]


REGISTRY = {
    "effet_echo": effet_echo,
    "effet_inverser": effet_inverser,
    "effet_combiner": effet_combiner
}