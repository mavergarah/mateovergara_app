def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def safety_validation(V, S):
    """ Esta función se encarga de validar los datos ingresados por el usuario para
    el cálculo de arco eléctrico. En caso de que alguno no sea valido se pondrá un
    error en el HTML en el <input> respectivo.

    """
    validation = 'No error'

    # Se valida que la tensión sea un número entero o de coma flotante
    if not is_number(V):
        validation = 'Error'
        print(validation)

    # Se valida que el usuario haya seleccionado una opción para el tipo de sistema
    if S == 'Sistema':
        validation = 'Error'
        print(validation)

    return validation

def work_validation(V, H, W, VS, BS, CO):
    """ Esta función se encarga de validar los datos ingresados por el usuario para
    el cálculo de arco eléctrico. En caso de que alguno no sea valido se pondrá un
    error en el HTML en el <input> respectivo.

    """
    validation = 'No error'

    # Se valida que la tensión sea un número entero o de coma flotante
    if not is_number(V):
        validation = 'Error'
        print(validation)

    # Se valida que la altura del tablero sea un número entero o de coma flotante
    if not is_number(H):
        validation = 'Error'
        print(validation)

    # Se valida que el ancho del tablero sea un número entero o de coma flotante
    if not is_number(W):
        validation = 'Error'
        print(validation)

    # Se valida que el usuario haya seleccionado una opción para el tipo de sistema
    if VS == 'Sistema':
        validation = 'Error'
        print(validation)

    # Se valida que el usuario haya seleccionado una opción para el acceso posterior
    if BS == 'Acceso posterior?':
        validation = 'Error'
        print(validation)

    # Se valida que el usuario haya seleccionado una opción para el tipo de sistema
    if CO == 'Condicion?':
        validation = 'Error'
        print(validation)

    return validation

def work_clearances(voltage = 220, panel_height = 0.6, panel_width = 0.76, system = 3, condition = 1, back_equipments = 'n'):
    """ Calcular la distancia de seguridad que debe haber alrededor de los equipos eléctricos basado
    en el artículo 110.26(A)(1), Espacios de Trabajo, de la NTC 2050 del 2020. El usuario deberá ingresar
    los datos de tensión, condición, sistema monofásico o trifásico, altura del panel, ancho del panel,
    y si hay equipos que se puedan acceder desenergizados por la parte posterior. """

    # PROFUNDIDAD DEL ESPACIO DE TRABAJO
    # 1. Preguntar si el sistema es monofásico, bifásico o trifásico
    if system == 1:
        voltage_to_ground = voltage
    else:
        voltage_to_ground = voltage / (3**0.5)

    if voltage_to_ground <= 150:
        depth_clearance = 0.9
    elif 150.1 <= voltage_to_ground <= 600:
        # 3. Preguntar por la profundidad del espacio de trabajo
        if condition == 1:
            depth_clearance = 0.9
        elif condition == 2:
            depth_clearance = 1
        else:
            depth_clearance = 1.2
    elif 600.1 <= voltage_to_ground <= 2500:
        if condition == 1:
            depth_clearance = 0.9
        elif condition == 2:
            depth_clearance = 1.2
        else:
            depth_clearance = 1.5
    elif 2500.1 <= voltage_to_ground <= 9000:
        if condition == 1:
            depth_clearance = 1.2
        elif condition == 2:
            depth_clearance = 1.5
        else:
            depth_clearance = 1.8
    elif 9000.1 <= voltage_to_ground <= 25000:
        if condition == 1:
            depth_clearance = 1.5
        elif condition == 2:
            depth_clearance = 1.8
        else:
            depth_clearance = 2.8
    elif 25000.1 <= voltage_to_ground <= 75000:
        if condition == 1:
            depth_clearance = 1.8
        elif condition == 2:
            depth_clearance = 2.5
        else:
            depth_clearance = 3.0
    else:
        if condition == 1:
            depth_clearance = 2.5
        elif condition == 2:
            depth_clearance = 3.0
        else:
            depth_clearance = 3.7

    # ALTURA DEL ESPACIO DE TRABAJO
    # 4. Preguntar por la altura del espacio del tablero para poder asignar la altura del espacio de TRABAJO
    if panel_height > 2.0:
        height_clearance = panel_height
    else:
        height_clearance = 2.0

    # ANCHO DEL ESPACIO DE TRABAJO
    if panel_width > 0.76:
        width_clearance = panel_width
    else:
        width_clearance = 0.76

    # ESPACIO DE TRABAJO POSTERIOR
    if back_equipments == 'Si':
        back_clearance = 0.76
    else:
        back_clearance = '-'

    print(back_equipments)
    # SE ENTREGA EL RESULTADO
    return depth_clearance, height_clearance, width_clearance, back_clearance

def safety_clearances(voltage = 220, system = 'AC'):
    """ Calcular la distancia de seguridad que debe haber alrededor de los equipos eléctricos basado
    en el artículo 110.26(A)(1), Espacios de Trabajo, de la NTC 2050 del 2020. El usuario deberá ingresar
    los datos de tensión, condición, sistema monofásico o trifásico, altura del panel, ancho del panel,
    y si hay equipos que se puedan acceder desenergizados por la parte posterior. """

    # PROFUNDIDAD DEL ESPACIO DE TRABAJO
    # 1. Preguntar si el sistema es AC o DC
    if system == 'AC':
        if 50 <= voltage <= 300:
            safety_clearance_movil = 3.0
            safety_clearance_static = 1.0
            resctricted_clearance = 0.3
        elif 301 <= voltage <= 750:
            safety_clearance_movil = 3.0
            safety_clearance_static = 1.0
            resctricted_clearance = 0.3
        elif 751 <= voltage <= 15000:
            safety_clearance_movil = 3.0
            safety_clearance_static = 1.5
            resctricted_clearance = 0.7
        elif 15001 <= voltage <= 36000:
            safety_clearance_movil = 3.0
            safety_clearance_static = 1.8
            resctricted_clearance = 0.8
        elif 36001 <= voltage <= 46000:
            safety_clearance_movil = 3.0
            safety_clearance_static = 2.5
            resctricted_clearance = 0.8
        elif 46001 <= voltage <= 72500:
            safety_clearance_movil = 3.0
            safety_clearance_static = 2.5
            resctricted_clearance = 1.0
        elif 72600 <= voltage <= 121000:
            safety_clearance_movil = 3.3
            safety_clearance_static = 2.5
            resctricted_clearance = 1.0
        elif 138000 <= voltage <= 145000:
            safety_clearance_movil = 3.4
            safety_clearance_static = 3.0
            resctricted_clearance = 1.2
        elif 161000 <= voltage <= 169000:
            safety_clearance_movil = 3.6
            safety_clearance_static = 3.6
            resctricted_clearance = 1.3
        elif 230000 <= voltage <= 242000:
            safety_clearance_movil = 4.0
            safety_clearance_static = 4.0
            resctricted_clearance = 1.7
        elif 345000 <= voltage <= 362000:
            safety_clearance_movil = 3.0
            safety_clearance_static = 1.0
            resctricted_clearance = 0.3
        elif 500000 <= voltage <= 550000:
            safety_clearance_movil = 3.0
            safety_clearance_static = 1.0
            resctricted_clearance = 0.3
        else:
            safety_clearance_movil = 'No value'
            safety_clearance_static = 'No value'
            resctricted_clearance = 'No value'

    if system == 'DC':
        if 100 <= voltage <= 300:
            safety_clearance_movil = 3.0
            safety_clearance_static = 1.0
            resctricted_clearance = 0.3
        elif 301 <= voltage <= 1000:
            safety_clearance_movil = 3.0
            safety_clearance_static = 1.0
            resctricted_clearance = 0.3
        elif 1100 <= voltage <= 5000:
            safety_clearance_movil = 3.0
            safety_clearance_static = 1.5
            resctricted_clearance = 0.5
        elif 5100 <= voltage <= 15000:
            safety_clearance_movil = 3.0
            safety_clearance_static = 1.5
            resctricted_clearance = 0.7
        elif 15100 <= voltage <= 45000:
            safety_clearance_movil = 3.0
            safety_clearance_static = 2.5
            resctricted_clearance = 0.8
        elif 45100 <= voltage <= 75000:
            safety_clearance_movil = 3.0
            safety_clearance_static = 2.5
            resctricted_clearance = 1.0
        elif 75100 <= voltage <= 150000:
            safety_clearance_movil = 3.3
            safety_clearance_static = 3.0
            resctricted_clearance = 1.2
        elif 150100 <= voltage <= 250000:
            safety_clearance_movil = 3.6
            safety_clearance_static = 3.6
            resctricted_clearance = 1.6
        elif 250100 <= voltage <= 500000:
            safety_clearance_movil = 6.0
            safety_clearance_static = 6.0
            resctricted_clearance = 3.5
        elif 500100 <= voltage <= 800000:
            safety_clearance_movil = 8.0
            safety_clearance_static = 8.0
            resctricted_clearance = 5.0
        else:
            safety_clearance_movil = 'No value'
            safety_clearance_static = 'No value'
            resctricted_clearance = 'No value'

    return safety_clearance_movil, safety_clearance_static, resctricted_clearance
