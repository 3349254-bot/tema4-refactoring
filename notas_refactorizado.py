"""
PROGRAMA DE GESTIÓN DE NOTAS ESCOLARES
Autor: [Tu Nombre]
Fecha: [Fecha actual]

Este programa calcula la media de tres notas de un alumno
y muestra su calificación cualitativa correspondiente.
"""

# Constantes (números con significado)
NOTA_APROBADO = 5
NOTA_NOTABLE = 7
NOTA_SOBRESALIENTE = 9


def calcular_media(nota1: float, nota2: float, nota3: float) -> float:
    """
    Calcula la media aritmética de tres notas.
    
    Args:
        nota1: Primera nota (0-10)
        nota2: Segunda nota (0-10)
        nota3: Tercera nota (0-10)
    
    Returns:
        float: La media de las tres notas
    """
    return (nota1 + nota2 + nota3) / 3


def obtener_calificacion(media: float) -> str:
    """
    Determina la calificación cualitativa según la nota media.
    
    Args:
        media: Nota media del alumno
    
    Returns:
        str: Calificación (Sobresaliente/Notable/Aprobado/Suspenso)
    """
    if media >= NOTA_SOBRESALIENTE:
        return "Sobresaliente"
    elif media >= NOTA_NOTABLE:
        return "Notable"
    elif media >= NOTA_APROBADO:
        return "Aprobado"
    else:
        return "Suspenso"


def mostrar_informe_alumno(nombre: str, nota1: float, nota2: float, nota3: float) -> None:
    """
    Muestra por pantalla el informe completo de un alumno.
    
    Args:
        nombre: Nombre del alumno
        nota1: Primera nota
        nota2: Segunda nota
        nota3: Tercera nota
    """
    # Cálculos (usando las funciones especializadas)
    media = calcular_media(nota1, nota2, nota3)
    calificacion = obtener_calificacion(media)
    
    # Presentación (solo imprimir, no calcular)
    print(f"Alumno: {nombre}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Media: {media:.2f}")  # :.2f formatea a 2 decimales
    print(f"Calificación: {calificacion}")
    print("-" * 30)


def main():
    """Función principal del programa."""
    print("=== INFORMES DE ALUMNOS ===\n")
    
    mostrar_informe_alumno("Ana García", 8, 7, 9)
    mostrar_informe_alumno("Luis Pérez", 4, 5, 3)
    mostrar_informe_alumno("Marta Gómez", 6, 7, 5)


if __name__ == "__main__":
    main()