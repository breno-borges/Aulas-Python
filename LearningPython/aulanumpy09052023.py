import numpy as np

x = [2, 5, 6, 9, 7, 8, 9, 10]
y = [5, 6, 9, 3, 1, 5, 6, 9]

#alpha1, alpha2 = np.polyfit(x, y, 1)

#print(f'A equação da curva é {alpha1}x {alpha2}')

x = np.array(x)
y = np.array(y)

#Calcular o coeficiente de correlação de Pearson entre x e y

corr_coef = np.corrcoef(x, y)[0][1]
print(corr_coef)
