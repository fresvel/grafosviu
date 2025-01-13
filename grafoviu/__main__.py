import sys
from grafoviu.arista import Arista
from grafoviu.grafo import GrafoListasAdyacencia
from grafoviu.grafo import GrafoMatrizAdyacencia

def probar_aristas(grafo, aristas, caso="True"):
    for arista in aristas:
        resultado = "encontrada" if grafo.contiene_arista(arista) else "no encontrada"
        if (caso == "True" and resultado == "encontrada") or (caso == "False" and resultado == "no encontrada"):
            print(f"Arista {arista} correctamente {resultado} en el grafo")
        else:
            print(f"Error: Arista {arista} {resultado} cuando no se esperaba.")
def main():
    try:
        print("Bienvenido a grafoviu!")
        grafo_lista = GrafoListasAdyacencia("grafoviu/assets/grafo.txt")
        print("\nGrafo con listas de adyacencia:")
        print(grafo_lista)
        
        grafo_matriz = GrafoMatrizAdyacencia("grafoviu/assets/grafo.txt")
        print("\nGrafo con matriz de adyacencia:")
        print(grafo_matriz)

        # Aristas para pruebas
        aristas_true = [
            Arista("a", "b", 1),
            Arista("a", "c", 3),
            Arista("b", "e", 3),
            Arista("c", "a", 2),
            Arista("c", "d", 1),
            Arista("d", "a", 1),
            Arista("d", "e", 2),
            Arista("d", "f", 1),
            Arista("e", "c", 3),
            Arista("e", "f", 4),
            Arista("f", "g", 1),
            Arista("g", "b", 2)
        ]

        aristas_false = [
            Arista("a", "d", 5),
            Arista("b", "f", 7),
            Arista("c", "e", 4),
            Arista("d", "g", 6),
            Arista("e", "b", 2),
            Arista("f", "a", 8),
            Arista("g", "c", 9),
            Arista("a", "f", 3),
            Arista("t", "u", 2),
            Arista("k", "y", 7),
            Arista("f", "h", 1),
            Arista("h", "d", 5)
        ]
        
        # Probar aristas
        print("\n-----------------Testing Lists----------------")
        print("Testing True cases...")
        probar_aristas(grafo_lista, aristas_true, caso="True")
        
        print("\nTesting False cases...")
        probar_aristas(grafo_lista, aristas_false, caso="False")

        print("\n-----------------Testing Matrices----------------")
        print("Testing True cases...")
        probar_aristas(grafo_matriz, aristas_true, caso="True")
        
        print("\nTesting False cases...")
        probar_aristas(grafo_matriz, aristas_false, caso="False")

    except FileNotFoundError:
        print("Error: El archivo 'grafo.txt' no se encontró. Por favor, verifica la ruta del archivo.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
if __name__ == "__main__":
    sys.exit(main())
