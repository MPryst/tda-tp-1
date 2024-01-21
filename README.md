# tda-tp-1
Trabajo Práctico 1: Algoritmos Greedy

## Algoritmo
El algoritmo de solución recibe por parámetro la ubicación del archivo con los datos a resolver.
Y al terminar imprime la lista con el orden corespondiente, y la duración total del análisis.

En el código fuente se cuenta con un *ejemplo.dat*. Pare resolverlo se debe ejecutar:
```bash
python3 algoritmo.py ejemplo.dat
```


## Generador de horarios

Para generar una grilla de horarios, se ejecuta el script `generador.py` y se imprime por stdout el csv.

El uso del script es:
```bash
python3 generador.py <cantidad de columnas> [hora max] [seed]
```

Por ejemplo, sin pasarle una seed:

```bash
python3 src/generador.py 5
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
python3 src/generador.py 5 > archivo.csv
```

## Graficador
Utiliza al generador.py para generar sets de datos, y los resuelve utilizando algoritmo.py.
Recibe un valor por parametro, la semilla a utilizar en el generador. El tiempo máximo que le envía es 2000.
Genera valores desde 500k hasta 25M, con saltos de 500k.

Los datos son guardados en */data/i.dat*, siendo *i* el número de equipos.

El resultado final se guarda en */data/run-results.csv*, listo para abrirlo y generar un gráfico de tiempo de elementos vs tiempo de ejecución (milisegundos).


Cada ejecución sobreescribe los archivos.

### Ejemplo de uso, posicionado en /src:
```bash
./graficador.sh 0
```