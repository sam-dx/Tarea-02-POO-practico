# Tarea 02 - Programacion Orientada a Objetos

## Descripcion

En este trabajo resolvi un problema de matricula de la UNSCH, donde dos estudiantes tenian las mismas condiciones pero pagaban montos diferentes por el orden de las clases.

Para esto hice 3 archivos en Python, donde primero muestro el problema y despues intento solucionarlo.

## Archivos

- **main.py:** Aqui muestro el problema usando herencia multiple, donde el orden de las clases cambia el resultado.
- **solucion.py:** En este archivo use composicion, guardando los recargos y la beca en una lista para poder elegir el orden.
- **politica_oti.py:** Es una mejora donde la OTI establece un mismo orden de cobro para todos los estudiantes.

## Resultados

En el primer codigo los resultados fueron:

- Luis Huamani Cardenas: S/ 45.00
- Rosa Ccahuana Prado: S/ 60.00

La diferencia fue de S/ 15.00, esto pasa por que el orden en que se hacen los calculos es diferente.

En la ultima solucion ambos pagan S/ 45.00, ya que primero se suman los recargos y despues se aplica la beca.

## Conclusion

Con este ejercicio pude entender mejor como funciona la herencia multiple y el MRO en Python. Tambien aprendi que el orden de las operaciones puede cambiar el resultado y que usando composicion podemos controlar mejor los calculos sin depender tanto de las clases.
