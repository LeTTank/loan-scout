from simulation import process_BoursoBank_simulation
from utils import extract_loan_data

def processAllStuff(loanDuration, queue):
    print(f"Exécution avec loanDuration={loanDuration}")
    resultBourso = process_BoursoBank_simulation(loanDuration)
    print(resultBourso)
    result = extract_loan_data(resultBourso, loanDuration)
    print(result)
    queue.put(result)
