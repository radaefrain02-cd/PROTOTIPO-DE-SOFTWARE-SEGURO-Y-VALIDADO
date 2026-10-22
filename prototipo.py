# ======================================================
# PROTOTIPO DE REGISTRO DE SOLICITUDES DE SOPORTE
# PFU-111 - Programación Fundamental
# ======================================================

# Variable global para almacenar la solicitud registrada
solicitud = None

# Opciones válidas
TIPOS_SOLICITUD = ["equipo", "software", "conectividad"]
PRIORIDADES = ["bajo", "medio", "alto"]


def validar_nombre(nombre):
    if nombre.strip() == "":
        raise ValueError("El nombre no puede estar vacío.")
    return True


def validar_codigo(codigo):
    # Formato definido: 8 dígitos numéricos
    if not codigo.isdigit() or len(codigo) != 8:
        raise ValueError(
            "El código de estudiante debe contener exactamente 8 dígitos numericos."
        )
    return True


def validar_tipo(tipo):
    if tipo.lower() not in TIPOS_SOLICITUD:
        raise ValueError(
            f"Tipo de solicitud no válido. Opciones: {', '.join(TIPOS_SOLICITUD)}"
        )
    return True


def validar_descripcion(descripcion):
    if descripcion.strip() == "":
        raise ValueError("La descripción no puede estar vacía.")
    return True


def validar_prioridad(prioridad):
    if prioridad.lower() not in PRIORIDADES:
        raise ValueError(
            f"Prioridad no válida. Opciones: {', '.join(PRIORIDADES)}"
        )
    return True


def registrar_solicitud():
    global solicitud

    try:
        print("\n=== REGISTRO DE SOLICITUD ===")

        nombre = input("Nombre del solicitante: ")
        validar_nombre(nombre)

        codigo = input("Código de estudiante (8 dígitos): ")
        validar_codigo(codigo)

        tipo = input(
            "Tipo de solicitud (equipo/software/conectividad): "
        ).lower()
        validar_tipo(tipo)

        descripcion = input("Descripción del problema: ")
        validar_descripcion(descripcion)

        prioridad = input(
            "Prioridad (bajo/medio/alto): "
        ).lower()
        validar_prioridad(prioridad)

        solicitud = {
            "nombre": nombre,
            "codigo": codigo,
            "tipo": tipo,
            "descripcion": descripcion,
            "prioridad": prioridad
        }

        print("\n Solicitud registrada correctamente.")

    except ValueError as error:
        print(f"\n Error de validación: {error}")

    except Exception as error:
        print(f"\n Error inesperado: {error}")


def consultar_solicitud():
    global solicitud

    print("\n=== CONSULTAR SOLICITUD ===")

    if solicitud is None:
        print("No existen solicitudes registradas.")
    else:
        print(f"Nombre      : {solicitud['nombre']}")
        print(f"Código      : {solicitud['codigo']}")
        print(f"Tipo        : {solicitud['tipo']}")
        print(f"Descripción : {solicitud['descripcion']}")
        print(f"Prioridad   : {solicitud['prioridad']}")


def limpiar_datos():
    global solicitud

    solicitud = None
    print("\n Datos eliminados. Puede ingresar una nueva solicitud.")


def mostrar_menu():
    print("\n" + "=" * 45)
    print(" SISTEMA DE SOPORTE TÉCNICO")
    print("=" * 45)
    print("1. Registrar solicitud")
    print("2. Consultar solicitud")
    print("3. Limpiar datos")
    print("4. Salir")
    print("=" * 45)


def main():
    while True:
        try:
            mostrar_menu()

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                registrar_solicitud()

            elif opcion == "2":
                consultar_solicitud()

            elif opcion == "3":
                limpiar_datos()

            elif opcion == "4":
                print("\nPrograma finalizado correctamente.")
                break

            else:
                raise ValueError(
                    "Opción inexistente. Seleccione una opción del 1 al 4."
                )

        except ValueError as error:
            print(f"\n {error}")

        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break

        except Exception as error:
            print(f"\n Error inesperado: {error}")


if __name__ == "__main__":
    main()