def printMenu():
    print("1. Citire date.")
    print("2. Determinare cea mai lungă subsecvență cu proprietatea ca numerele sunt neprime.")
    print("3. Determina cea mai lungă subsecvență cu proprietatea ca numerele sa fie formate din cifre prime.")
    print("4. Determina cea mai lunga subsecventa cu proprietatea ca numerele sa fie pare.")
    print("5. Iesire")


def citireLista():
    l = []
    givenString = input("Dati lista, cu elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l


def verificare_neprim(nr):
    '''
    Verificam daca nr este numar neprim
    :param nr: int, un numar din lista
    :return: True daca nr este neprim si False in caz contrar
    '''
    if nr<2:
       return True
    elif nr==2:
        return False
    elif nr%2==0:
        return True
    else:
        for i in range(3,nr//2+1,2):
            if nr%i==0:
                return True
        return False
def test_verificare_neprim():
    assert verificare_neprim(45) == True
    assert verificare_neprim(13) == False
test_verificare_neprim()


def neprime(lst):
    '''
    Verificam daca toate numerele din lista sunt neprime
    :param lst: int, lista
    :return: True daca lst are toate elementele neprime si False in caz contrar
    '''
    for element in lst:
        if verificare_neprim(element)== False:
            return False
    return True


def test_neprime():
    assert neprime([12,63,42,55, 81,1]) == True
    assert neprime([12,63,42,55, 81,2]) == False


def get_longest_all_not_prime(numere):
    '''
    Determina cea mai lunga secventa de numere neprime
    Daca sunt mai multe secvente de aceeasi lungime se va afisa prima gasita
    :param numere: int, lista cu numerele introduse
    :return: secventa maxima care indeplineste conditia
    '''
    secventa=[]
    for i in range(len(numere)):
        for j in range(i, len(numere)):
            considered = numere[i:j + 1]
            if neprime(considered):
                if len(secventa) < len(considered):
                    secventa = considered
    return secventa


def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([2,13,17,22, 81,5,3,6]) == [22, 81]
    assert get_longest_all_not_prime([2,13,17,22, 81,5,3,6,66,21,24,58,11]) == [6,66,21,24,58]


def get_longest_prime_digits(l):
    '''
    Determina cea mai lunga secventa ce are doar numere prime.
    :param l: lista cu numere
    :return: secventa cea mai lunga
    '''
    submax= []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if numere_prime(l[i:j+1]) and len(submax) < len(l[i:j+1]):
                submax= l[i:j+1]
    return submax


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([2,13,5,8,9]) == [2,13,5]
    assert get_longest_prime_digits([6,8,9]) == []
    assert get_longest_prime_digits([6,2,3,8,9,10,11,13,17]) == [11,13,17]


def numere_prime(l):
    '''
    Functie de arata daca toate elementele unui subliste sunt prime.
    :param l: sublista cu numere intregi
    :return: True daca toate elemntele sunt prime, False in caz contrar
    '''
    for a in l:
        while a != 0:
            c = a % 10
            if c == 0:
                return False
            for b in range(2,c // 2 + 1):
                if c % b == 0:
                    return False
            a = a//10
    return True


def numere_pare(l):
    """
    Functie ce returneaza True daca toate elementele unei subliste sunt pare.
    :param l: lista de numere
    :return: True daca toate sunt pare, False in caz contrar
    """
    for x in l:
        if x % 2 != 0:
            return False
    return True


def get_longest_all_even(l):
    """
    Determina cea mai lunga secventa care are toate numerele pare
    :param l: lista cu numerele
    :return: secventa cea mai lunga de numere
    """
    subsecmax=[]
    for i in range(len(l)):
        for j in range(i, len(l)):
            if numere_pare(l[i:j+1]) and len(subsecmax) < len(l[i:j+1]):
                subsecmax= l[i:j+1]
    return subsecmax


def test_get_longest_all_even():
    assert get_longest_all_even([2,4,6,8,9,]) == [2,4,6,8]
    assert get_longest_all_even([1,3,5]) == []
    assert get_longest_all_even([1,9,10,3]) == [10]


def main():
    l = []
    test_get_longest_all_not_prime()
    test_neprime()
    test_get_longest_all_even()
    test_get_longest_prime_digits()

    while True:
        printMenu()
        optiune = input("Dati obtiunea: ")
        if optiune == "1":
            l=citireLista()
        elif optiune == "2":
            print(get_longest_all_not_prime(l))
        elif optiune == "3":
            print(get_longest_prime_digits(l))
        elif optiune == "4":
            print(get_longest_all_even(l))
        elif optiune == "5":
            break
        else:
            print("Optiune gresita! Reincercati!")

main()
