from solucion import Matricula

class PoliticaOTI:
    def registrar_matricula(self, nombre, extemporaneo, desaprobado, becado):
        matricula = Matricula(nombre)

        # Primero aplicamos los recargos
        if extemporaneo:
            matricula.agregar_extemporaneo()

        if desaprobado:
            matricula.agregar_indice()

        # Finalmente aplicamos la beca
        if becado:
            matricula.agregar_beca()

        return matricula


oti = PoliticaOTI()

# Registramos a los estudiantes
luis = oti.registrar_matricula(
    "Luis Huamani Cardenas", True, True, True
)

rosa = oti.registrar_matricula(
    "Rosa Ccahuana Prado", True, True, True
)

pedro = oti.registrar_matricula(
    "Pedro Quispe", True, False, True
)


for estudiante in [luis, rosa, pedro]:
    print(f"{estudiante.estudiante}: S/ {estudiante.costo():.2f}")


# Comprobamos que Luis y Rosa pagan lo mismo
if luis.costo() == rosa.costo():
    print("\nLuis y Rosa pagan el mismo monto.")
else:
    print("\nExiste una diferencia en los cobros.")