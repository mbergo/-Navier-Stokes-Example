i# Importar bibliotecas necessárias
import numpy as np

# Função para calcular o campo de velocidades
def calcular_velocidades(densidade, viscosidade, comprimento, pressao_gradiente):
    # Definir parâmetros
    num_pontos = 10  # Número de pontos no tubo
    delta_x = comprimento / (num_pontos - 1)  # Espaçamento entre os pontos

    # Inicializar matriz de velocidades
    velocidades = np.zeros(num_pontos)

    # Calcular velocidades em cada ponto
    for i in range(num_pontos):
        # Calcular velocidade no ponto i usando a equação de Navier-Stokes
        velocidade = (pressao_gradiente * i * delta_x) / (2 * densidade * viscosidade)
        velocidades[i] = velocidade

    return velocidades

# Inputs necessários:
densidade_fluido = 1.2  # Densidade do fluido (por exemplo, ar)
viscosidade_fluido = 0.001  # Viscosidade do fluido (por exemplo, ar)
comprimento_tubo = 1.0  # Comprimento do tubo em metros
gradiente_pressao = 10.0  # Gradiente de pressão aplicado ao longo do tubo

# Calcular o campo de velocidades
campo_velocidades = calcular_velocidades(densidade_fluido, viscosidade_fluido, comprimento_tubo, gradiente_pressao)

# Imprimir resultados
print("Campo de Velocidades:")
for i, velocidade in enumerate(campo_velocidades):
    print("Ponto", i, ":", velocidade, "m/s")

