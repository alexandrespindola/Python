import math
angulo_em_graus = float(input('Ângulo: '))
angulo_em_radianos = (angulo_em_graus * math.pi / 180.0)
sin = math.sin(angulo_em_radianos)
cos = math.cos(angulo_em_radianos)
tan = math.tan(angulo_em_radianos)
print(f'Seno = {sin:.2f}\nCosseno = {cos:.2f}\nTangente = {tan:.2f}')
