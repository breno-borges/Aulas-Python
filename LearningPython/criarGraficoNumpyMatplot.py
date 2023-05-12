import numpy as np
import random as rd
import matplotlib.pyplot as plt

RA = 2222107276

rd.seed(RA)
quantidade = rd.randint(10, 30)

x = np.linspace(0, 30, quantidade)
y = [item * rd.randint(1,5) for item in range(quantidade)]

resultado = np.polyfit(x, y, 1)
correlacao = np.corrcoef(x, y)[0][1]

plt.title("Exemplo de Gráfico")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.plot(x, y, 'ob')

resposta = f'y = {resultado[0]:.4f}x {resultado[1]:.4f}'
resposta += f'\nPearson: {correlacao:.4f}'
plt.text(0.1, 0.9, resposta, transform = plt.gca().transAxes)

plt.show()