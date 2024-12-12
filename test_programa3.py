import pytest
from programa3 import ManejadorClases

# Instalar pytest y coverage
# pip install pytest
# pip install coverage

# Ejecutar las pruebas
# pytest test_programa4.py

# Ejecutar las pruebas con cobertura
# coverage run -m pytest test_programa4.py

# Generar el reporte de cobertura en la terminal
# coverage report

@pytest.fixture
def manejador():
    return ManejadorClases()

def test_agregar_clase(manejador):
    manejador.agregar_clase("CLASS A f g")
    assert "A" in manejador.clases
    assert manejador.clases["A"]["metodos"] == {"f": "A", "g": "A"}

def test_agregar_clase_con_super(manejador):
    manejador.agregar_clase("CLASS A f g")
    manejador.agregar_clase("CLASS B : A h")
    assert "B" in manejador.clases
    assert manejador.clases["B"]["metodos"] == {"h": "B"}

def test_describir_clase(manejador, capsys):
    manejador.agregar_clase("CLASS A f g")
    manejador.agregar_clase("CLASS B : A h")
    manejador.agregar_clase("CLASS C : B i")
    manejador.describir_clase("C")
    captured = capsys.readouterr()
    assert "f -> A :: f" in captured.out
    assert "g -> A :: g" in captured.out
    assert "h -> B :: h" in captured.out
    assert "i -> C :: i" in captured.out

def test_add_class_with_errors(manejador, capsys):
    manejador.agregar_clase("CLASS A f g")
    manejador.agregar_clase("CLASS A h")
    captured = capsys.readouterr()
    assert "Error: La clase ya existe." in captured.out

    manejador.agregar_clase("CLASS B : C h")
    captured = capsys.readouterr()
    assert "Error: La super clase no existe." in captured.out

    manejador.agregar_clase("CLASS C f f")
    captured = capsys.readouterr()
    assert "Error: Métodos repetidos en la definición." in captured.out

def test_describir_clase_inexistente(manejador, capsys):
    manejador.describir_clase("Z")
    captured = capsys.readouterr()
    assert "Error: La clase no existe." in captured.out

def test_sobrescribir_metodo(manejador, capsys):
    manejador.agregar_clase("CLASS A f g")
    manejador.agregar_clase("CLASS B : A f h")
    manejador.describir_clase("B")
    captured = capsys.readouterr()
    assert "f -> B :: f" in captured.out
    assert "g -> A :: g" in captured.out
    assert "h -> B :: h" in captured.out