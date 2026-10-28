
# SISTEMA DE MATRICULA UNSCH - 2026-II

# Creamos la clase principal
class Matricula:
    def __init__(self, estudiante):
        self.estudiante = estudiante

    def costo(self):
        return 60.0
    
# Matricula fuera de fecha
class MatriculaExtemporanea(Matricula):
    def costo(self):
        return super().costo() + 15

# Matricula con indice desaprobatorio
class MatriculaIndiceDesaprobatorio(Matricula):
    def costo(self):
        return super().costo() + 15

# Matricula con beca
class MatriculaBecado(Matricula):
    def costo(self):
        return super().costo() / 2


# Primera version
class VersionUno(MatriculaBecado,
                 MatriculaIndiceDesaprobatorio,
                 MatriculaExtemporanea):
    pass

# Segunda version
class VersionDos(MatriculaIndiceDesaprobatorio,
                 MatriculaExtemporanea,
                 MatriculaBecado):
    pass


# Creamos los objetos
luis = VersionUno("Luis Huamani Cardenas")
rosa = VersionDos("Rosa Ccahuana Prado")

# Mostramos los costos
print("\nPrimer programador:")
print("Estudiante:", luis.estudiante)
print(f"Costo: S/ {luis.costo():.2f}")

print("\nSegundo programador:")
print("Estudiante:", rosa.estudiante)
print(f"Costo: S/ {rosa.costo():.2f}")

# Mostramos el MRO
print("\nMRO de la primera version:")
for clase in VersionUno.__mro__:
    print(clase.__name__)

print("\nMRO de la segunda version:")
for clase in VersionDos.__mro__:
    print(clase.__name__)


# Diferencia de pagos
diferencia = abs(luis.costo() - rosa.costo())
print(f"\nDiferencia: S/ {diferencia:.2f}")
