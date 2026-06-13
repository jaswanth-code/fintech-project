# compute_metrics.py

import pandas as pd
import numpy as np

def sharpe_ratio(returns):
    return (returns.mean() / returns.std()) * np.sqrt(252)

def var_95(returns):
    return np.percentile(returns, 5)

def cvar_95(returns):
    var = np.percentile(returns, 5)
    return returns[returns <= var].mean()