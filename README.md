# Librería grafoviu

Esta librería proporciona funcionalidades para la creación y manipulación de grafos, implementando dos representaciones principales: listas de adyacencia y matrices de adyacencia.

## Módulos

La librería se compone de los siguientes módulos:

- **arista.py**: Define la clase `Arista` para representar las aristas del grafo.
- **grafo.py**: Define las clases abstractas `Grafo` y las implementaciones concretas `GrafoListasAdyacencia` y `GrafoMatrizAdyacencia` para la representación de grafos.

## Clase `Arista`

### Descripción
Representa una arista en un grafo, con un nodo de origen, un nodo de destino y un peso asociado.

### Atributos

- `__origen`: El nodo de origen de la arista.
- `__destino`: El nodo de destino de la arista.
- `__peso`: El peso asociado a la arista.

### Métodos

- `__init__(self, origen, destino, peso)`: Constructor de la clase. Inicializa una arista con su origen, destino y peso.
- `__str__(self)`: Retorna una representación en cadena de la arista en el formato `|(origen, destino, peso)|`.
- `get_arista(self)`: Retorna una tupla con el origen, destino y peso de la arista.
- `peso(self)`: Propiedad que devuelve el peso de la arista.
- `origen(self)`: Propiedad que devuelve el origen de la arista.
- `destino(self)`: Propiedad que devuelve el destino de la arista.

## Clase abstracta `Grafo`

### Descripción
Define la interfaz común para las representaciones de grafos. No puede ser instanciada directamente.

### Atributos

- `__nodes`: Un conjunto de nodos únicos presentes en el grafo.
- `__node_index`: Diccionario que asigna un índice a cada nodo del grafo.

### Métodos

- `__init__(self, path_file)`: Constructor de la clase abstracta. Lee un archivo de texto donde cada línea representa una arista en el formato "origen destino peso", inicializa el conjunto de nodos, y llama a `aniadir_arista` para cada arista.
- `aniadir_arista(self, arista)`: Método abstracto para añadir una arista al grafo. Debe ser implementado por las clases concretas.
- `contiene_arista(self, arista)`: Método abstracto para verificar si una arista existe en el grafo. Debe ser implementado por las clases concretas.

## Clase `GrafoListasAdyacencia`

### Descripción
Implementa la representación de un grafo usando listas de adyacencia.

### Atributos

- `__grafo`: Un diccionario donde las claves son los nodos de origen y los valores son listas de tuplas `(destino, peso)` que representan las aristas salientes del nodo origen.

### Métodos

- `__init__(self, path_file)`: Constructor de la clase. Inicializa el grafo llamando al constructor de la clase padre `Grafo` e inicializando el diccionario que representa el grafo con listas de adyacencia.
- `aniadir_arista(self, arista)`: Añade una arista al grafo. Agrega el destino y peso a la lista de adyacencia del nodo origen.
- `contiene_arista(self, arista)`: Verifica si una arista existe en el grafo. Retorna `True` si el destino y el peso de la arista se encuentran en la lista de adyacencia del origen, y `False` en caso contrario.
- `__str__(self)`: Retorna una representación en cadena del grafo en el formato `{nodo: [(destino, peso), ...], ...}`.

## Clase `GrafoMatrizAdyacencia`

### Descripción
Implementa la representación de un grafo usando una matriz de adyacencia.

### Atributos

- `__grafo`: Una matriz bidimensional que representa las conexiones entre nodos. Cada celda `[i][j]` contiene el peso de la arista entre el nodo con índice `i` y el nodo con índice `j`. `0` indica que no hay arista.
- `__node_index`: Diccionario que mapea nodos a índices de la matriz.

### Métodos

- `__init__(self, path_file)`: Constructor de la clase. Inicializa el grafo llamando al constructor de la clase padre `Grafo` e inicializa la matriz a `None`.
- `aniadir_arista(self, arista)`: Añade una arista al grafo. Si la matriz aún no ha sido inicializada, la crea. Luego, establece el peso en la celda correspondiente.
- `contiene_arista(self, arista)`: Verifica si una arista existe en el grafo. Retorna `True` si el peso de la arista en la matriz es diferente de `0`, y `False` en caso contrario.
- `__str__(self)`: Retorna una representación en cadena de la matriz del grafo, mostrando los nodos en la primera fila y columna, y los pesos de las aristas en la matriz.

## Función `probar_aristas`

### Descripción
Función para probar la funcionalidad de `contiene_arista` de un grafo con una lista de aristas, ya sea para casos donde deberían existir (caso="True") o donde no deberían existir (caso="False").

### Parámetros

- `grafo`: Instancia de un grafo (`GrafoListasAdyacencia` o `GrafoMatrizAdyacencia`).
- `aristas`: Lista de objetos `Arista` para probar.
- `caso`: Cadena que puede ser `"True"` o `"False"` para indicar qué tipo de prueba se realiza.

## Función `main`

### Descripción
Función principal que:

- Crea instancias de `GrafoListasAdyacencia` y `GrafoMatrizAdyacencia` a partir del archivo `grafo.txt`.
- Define listas de aristas `aristas_true` (que deben existir en el grafo) y `aristas_false` (que no deben existir).
- Llama a la función `probar_aristas` para verificar la correcta implementación de la función `contiene_arista`.
- Maneja excepciones `FileNotFoundError` si el archivo `grafo.txt` no se encuentra, y `Exception` para errores inesperados.

## Ejecución del programa

El script principal ejecuta la función `main` al ser invocado, comenzando la ejecución de pruebas de creación de grafos y validación de la existencia de aristas.

---

Este documento proporciona una visión general de la librería **grafoviu** y su funcionalidad, permitiendo a los usuarios comprender cómo utilizarla para crear y manipular grafos.

El programa se ha desarrollado en un entornos linux y para su ejecución es necesario utilizar `pipenv shell` junto a `pipenv install .`. Para el funcionamiento del programa se utiliza el archivo grafo.txt ubicado en assets por lo que para probar el código se debe ejecutar `grafoviu` desde la raiz del proyecto.

### Salida esperada

```plaintext
Grafo con listas de adyacencia:
{
a : [('b', 1), ('c', 3)]
b : [('e', 3)]
c : [('a', 2), ('d', 1)]
d : [('a', 1), ('e', 2), ('f', 1)]
e : [('c', 3), ('f', 4)]
f : [('g', 1)]
g : [('b', 2)]
}

Grafo con matriz de adyacencia:
  a b c d e f g 
a 0 1 3 0 0 0 0 
b 0 0 0 0 3 0 0 
c 2 0 0 1 0 0 0 
d 1 0 0 0 2 1 0 
e 0 0 3 0 0 4 0 
f 0 0 0 0 0 0 1 
g 0 2 0 0 0 0 0 


-----------------Testing Lists----------------
Testing True cases...
Arista |('a', 'b', 1)| correctamente encontrada en el grafo
Arista |('a', 'c', 3)| correctamente encontrada en el grafo
Arista |('b', 'e', 3)| correctamente encontrada en el grafo
Arista |('c', 'a', 2)| correctamente encontrada en el grafo
Arista |('c', 'd', 1)| correctamente encontrada en el grafo
Arista |('d', 'a', 1)| correctamente encontrada en el grafo
Arista |('d', 'e', 2)| correctamente encontrada en el grafo
Arista |('d', 'f', 1)| correctamente encontrada en el grafo
Arista |('e', 'c', 3)| correctamente encontrada en el grafo
Arista |('e', 'f', 4)| correctamente encontrada en el grafo
Arista |('f', 'g', 1)| correctamente encontrada en el grafo
Arista |('g', 'b', 2)| correctamente encontrada en el grafo

Testing False cases...
Arista |('a', 'd', 5)| correctamente no encontrada en el grafo
Arista |('b', 'f', 7)| correctamente no encontrada en el grafo
Arista |('c', 'e', 4)| correctamente no encontrada en el grafo
Arista |('d', 'g', 6)| correctamente no encontrada en el grafo
Arista |('e', 'b', 2)| correctamente no encontrada en el grafo
Arista |('f', 'a', 8)| correctamente no encontrada en el grafo
Arista |('g', 'c', 9)| correctamente no encontrada en el grafo
Arista |('a', 'f', 3)| correctamente no encontrada en el grafo
Arista |('t', 'u', 2)| correctamente no encontrada en el grafo
Arista |('k', 'y', 7)| correctamente no encontrada en el grafo
Arista |('f', 'h', 1)| correctamente no encontrada en el grafo
Arista |('h', 'd', 5)| correctamente no encontrada en el grafo

-----------------Testing Matrices----------------
Testing True cases...
Arista |('a', 'b', 1)| correctamente encontrada en el grafo
Arista |('a', 'c', 3)| correctamente encontrada en el grafo
Arista |('b', 'e', 3)| correctamente encontrada en el grafo
Arista |('c', 'a', 2)| correctamente encontrada en el grafo
Arista |('c', 'd', 1)| correctamente encontrada en el grafo
Arista |('d', 'a', 1)| correctamente encontrada en el grafo
Arista |('d', 'e', 2)| correctamente encontrada en el grafo
Arista |('d', 'f', 1)| correctamente encontrada en el grafo
Arista |('e', 'c', 3)| correctamente encontrada en el grafo
Arista |('e', 'f', 4)| correctamente encontrada en el grafo
Arista |('f', 'g', 1)| correctamente encontrada en el grafo
```