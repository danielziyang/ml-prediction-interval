from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.datasets import load_boston
import pandas as pd

data = load_boston()
boston = pd.DataFrame(data=data.data, columns = data.feature_names)

all(x in ['b', 'a', 'foo', 'bar'] for x in ['a', 'b'])

print(all(x in boston.columns for x in ['CRIM', 'ZM']))