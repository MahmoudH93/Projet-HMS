def chif_cesar(text):
    resultat = ''
    for char in text:
        resultat += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
    return resultat

print(chif_cesar('abc'))
