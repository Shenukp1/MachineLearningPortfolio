"""
This file is a proof of concept in using mlflow to track all the models ran.
The goal of this file is to do hyperparamter tuning.

The resources used for following example:
    1. https://towardsdatascience.com/an-intuitive-guide-to-track-your-ml-experiments-with-mlflow-7ac50e63b09-2/
    2. https://mlflow.org/docs/latest/ml/getting-started/quickstart/
"""

import numpy as np
import pandas as pd

# Constants
FS = 125
LABEL_COL = 187
RANDOM_SEED = 42
CLASSIFICATION_COL = 186

def preprocessing(df: pd.DataFrame) -> None:
    """A Training split is returned after preprocessing the data.
    
    Information regarding preprocessing:
        1. 
    """
