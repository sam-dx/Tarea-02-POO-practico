# Clase general para los ajustes
class Ajuste:
    def aplicar(self, monto):
        return monto


# Recargo por matricula fuera de fecha
class RecargoExtemporaneo(Ajuste):
    def aplicar(self, monto):
        return monto + 15


# Recargo por indice desaprobatorio
class RecargoIndice(Ajuste):
    def aplicar(self, monto):
        return monto + 15


# Descuento por beca
class Beca(Ajuste):
    def aplicar(self, monto):
        return monto / 2


# Clase matricula
class Matricula:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.ajustes = []

    def agregar_extemporaneo(self):
        self.ajustes.append(RecargoExtemporaneo())

    def agregar_indice(self):
        self.ajustes.append(RecargoIndice())

    def agregar_beca(self):
        self.ajustes.append(Beca())

    def costo(self):
        monto = 60.0

        for ajuste in self.ajustes:
            monto = ajuste.aplicar(monto)

        return monto


# Primera matricula
luis = Matricula("Luis Huamani Cardenas")

luis.agregar_extemporaneo()
luis.agregar_indice()
luis.agregar_beca()


# Segunda matricula
rosa = Matricula("Rosa Ccahuana Prado")

rosa.agregar_extemporaneo()
rosa.agregar_indice()
rosa.agregar_beca()


# Mostramos los resultados
if __name__ == "__main__":
    print("Estudiante:", luis.estudiante)
    print(f"Total: S/ {luis.costo():.2f}")

    print("\nEstudiante:", rosa.estudiante)
    print(f"Total: S/ {rosa.costo():.2f}")


    # Comprobamos que pagan lo mismo
    if luis.costo() == rosa.costo():
        print("\nAmbos estudiantes pagan el mismo monto.")
    else:
        print("\nLos estudiantes pagan montos diferentes.")


    # Prueba de otro orden de aplicacion
    prueba = Matricula("Matricula de prueba")

    prueba.agregar_beca()
    prueba.agregar_indice()
    prueba.agregar_extemporaneo()

    print("\nPRUEBA CON BECA PRIMERO")
    print(f"Total: S/ {prueba.costo():.2f}")
