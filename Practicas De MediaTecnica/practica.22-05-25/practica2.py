def obtener_nota(materia):
    """
    Función auxiliar para obtener una nota de una materia, con validación
    de entrada numérica y rango (entre 0 y 5).
    """
    while True:
        try:
            nota = float(input(f"Ingrese la nota de {materia}: "))
            if 0 <= nota <= 5: # Asumiendo que las notas son de 0 a 5
                return nota
            else:
                print("La nota debe estar entre 0 y 5. Por favor, intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número para la nota.")

def procesar_estudiante(grado_actual, periodo_actual, año_actual):
    """
    Procesa todos los datos y notas de un solo estudiante para el grado, período y año dados,
    determina si pasa el período y muestra un resumen.
    Retorna un diccionario con la información clave del estudiante.
    """
    print("\n" + "="*40)
    print(f"      DATOS DEL ESTUDIANTE ({grado_actual})")
    print("="*40)

    # Solicitar datos personales del estudiante
    numero_documento = input("Ingrese por favor el número de documento de identidad: ")
    tipo_documento = input("Ingrese el tipo de documento (Ej: CC, TI, Pasaporte, Otro): ").upper()
    nombre = input("Ingrese el nombre del estudiante: ").capitalize()
    apellido = input("Ingrese el apellido del estudiante: ").capitalize()

    print("\n" + "="*40)
    print("       INGRESO DE NOTAS POR MATERIA")
    print("="*40)

    notas_estudiante = {}
    materias = ["Inglés", "Matemáticas", "Ciencias", "Sociales"]

    # Preguntar por la nota de cada materia usando la función auxiliar
    for materia in materias:
        notas_estudiante[materia.lower()] = obtener_nota(materia)

    print("\n" + "="*40)
    print("           INFORMACIÓN FINAL")
    print("="*40)
    print("\n--Datos del Estudiante--")
    print(f"Nombre completo: {nombre} {apellido}")
    print(f"Tipo de documento: {tipo_documento}")
    print(f"Número de documento: {numero_documento}")
    print("\n--Grado y Período--")
    print(f"Grado: {grado_actual}")
    print(f"Período: {periodo_actual}")
    print(f"Año lectivo: {año_actual}")
    print("\n--Notas del Estudiante--")

    # Calcular la suma y el promedio de las notas válidas
    suma_notas_validas = 0
    conteo_notas_validas = 0
    for materia, nota in notas_estudiante.items():
        if nota is not None:
            print(f"Nota de {materia.capitalize()}: {nota}")
            suma_notas_validas += nota
            conteo_notas_validas += 1
        else:
            print(f"Nota de {materia.capitalize()}: No registrada (entrada inválida)")

    promedio_final = 0
    pasa_periodo = False # Variable para almacenar si el estudiante pasa o no

    print("\n--Resultado del Período--")
    if conteo_notas_validas == len(materias) and conteo_notas_validas > 0: # Asegurarse de que todas las notas fueron ingresadas correctamente y hay notas
        promedio_final = suma_notas_validas / conteo_notas_validas # Se divide entre la cantidad de notas
        print(f"Suma de todas las notas: {suma_notas_validas:.2f}") # Formatear a 2 decimales
        print(f"Promedio final: {promedio_final:.2f}") # Formatear a 2 decimales

        # Lógica de aprobación: promedio mayor a 2.9
        if promedio_final > 2.9:
            print(f"Sí, el estudiante {nombre} {apellido} PASA el período")
            pasa_periodo = True
        else:
            print(f"No, el estudiante {nombre} {apellido} NO PASA el período. Necesitaba más de 2.9.")
    else:
        print("No se pudo calcular el promedio ni determinar si el estudiante pasa debido a notas inválidas o faltantes.")


    # Retornar la información del estudiante para el resumen final
    return {
        "nombre": nombre,
        "apellido": apellido,
        "grado": grado_actual,
        "numero_documento": numero_documento,
        "pasa_periodo": pasa_periodo,
        "promedio_final": f"{promedio_final:.2f}" if conteo_notas_validas == len(materias) else "N/A" # Guardar el promedio formateado
    }


# --- Lógica principal del programa ---
print("***************")
print("  BIENVENIDO AL SISTEMA DE GESTIÓN DE NOTAS")
print("***************")

# Lista para almacenar la información de todos los estudiantes procesados
todos_los_estudiantes = []

procesar_otro_grado = "si"

print("\n" + "="*40)
print("        DATOS DEL COLEGIO")
print("="*40)
nombre_colegio = input("Digite el nombre de la institucion: ")
nit_colegio = input("Digite el nit del colegio: ")
periodo_actual = input("Ingrese el período actual para este grado (Ej: Primer Periodo, Segundo periodo): ")

# Bucle exterior para procesar GRADOS
while procesar_otro_grado.lower() == "si":
    print("\n" + "#"*50)
    print("         INICIO DE UN NUEVO GRADO")
    print("#"*50)

    # --- Validación del Grado ---
    while True:
        grado_input = input("Ingrese el grado que desea procesar (Ej: 6A, 7B, 11C, 8D, 9E, 10F): ").upper().strip()

        if len(grado_input) >= 2:
            try:
                # Intenta separar el número y la letra del grado
                # Esta lógica intenta ser más robusta para grados de 1 o 2 dígitos
                grado_num_str = ""
                grado_letra_parte = ""
                for char in grado_input:
                    if char.isdigit():
                        grado_num_str += char
                    else:
                        grado_letra_parte = char
                        break # Asume que la letra está al final del número

                if not grado_num_str or not grado_letra_parte: # Si no se pudo extraer número o letra
                     raise ValueError("Formato incompleto.")

                grado_num_parte = int(grado_num_str)


                # Validar el número y la letra
                if 6 <= grado_num_parte <= 11 and grado_letra_parte in ['A', 'B', 'C','D','E','F']:
                    grado_actual = f"{grado_num_parte}{grado_letra_parte}" # Reconstruir para asegurar formato consistente
                    print(f"Grado '{grado_actual}' aceptado.")
                    break # Salir del bucle de validación de grado
                else:
                    print("Formato de grado inválido. Asegúrese que el número esté entre 6 y 11 y la letra sea A, B, C, D, F.")
            except (ValueError, IndexError):
                print("Formato de grado inválido. Use el formato 'NúmeroLetra' (Ej: 6A, 10B).")
        else:
            print("Formato de grado inválido. Demasiado corto. Use el formato 'NúmeroLetra' (Ej: 6A, 10B).")
    # --- FIN DE LA VALIDACIÓN DEL GRADO ---

    año_actual = input("Ingrese el año lectivo actual (Ej: 2025): ")

    hay_mas_estudiantes_en_grado = "si"

    # Bucle interior para procesar ESTUDIANTES dentro del GRADO actual
    while hay_mas_estudiantes_en_grado.lower() == "si":
        # Llama a la función y guarda el diccionario que retorna
        estudiante_info = procesar_estudiante(grado_actual, periodo_actual, año_actual)
        todos_los_estudiantes.append(estudiante_info) # Añade la info del estudiante a la lista

        # Preguntar si hay más estudiantes en el GRADO ACTUAL
        print("\n" + "-"*40)
        hay_mas_estudiantes_en_grado = input(
            f"¿Hay más estudiantes en el grado {grado_actual} para procesar? (si/no): "
        )
        print("-" * 40)

    # Si el usuario dice que no hay más estudiantes en el grado actual,
    # preguntamos si quiere procesar otro grado
    print("\n" + "="*50)
    procesar_otro_grado = input("¿Desea procesar estudiantes de OTRO GRADO? (si/no): ")
    print("=" * 50)

# Datos del colegio
print("\n" + "="*40)
print("        DATOS DEL COLEGIO")
print("="*40)
print(" ")
print("Nombre de la institucion: ", nombre_colegio)
print("Nit del colegio: ", nit_colegio)
print("Periodo del colegio: ", periodo_actual)

# --- Resumen final de todos los estudiantes ---
print("\n" + "="*60)
print("             RESUMEN GENERAL DE ESTUDIANTES")
print("="*60)

if not todos_los_estudiantes:
    print("No se procesó ningún estudiante.")
else:
    for i, estudiante in enumerate(todos_los_estudiantes):
        estado = "Pasa" if estudiante['pasa_periodo'] else "No Pasa"
        print(f"\n--- Estudiante #{i+1} ---")
        print(f"Nombre: {estudiante['nombre']} {estudiante['apellido']}")
        print(f"Grado: {estudiante['grado']}")
        print(f"Documento: {estudiante['numero_documento']}")
        print(f"Promedio Final: {estudiante['promedio_final']}")
        print(f"Resultado: {estado}")

print("\n" + "*"*60)
print("¡Proceso de gestión de notas finalizado!")
print("*"*60)