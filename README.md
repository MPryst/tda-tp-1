# tda-tp-1
Trabajo Práctico 1: Algoritmos Greedy

## Generador de horarios

Para generar una grilla de horarios, se ejecuta el script `generador.py` y se imprime por stdout el csv.

El uso del script es:
```bash
python generador.py <cantidad de columnas> [hora max] [seed]
```

Por ejemplo, sin pasarle una seed:

```bash
python src/generador.py 5
```

Devolvería por ejemplo

```
S_i,A_i
2,4
4,1
2,2
5,4
5,1
```

Para generar un archivo que después se pueda usar en el algoritmo principal, se puede ejecutar redireccionando el stream:

```bash
python src/generador.py 5 > archivo.csv
```
