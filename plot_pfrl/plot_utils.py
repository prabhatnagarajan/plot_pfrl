import numpy as np
from scipy.stats import norm
from pdb import set_trace

def compute_z_score(confidence_level):
    assert 0 < confidence_level < 1, "unsupported confidence level"
    return norm.ppf((1 + confidence_level) / 2)

def mean(curves):
    y_axis_values = [curve.values for curve in curves]
    mean_value = np.mean(np.stack(y_axis_values), axis=0)
    return mean_value

def compute_se(curves):
    num_datapoints = float(len(curves))
    y_axis_values = [curve.values for curve in curves]
    sample_std = np.std(np.stack(y_axis_values), axis=0, ddof=1)
    standard_error = sample_std / np.sqrt(num_datapoints)
    return standard_error
   

def compute_confidence_increment(curves, confidence_level=0.95):
    se = compute_se(curves)
    z_score = compute_z_score(confidence_level)
    confidence_increment = z_score * se
    return confidence_increment
