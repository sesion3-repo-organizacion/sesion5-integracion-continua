# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import esPar

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_par(self):
        assert esPar(4) == "par"
        assert esPar(1) == "impar"
        assert esPar(2) == "par"
        assert esPar(3) == "impar"
