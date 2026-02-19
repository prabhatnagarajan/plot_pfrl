import pandas as pd

def count_steps(score_file):
    scores = pd.read_csv(score_file, delimiter='\t')
    steps = scores['steps'].values
    return len(steps)