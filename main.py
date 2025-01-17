import logging
import multiprocessing
from process import processAllStuff
from utils import order_data


def main():
    logging.basicConfig(level=logging.INFO)

    # Liste des paramètres pour chaque exécution
    parametres = [(f'{i} ans') for i in range(15, 26)]

    # Initialiser la queue pour collecter les résultats
    queue = multiprocessing.Queue()

    # Création d'une liste pour stocker les processus
    processus = []

    # Initialisation et démarrage des processus
    for params in parametres:
        p = multiprocessing.Process(target=processAllStuff, args=(params,queue))
        p.start()
        processus.append(p)

    # Attente de la fin de tous les processus
    for p in processus:
        p.join()

     # Récupérer les résultats de la queue
    results = []
    while not queue.empty():
        results.append(queue.get())

    # Trier les résultats
    sorted_results = sorted(results, key=lambda x: x['Durée emprunt'])

    # Affichage des résultats sous forme de tableau
    order_data(sorted_results)


if __name__ == "__main__":
    main()
