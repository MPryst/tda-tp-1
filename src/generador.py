import sys
import random 

def params_invalidos():
  print('Uso: python generador.py <cantidad de columnas> [hora max] [seed]')
  exit(1)

def parsear_params():
  if (len(sys.argv) < 2):
    params_invalidos()

  cantidad = int(sys.argv[1])

  if (cantidad < 2):
    params_invalidos()

  if (len(sys.argv) > 2):
    hora_max = int(sys.argv[2])
  else:
    hora_max = cantidad

  if (len(sys.argv) > 3):
    seed = sys.argv[3]
  else:
    seed = None

  return cantidad, hora_max, seed

def generar_horario(max):
  hora_scaloni = random.randint(1, max)
  hora_ayudante = random.randint(1, max)
  return str(hora_scaloni) + ',' + str(hora_ayudante)

def main():
  cantidad, hora_max, seed = parsear_params()

  if (seed):
    random.seed(seed)

  # Header
  print('S_i,A_i')
  # Horarios
  for i in range(0, cantidad):
    print(generar_horario(hora_max))

main()