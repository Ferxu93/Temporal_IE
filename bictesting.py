from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.arima_model import ARMA
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ar = np.array([1, 0.9])
ma = np.array([1, 0])
AR_object = ArmaProcess(ar, ma)
Simulated_data = AR_object.generate_sample(nsample=5000)
print('This is my ARMA simulation:', Simulated_data)

bic_serie = []
for p in range(1, 3):
    for phi in np.arange(0.1, 0.9, 0.1):
        q = p
        ar = np.array([p, phi])
        ma = np.array([q, phi - 0.1])
        AR_object = ArmaProcess(ar, ma)
        simulated_data = AR_object.generate_sample(nsample=5000)
        print(simulated_data)

        model = ARMA(simulated_data, order=(p, q))
        model_trained = model.fit()
        print('bic: ', model_trained.bic)
        bic_serie.append(model_trained.bic)

plt.plot(pd.Series(bic_serie))
plt.show()