# Štatistická práca - Martin Belluš - Coffeine Effect on Sleep

---

## Korelácia kofeínu a spánku

Ako prvé sa pozriem, či existuje korelácia medzi množstvom skonzumovaného
kofeínu (`caffeine_mg`) a kvalitou spánku (`sleep_quality`). Dáta rozdelím podľa
toho, či sa jedná o kávu alebo čaj.

*Nulová hypotéza*: Neexistuje korelácia medzi množstvom skonzumovaného kofeínu a
kvalitou spánku.

*Alternatívna hypotéza*: Existuje negatívna korelácia medzi množstvom
skonzumovaného kofeínu a kvalitou spánku.

Na testovanie použijem Pearsonov koeficient.

Zdrojový kód testu sa nachádza v súbore [src/correlation.py](./src/correlation.py)

Výsledok testu:

```
Coffee - Testing correlation between caffeine_mg and sleep_quality
Pearson correlation: r = -0.320, p = 5.264505197063971e-08

Tea - Testing correlation between caffeine_mg and sleep_quality
Pearson correlation: r = 0.082, p = 0.8697615652798727
```

Pearsonov koeficient pre čaj je nečakane kladný, preto spravím ešte test pre
alternatívnu hypotézu, že čaj má pozitívnu koreláciu s kvalitou spánku.
Výsledok:

```
Tea Positive - Testing correlation between caffeine_mg and sleep_quality
Pearson correlation: r = 0.082, p = 0.13023843472012667
```

Hodnota p pre kávu je väčšia ako 0.05, preto zamietam nulovú hypotézu. Teda
existuje silná negatívna korelácia medzi množstvom skonzumovaného kofeínu z kávy
a kvalitou spánku.

Pre čaj je hodnota p menšia ako 0.05, preto nulovú hypotézu nemôžem zamietnuť.

Na záver ešte vykreslím grafy kvality spánku v závislosti od množstva kofeínu:

![Coffee](./img/coffee_plot.png)

![Tea](./img/tea_plot.png)

## Vplyv času konzumácie kofeínu na kvalitu spánku

Teraz sa zameriam na to, či a ako veľmi vplýva čas konzumácie kávy na kvalitu
spánku. Na to použijem lineárnu regresiu.

*Nulová hypotéza*: Neexistuje lineárna závyslosť medzi časom konzumácie kávy a
kvalitou spánku.

Budem chcieť spočítať koeficienty rovnice `sleep_quality = x1 *
morning_caffeine_mg + x2 * afternoon_caffeine_mg + x3 * evening_caffeine_mg +
b`.

Zdrojový kód testu sa nachádza v súbore
[src/regression.py](./src/regression.py).

Výsledok testu:

```
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.123
Model:                            OLS   Adj. R-squared:                  0.113
Method:                 Least Squares   F-statistic:                     12.22
Date:                Sat, 20 Sep 2025   Prob (F-statistic):           1.65e-07
Time:                        16:59:38   Log-Likelihood:                 22.814
No. Observations:                 265   AIC:                            -37.63
Df Residuals:                     261   BIC:                            -23.31
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.7781      0.042     18.530      0.000       0.695       0.861
x1            -0.4739      0.092     -5.129      0.000      -0.656      -0.292
x2            -0.4157      0.100     -4.172      0.000      -0.612      -0.220
x3            -0.6211      0.105     -5.909      0.000      -0.828      -0.414
==============================================================================
Omnibus:                        6.516   Durbin-Watson:                   1.905
Prob(Omnibus):                  0.038   Jarque-Bera (JB):                6.473
Skew:                          -0.382   Prob(JB):                       0.0393
Kurtosis:                       3.044   Cond. No.                         12.0
==============================================================================
```

Z výsledku vidno, že medzi dátami existuje lineárna závislosť (hodnota `Prob
(F-statistic)` je menšia ako 0.05). Teda môžem zamietnuť nulovú hypotézu.

Zároveň všetky koeficienty sú štatisticky významné (hodnoty `P>|t|` sú menšie
ako 0.05). Z jednotlivých koeficientov môžem usúdiť, že káva vypitá večer má
najhorší vplyv na kvalitu spánku (čo sa aj dalo očakávať).
