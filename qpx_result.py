import pickle
from pyflight.results import Result
from results_printer import print_results

with open("results.pckl", "rb") as file:
    answer = pickle.load(file)

assert isinstance(answer, Result)

print_results(answer)

