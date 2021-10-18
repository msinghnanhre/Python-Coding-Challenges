str = 'We promptly judged antique ivory buckles for the prize'

def pangrams(s):
    stringData = s.lower()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    listarr = list(alph)
    for x in listarr:
        if x not in stringData:
            return 'not pangram'
    return 'pangram'

print(pangrams(str))