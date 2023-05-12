import numpy as np

temperature = [20, 25, 30, 35, 40, 45]
pressure = [280, 320, 370, 400, 430, 480]

alpha1, alpha2 = np.polyfit(temperature, pressure, 1)

corr_coef = np.corrcoef(temperature, pressure)[0][1]

print(f'A equação da curva é {alpha1}x {alpha2}')
print(f'O coeficiente de correlação é {corr_coef}')