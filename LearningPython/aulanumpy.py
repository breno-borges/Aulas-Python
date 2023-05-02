import numpy as np

#Verificar a versão da biblioteca usada no código
print(np.__version__)

#Vetor
vetor = np.array([1,2,3,4,5])
print(vetor)

#Matriz
matriz = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(matriz)

#Ver o shape (Tamanho) do vetor e matriz
print(vetor.shape)
print(matriz.shape)

#Vetor e matriz com valores zero
vetor = np.zeros(5)
print(vetor)

matriz = np.zeros((2, 3))
print(matriz)

#Preencher com vazio
#OBS: O valor fica bem pequeno mas não é zero
#Noções de erros
vetor = np.empty(5)
print(vetor)

matriz = np.empty((2,3))
print(matriz)

#Cria um vetor de 0 ao tamanho do range (6) de 0 a 5 no caso
vetor = np.arange(6)
print(vetor)

#Numeros pares a patir do range (De o a 15, começando do 0 e de 2 em 2. (0, 15, 2))
vetor = np.arange(0, 15, 2)
print(vetor)

#De 0 a 10, contando de 4 em 4 números
vetor = np.linspace(0, 10, 4)
print(vetor)

matriz = vetor.reshape(1, 4)
print(matriz)

#Adicionando 1 ao vetor e convertendo o valor de float para int
vetor = np.ones(5, dtype= np.int32)
print(vetor)