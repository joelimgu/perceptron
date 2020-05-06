from numpy import random

nb0a = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]

nb0b = [[0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0]]

nb1a = [[0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0]]

nb1b = [[0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0]]

nb2a = [[1,1,1,1,1],
        [0,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,1]]

nb2b = [[1,1,1,1,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,1]]

nb3a = [[1,1,1,1,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [1,1,1,1,1],
        [0,0,0,0,1],
        [1,1,1,1,1]]

nb3b = [[1,1,1,1,1],
        [0,0,0,0,1],
        [1,1,1,1,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [1,1,1,1,1]]

nb4a = [[1,0,1,0,0],
        [1,0,1,0,0],
        [1,0,1,0,0],
        [1,1,1,1,1],
        [0,0,1,0,0],
        [0,0,1,0,0]]

nb4b = [[0,0,0,1,0],
        [0,0,1,1,0],
        [0,1,0,1,0],
        [1,1,1,1,1],
        [0,0,0,1,0],
        [0,0,0,1,0]]

nb5a = [[1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [1,1,1,1,1]]

nb5b = [[1,1,1,1,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,1],
        [0,0,0,0,1],
        [1,1,1,1,1]]

nb5c = [[1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,0],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [1,1,1,1,0]]

nb6a = [[1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]

nb6b = [[1,1,1,1,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]

nb6c = [[0,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0]]

nb7a = [[1,1,1,1,1],
        [0,0,0,0,1],
        [0,0,1,1,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [0,0,0,0,1]]

nb7b = [[1,1,1,1,1],
        [0,0,0,0,1],
        [0,0,0,1,0],
        [0,0,1,0,0],
        [0,1,0,0,0],
        [1,0,0,0,0]]

nb8a = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]

nb8b = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]

nb8c= [[0,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0]]

nb9a = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [1,1,1,1,1]]

nb9b = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [0,0,0,0,1],
        [1,1,1,1,1]]

nb9c = [[0,1,1,1,0],
        [1,0,0,0,1],
        [0,1,1,1,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [1,1,1,1,0]]


def flatten_matrice(m):
    ret = []
    for line in m:
        ret.extend(line)
    return ret


def structuration_donnees():
    matrices = []
    d = {0:[flatten_matrice(nb0a), flatten_matrice(nb0b)],
         1:[flatten_matrice(nb1a), flatten_matrice(nb1b)],
         2:[flatten_matrice(nb2a), flatten_matrice(nb2b)],
         3:[flatten_matrice(nb3a),flatten_matrice(nb3b)],
         4:[flatten_matrice(nb4a),flatten_matrice(nb4b)],
         5:[flatten_matrice(nb5a),flatten_matrice(nb5b), flatten_matrice(nb5c)],
         6:[flatten_matrice(nb6a),flatten_matrice(nb6b),flatten_matrice(nb6c)],
         7:[flatten_matrice(nb7a),flatten_matrice(nb7b)],
         8:[flatten_matrice(nb8a),flatten_matrice(nb8b),flatten_matrice(nb8c)],
         9:[flatten_matrice(nb9a),flatten_matrice(nb9b),flatten_matrice(nb9c)]}
    return d


def print_diese():
    print("#", end="")


def print_espace():
    print(" ", end="")


def print_saut_de_ligne():
    print("")


def print_matrice(m):
    i = 0
    for case in m:
        if case == 1:
            print_diese()
        else:
            print_espace()
        i += 1
        if i%5 == 0:
            print_saut_de_ligne()


d = structuration_donnees()
# print_matrice(d[9][2])


def init_poids(dim_entree, dim_sortie):
    random.seed(2)
    poids = []
    for d_entree in range(dim_entree):
        lst = []
        for d_sortie in range(dim_sortie):
            lst.append(100*random.random()-50)
        poids.append(lst)
    return poids

#poids = init_poids(30,10)
#print(poids[25])


def calcul_neurone(j, e, poids):
    result = 0
    for i in range(len(e)): # basically 30 cause weighted 'link' to  neuron for each position
        # 30x10 ==> premier element = poids de chaque case pour le neurone 1
        # representer la matrice ==> on prend la colonne j et on itere sur les lignes
        result += e[i]*poids[i][j]
        resultat = int(result > 0)
    return resultat

#print(calcul_neurone(3,d[9][0],poids))
#print(calcul_neurone(9,d[9][0],poids))


def calcul_reseau(e,poids):
    return [calcul_neurone(neuron, e, poids) for neuron in range(10)]


#sortie = calcul_reseau(d[9][0],poids)
#print(sortie)


def apprendre_neurone(e, poids, j, sortie_attendue):
    h = 5
    valeur_calculee = calcul_neurone(j, e, poids)
    for i in range(len(poids)):
        valeur_desiree = 0
        if sortie_attendue == j:
            valeur_desiree = 1
        poids[i][j] = poids[i][j] + (valeur_desiree - valeur_calculee) * e[i] * h
    return poids


def apprendre_reseau(e, poids, sortie_attendue):
    for neuron in range(10):
        apprendre_neurone(e, poids, neuron, sortie_attendue)



def apprendre(d, poids):
    for key in d:
        for number_specific in d[key]:
            apprendre_reseau(number_specific, poids, key)


def saisir_chiffre_matrice():
    lst = [[0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0]]
    ipt = ""
    print("Please insert binaries to create a number in a 6x5 matrix")
    for ligne in range(6):
        for colonne in range(5):
            lst[ligne][colonne] = eval(input(ipt))
    return lst


nb3a_bruite = [[1,1,1,1,1],
        [0,0,1,0,1],
        [0,0,0,0,1],
        [1,1,1,1,1],
        [0,0,0,1,1],
        [1,1,1,1,1]]

def main():
    d = structuration_donnees()
    poids_neurones = init_poids(30, 10)
    for i in range(1000):
        apprendre(d, poids_neurones)
    # entree = saisir_chiffre_matrice()
    flat_input = flatten_matrice(nb3a_bruite)
    output = calcul_reseau(flat_input,poids_neurones)
    print(output)

main()