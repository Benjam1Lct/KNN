def hamming(chaine1, chaine2):
    """
        Calcule la diatance de Hamming entre les deux chaines chaine1 et chaine2

        Enntrée : chaine 1 et chaine 2 deux chaines de carcatères

        Sortie : un entier
    """
    dist = 0
    for i in range(min(len(chaine1), len(chaine2))):
        if chaine1[i] != chaine2[i]:
            dist += 1
    return dist + abs(len(chaine1) - len(chaine2))

print(hamming('close', 'close'))