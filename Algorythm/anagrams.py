def anagramsolution1(s1, s2):
    """
        Tworzy listę z pierwszego wyrazu która zapisuje w niej None jeślli było wystąpienie, jeśli nie przerywa
    """
    alist = list(s2)
    pos1 = 0
    stillOK = True
    
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK




print(anagramsolution1('abcd', 'dcba'))


