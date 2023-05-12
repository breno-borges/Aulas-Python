import numpy as np

a = np.array([1, 2, 3])
print("Array")
print(a)
print("\n####################\n")

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print("\n####################\n")

###########################################
#Vetor e matriz preenchidas com zeros
vetor = np.zeros(2)
matriz = np.zeros((2, 3))

print("Zeros")
print(vetor)
print(matriz)
print("\n####################\n")

############################################
#Vetor e matriz preenchidos com um
vetor = np.ones(2, dtype = np.int64)
matriz = np.ones((5, 5), dtype = np.float32)

print("Ones")
print(vetor)
print(matriz)
print("\n####################\n")

############################################
#Vetor e matriz preenchidos com valores próximos de zero
vetor = np.empty(2)
matriz = np.empty((2, 5))

print("Empty")
print(vetor)
print(matriz)
print("\n####################\n")

############################################
#Vetor de 4 posições
vetor = np.arange(4)
matriz = vetor.reshape(2, 2)

print("Arange")
print(vetor)
print(matriz)
print("\n####################\n")

############################################
#Vetor começando de 2 a 9, contando de 2 em 2
vetor = np.arange(2, 9, 2)
print("\n####################\n")
print(vetor)
print("\n####################\n")

############################################
#Vetor e matriz de 0 a 10 , de 4 em 4 números
print("Linspace")
vetor = np.linspace(0, 10, num = 4)
print(vetor)
print("\n####################\n")

matriz = vetor.reshape(2, 2)
print(matriz)
print("\n####################\n")