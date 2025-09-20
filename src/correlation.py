import pandas as pd
from scipy import stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation(df, drink, col1 = "caffeine_mg", col2 = "sleep_quality"):
    title = f"{drink}: Caffeine vs Sleep Quality"
    sns.scatterplot(data=df, x=col1, y=col2)
    plt.title(title)

    plt.savefig(f"img/{drink.lower()}_plot.png")
    plt.clf()

def statistical_test(df, drink, alternative = 'less', col1 = "caffeine_mg", col2 = "sleep_quality"):
    r, p_value = stats.pearsonr(df[col1], df[col2], alternative=alternative)
    print(f"{drink} - Testing correlation between {col1} and {col2}")
    print(f"Pearson correlation: r = {r:.3f}, p = {p_value}")

    print()

if __name__ == "__main__":

    dataset = pd.read_csv("./data/caffeine_intake_tracker.csv")

    coffee = dataset[dataset['beverage_coffee']]
    tea = dataset[dataset['beverage_tea']]

    statistical_test(coffee, "Coffee")
    statistical_test(tea, "Tea")
    statistical_test(tea, "Tea Positive", 'greater')


    plot_correlation(coffee, "Coffee")
    plot_correlation(tea, "Tea")
