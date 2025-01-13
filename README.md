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