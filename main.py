import multiprocessing
from process import process_BoursoBank_simulation, afficher_tableau

def fonction_a_executer(loanDuration, queue):
    # Remplacez cette fonction par votre logique
    print(f"Exécution avec loanDuration={loanDuration}")
    result = process_BoursoBank_simulation(loanDuration)
    queue.put(result)


if __name__ == "__main__":
    # Liste des paramètres pour chaque exécution
    parametres = [(f'{i} ans') for i in range(15, 26)]


    # Initialiser la queue pour collecter les résultats
    queue = multiprocessing.Queue()

    # Création d'une liste pour stocker les processus
    processus = []

    # Initialisation et démarrage des processus
    for params in parametres:
        p = multiprocessing.Process(target=fonction_a_executer, args=(params,queue))
        p.start()
        processus.append(p)

    # Attente de la fin de tous les processus
    for p in processus:
        p.join()

     # Récupérer les résultats de la queue
    resultats = []
    while not queue.empty():
        resultats.append(queue.get())

    resultats_triees = sorted(resultats, key=lambda x: x['Durée emprunt'])

    
    # Afficher les résultats sous forme de tableau
    afficher_tableau(resultats_triees)

    exit()




