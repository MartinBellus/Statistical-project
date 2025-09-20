import pandas as pd
from scipy import stats, linalg
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

def calculate_coefficients(df, *cols):
    X = []
    for d in df.to_dict(orient='records'):
        val = d['caffeine_mg']
        X.append(list(val if d[col] else 0 for col in cols))

    X = np.array(X)
    X = sm.add_constant(X)

    b = df['sleep_quality'].to_numpy()

    return sm.OLS(b, X).fit()


if __name__ == "__main__":
    dataset = pd.read_csv("./data/caffeine_intake_tracker.csv")

    coffee = dataset[dataset['beverage_coffee']]

    res = calculate_coefficients(coffee,
        'time_of_day_morning',
        'time_of_day_afternoon',
        'time_of_day_evening')

    print(res.summary())
