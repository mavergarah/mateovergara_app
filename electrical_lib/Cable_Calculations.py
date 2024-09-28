def isin_range(value, min, max):
    """ Esta función verifica que un valor ingresado sea un número entero positivo
    """

    try:
        if min <= float(value) <= max:
            return True
    except ValueError:
        return False

def is_choice(value, option):
    """ Esta función verifica se haya seleccionado una opción de un formulario
    """

    if value == option:
        return False
    else:
        return True

def is_number(value):
    """ Esta función verifica que un valor ingresado sea un número entero positivo
    """

    try:
        float(value)
        return True
    except ValueError:
        return False

def cable_validation(P, U, Phases, FP, V, L, T_amb, T_cond, CL, K, NC, KC):
    """ Esta función se encarga de realizar la validación de los datos que ingresa el usuario
    """
    validation = 'No error'

    if not is_number(P):
        validation = 'Error'

    if U == 'unidades':
        validation = 'Error'

    if Phases == 'fases':
        validation = 'Error'

    if not is_number(FP):
        validation = 'Error'
    elif (1 < float(FP) < 0):
        validation = 'Error'

    if not is_number(V):
        validation = 'Error'

    if not is_number(L):
        validation = 'Error'

    if not is_number(T_amb):
        validation = 'Error'

    if T_cond == 'temperatura':
        validation = 'Error'

    if CL == 'carga continua':
        validation = 'Error'

    if K == 'material':
        validation = 'Error'

    if not is_number(NC):
        validation = 'Error'

    if KC == 'conduit':
        validation = 'Error'

    return validation

def electrode_conductor(gauge_input,K):
    """ Esta función selecciona el conductor del electrodo de puesta a tierra basado en
    la tabla 250.66 de la NTC 2050 del 2021. La función busca la posición en la que se
    encuentra el calibre ingresado por el usuario en el arreglo all_gauges. Sabiendo esa
    posición se puede determinar en que rango está el calibre y seleccionar el conductor
    del electrodo de puesta a tierra. Los rango son:
    Cu: 2 AWG o menor --> Hasta la posición 8
    Al: 1/0 AWG o menor --> Hasta la posición 10
    Cu: 1 AWG - 1/0 AWG --> 9 - 10
    Al: 2/0 AWG - 3/0 AWG --> 11 - 12
    Cu: 2/0 AWG - 3/0 AWG --> 11 - 12
    Al: 4/0 AWG - 250 MCM --> 13 - 14
    Cu: 4/0 AWG - 350 MCM --> 14 - 16
    Al: 300 MCM - 500 MCM --> 15 - 18
    Cu: 400 MCM - 600 MCM --> 17 - 19
    Al: 500 MCM - 900 MCM --> 18 - 20
    Cu: 750 MCM - 1000 MCM --> 20 en adelante
    Al: 1000 MCM --> 21

    """
    all_gauges = ['14 AWG','12 AWG','10 AWG','8 AWG','6 AWG','4 AWG','3 AWG','2 AWG','1 AWG','1/0 AWG','2/0 AWG','3/0 AWG', '4/0 AWG','250 MCM','300 MCM','350 MCM','400 MCM','500 MCM','600 MCM','750 MCM','1000 MCM']
    i = 1

    while not gauge_input == all_gauges[i-1]:
        i = i + 1

    if K == 'Cu':
        if i <= 8:
            ground_cu = '8 AWG'
            ground_al = '6 AWG'
        elif i <= 10:
            ground_cu = '6 AWG'
            ground_al = '4 AWG'
        elif i <= 12:
            ground_cu = '4 AWG'
            ground_al = '2 AWG'
        elif i <= 16:
            ground_cu = '2 AWG'
            ground_al = '1/0 AWG'
        elif i <= 19:
            ground_cu = '1/0 AWG'
            ground_al = '3/0 AWG'
        elif i >= 20:
            ground_cu = '2/0 AWG'
            ground_al = '4/0 AWG'
        else:
            ground_cu = 'No gauge'
            ground_al = 'No gauge'
    else:
        if i <= 10:
            ground_cu = '8 AWG'
            ground_al = '6 AWG'
        elif i <= 12:
            ground_cu = '6 AWG'
            ground_al = '4 AWG'
        elif i <= 14:
            ground_cu = '4 AWG'
            ground_al = '2 AWG'
        elif i <= 18:
            ground_cu = '2 AWG'
            ground_al = '1/0 AWG'
        elif i <= 20:
            ground_cu = '1/0 AWG'
            ground_al = '3/0 AWG'
        elif i >= 21:
            ground_cu = '2/0 AWG'
            ground_al = '4/0 AWG'
        else:
            ground_cu = 'No gauge'
            ground_al = 'No gauge'

    return ground_cu, ground_al


def earth_conductor(protective_device, kind_of_cable):
    """ Esta función selecciona el conductor de puesta a tierra del equipo basado en el tipo de material del
    conductor y el dispositivo de protección. Esta selección se hace basado en la tabla
    """

    # 1. Evaluar el valor del dispositivo de protección
    if protective_device == '-':
        earth_gauge = '-'
    elif protective_device <= 15:
        if kind_of_cable == 'Cu':
            earth_gauge = '14 AWG'
        else:
            earth_gauge = '12 AWG'
    elif protective_device <= 20:
        if kind_of_cable == 'Cu':
            earth_gauge = '12 AWG'
        else:
            earth_gauge = '10 AWG'
    elif protective_device <= 60:
        if kind_of_cable == 'Cu':
            earth_gauge = '10 AWG'
        else:
            earth_gauge = '8 AWG'
    elif protective_device <= 100:
        if kind_of_cable == 'Cu':
            earth_gauge = '8 AWG'
        else:
            earth_gauge = '6 AWG'
    elif protective_device <= 200:
        if kind_of_cable == 'Cu':
            earth_gauge = '6 AWG'
        else:
            earth_gauge = '4 AWG'
    elif protective_device <= 300:
        if kind_of_cable == 'Cu':
            earth_gauge = '4 AWG'
        else:
            earth_gauge = '2 AWG'
    elif protective_device <= 400:
        if kind_of_cable == 'Cu':
            earth_gauge = '3 AWG'
        else:
            earth_gauge = '1 AWG'
    elif protective_device <= 500:
        if kind_of_cable == 'Cu':
            earth_gauge = '2 AWG'
        else:
            earth_gauge = '1/0 AWG'
    elif protective_device <= 600:
        if kind_of_cable == 'Cu':
            earth_gauge = '1 AWG'
        else:
            earth_gauge = '2/0 AWG'
    elif protective_device <= 800:
        if kind_of_cable == 'Cu':
            earth_gauge = '1/0 AWG'
        else:
            earth_gauge = '3/0 AWG'
    elif protective_device <= 1000:
        if kind_of_cable == 'Cu':
            earth_gauge = '2/0 AWG'
        else:
            earth_gauge = '4/0 AWG'
    elif protective_device <= 1200:
        if kind_of_cable == 'Cu':
            earth_gauge = '3/0 AWG'
        else:
            earth_gauge = '250 MCM'
    elif protective_device <= 1600:
        if kind_of_cable == 'Cu':
            earth_gauge = '4/0 AWG'
        else:
            earth_gauge = '350 MCM'
    elif protective_device <= 2000:
        if kind_of_cable == 'Cu':
            earth_gauge = '250 MCM'
        else:
            earth_gauge = '400 MCM'
    elif protective_device <= 2500:
        if kind_of_cable == 'Cu':
            earth_gauge = '350 MCM'
        else:
            earth_gauge = '600 MCM'
    elif protective_device <= 3000:
        if kind_of_cable == 'Cu':
            earth_gauge = '400 MCM'
        else:
            earth_gauge = '600 MCM'
    elif protective_device <= 4000:
        if kind_of_cable == 'Cu':
            earth_gauge = '500 MCM'
        else:
            earth_gauge = '750 MCM'
    elif protective_device <= 5000:
        if kind_of_cable == 'Cu':
            earth_gauge = '700 MCM'
        else:
            earth_gauge = '1200 MCM'
    elif protective_device <= 6000:
        if kind_of_cable == 'Cu':
            earth_gauge = '800 MCM'
        else:
            earth_gauge = '1200 MCM'

    return earth_gauge

def protective_device(I_adjust, I_continuous):
    """ Selecciona el valor nominal estándar en A para fusibles e interruptores automáticos de la tabla
    240.6(A) basado en la corriente de carga continua y en la corriente corregida por temperatura y ajustada
    por cantidad de conductores en una misma canalización. """

    if I_continuous <= 10 <= I_adjust:
        return 10
    elif I_continuous <= 15 <= I_adjust:
        return 15
    elif I_continuous <= 20 <= I_adjust:
        return 20
    elif I_continuous <= 25 <= I_adjust:
        return 25
    elif I_continuous <= 30 <= I_adjust:
        return 30
    elif I_continuous <= 35 <= I_adjust:
        return 35
    elif I_continuous <= 40 <= I_adjust:
        return 40
    elif I_continuous <= 45 <= I_adjust:
        return 45
    elif I_continuous <= 50 <= I_adjust:
        return 50
    elif I_continuous <= 60 <= I_adjust:
        return 60
    elif I_continuous <= 70 <= I_adjust:
        return 70
    elif I_continuous <= 80 <= I_adjust:
        return 80
    elif I_continuous <= 90 <= I_adjust:
        return 90
    elif I_continuous <= 100 <= I_adjust:
        return 100
    elif I_continuous <= 110 <= I_adjust:
        return 110
    elif I_continuous <= 125 <= I_adjust:
        return 125
    elif I_continuous <= 150 <= I_adjust:
        return 150
    elif I_continuous <= 175 <= I_adjust:
        return 175
    elif I_continuous <= 200 <= I_adjust:
        return 200
    elif I_continuous <= 225 <= I_adjust:
        return 225
    elif I_continuous <= 250 <= I_adjust:
        return 250
    elif I_continuous <= 300 <= I_adjust:
        return 300
    elif I_continuous <= 350 <= I_adjust:
        return 350
    elif I_continuous <= 400 <= I_adjust:
        return 400
    elif I_continuous <= 450 <= I_adjust:
        return 450
    elif I_continuous <= 500 <= I_adjust:
        return 500
    elif I_continuous <= 600 <= I_adjust:
        return 600
    elif I_continuous <= 700 <= I_adjust:
        return 700
    elif I_continuous <= 800 <= I_adjust:
        return 800
    elif I_continuous <= 1000 <= I_adjust:
        return 1000
    elif I_continuous <= 1200 <= I_adjust:
        return 1200
    elif I_continuous <= 1600 <= I_adjust:
        return 1600
    elif I_continuous <= 2000 <= I_adjust:
        return 2000
    elif I_continuous <= 2500 <= I_adjust:
        return 2500
    elif I_continuous <= 3000 <= I_adjust:
        return 3000
    elif I_continuous <= 4000 <= I_adjust:
        return 4000
    elif I_continuous <= 5000 <= I_adjust:
        return 5000
    elif I_continuous <= 5000 <= I_adjust:
        return 5000
    else:
        return '-'

def find_next_gauge(gauge):
    """ Compara el calibre actual y devuelve el siguiente calibre más grande para poder volver a calcular la regulación
    de tensión con el calibre más grande y garantizar así que esta sea menor que 3%. """
    # 1. Iniciar un arreglo con los calibres de los conductores y un índice para recorrer el arreglo
    j = 0
    all_gauges = ['14 AWG','12 AWG','10 AWG','8 AWG','6 AWG','4 AWG','3 AWG','2 AWG','1 AWG','1/0 AWG','2/0 AWG','3/0 AWG', '4/0 AWG','250 MCM','300 MCM','350 MCM','400 MCM','500 MCM','600 MCM','750 MCM','1000 MCM']

    # 2. Buscar el calibre enviado
    while gauge != all_gauges[j]:
        j = j + 1

    # 3. Retornar el valor del calibre
    return all_gauges[j+1]

def drop_voltage_calculation(Ph, V, L, I, PF, gauge, KC, K):
    """ Calcula la caída de tensión porcentual de un circuito eléctrico dependiendo de si este es monofásico o
    trifásico, el nivel de tensión la longitud, la corriente, la resistencia, la reactancia del conductor eléctrico
    y el factor de potencia. Retorna el valor en porcentaje (No en entero)."""

    # 1. Importar el método math para poder sacar el seno y el coseno
    import math

    # 2. Seleccionar los valores de resistencia y reactancia de la tabla 9 de la NTC 2050 del 2020
    R, XL = resistance_and_reactance(gauge, KC, K)
    print ('La resistencia es %.4f y la reactancia es %.4f' %(R, XL))

    # 3. Preguntar si el sistema es monofásico o trifásico. Monofásico y bifásico se calculas igual.
    if Ph == 3:
        drop_voltage = (3**0.5) * I * (L / 1000) * (R * PF + XL * math.sin(math.acos(PF)))
    else:
        drop_voltage = 2 * I * (L / 1000) * (R * PF + XL * math.sin(math.acos(PF)))
    print('La caida de tensión es: %.4f V' % drop_voltage)
    return drop_voltage, (drop_voltage * 100 / V), R, XL

def resistance_and_reactance(gauge, KC, K):
    """ Selecciona la resisencia y la reactancia del calibre de un conductor determinado dependiendo del calibre
    del conductor y del tipo de material del conduit del circuito ramal"""
    # 1. Preguntar si el conductor es de Al o Cu para seleccionar la resistencia en c.a.
    if K == 'Cu':
        # 2. Preguntar si el material del conduito es Acero o PVC
        if KC == 'st':
            if gauge == '14 AWG':
                R = 10.2
            elif gauge == '12 AWG':
                R = 6.6
            elif gauge == '10 AWG':
                R = 3.9
            elif gauge == '8 AWG':
                R = 2.56
            elif gauge == '6 AWG':
                R = 1.61
            elif gauge == '4 AWG':
                R = 1.02
            elif gauge == '3 AWG':
                R = 0.82
            elif gauge == '2 AWG':
                R = 0.66
            elif gauge == '1 AWG':
                R = 0.52
            elif gauge == '1/0 AWG':
                R = 0.39
            elif gauge == '2/0 AWG':
                R = 0.33
            elif gauge == '3/0 AWG':
                R = 0.259
            elif gauge == '4/0 AWG':
                R = 0.207
            elif gauge == '250 MCM':
                R = 0.177
            elif gauge == '300 MCM':
                R = 0.148
            elif gauge == '350 MCM':
                R = 0.128
            elif gauge == '400 MCM':
                R = 0.115
            elif gauge == '500 MCM':
                R = 0.095
            elif gauge == '600 MCM':
                R = 0.082
            elif gauge == '750 MCM':
                R = 0.069
            elif gauge == '1000 MCM':
                R = 0.059
        else:
            if gauge == '14 AWG':
                R = 10.2
            elif gauge == '12 AWG':
                R = 6.6
            elif gauge == '10 AWG':
                R = 3.9
            elif gauge == '8 AWG':
                R = 2.56
            elif gauge == '6 AWG':
                R = 1.61
            elif gauge == '4 AWG':
                R = 1.02
            elif gauge == '3 AWG':
                R = 0.82
            elif gauge == '2 AWG':
                R = 0.62
            elif gauge == '1 AWG':
                R = 0.49
            elif gauge == '1/0 AWG':
                R = 0.39
            elif gauge == '2/0 AWG':
                R = 0.33
            elif gauge == '3/0 AWG':
                R = 0.253
            elif gauge == '4/0 AWG':
                R = 0.203
            elif gauge == '250 MCM':
                R = 0.171
            elif gauge == '300 MCM':
                R = 0.144
            elif gauge == '350 MCM':
                R = 0.125
            elif gauge == '400 MCM':
                R = 0.108
            elif gauge == '500 MCM':
                R = 0.089
            elif gauge == '600 MCM':
                R = 0.075
            elif gauge == '750 MCM':
                R = 0.062
            elif gauge == '1000 MCM':
                R = 0.049
    else:
        if KC == 'st':
            if gauge == '12 AWG':
                R = 10.5
            elif gauge == '10 AWG':
                R = 6.6
            elif gauge == '8 AWG':
                R = 4.3
            elif gauge == '6 AWG':
                R = 2.66
            elif gauge == '4 AWG':
                R = 1.67
            elif gauge == '3 AWG':
                R = 1.31
            elif gauge == '2 AWG':
                R = 1.05
            elif gauge == '1 AWG':
                R = 0.82
            elif gauge == '1/0 AWG':
                R = 0.66
            elif gauge == '2/0 AWG':
                R = 0.52
            elif gauge == '3/0 AWG':
                R = 0.43
            elif gauge == '4/0 AWG':
                R = 0.33
            elif gauge == '250 MCM':
                R = 0.282
            elif gauge == '300 MCM':
                R = 0.236
            elif gauge == '350 MCM':
                R = 0.207
            elif gauge == '400 MCM':
                R = 0.180
            elif gauge == '500 MCM':
                R = 0.148
            elif gauge == '600 MCM':
                R = 0.125
            elif gauge == '750 MCM':
                R = 0.102
            elif gauge == '1000 MCM':
                R = 0.082
        else:
            if gauge == '12 AWG':
                R = 10.5
            elif gauge == '10 AWG':
                R = 6.6
            elif gauge == '8 AWG':
                R = 4.3
            elif gauge == '6 AWG':
                R = 2.66
            elif gauge == '4 AWG':
                R = 1.67
            elif gauge == '3 AWG':
                R = 1.31
            elif gauge == '2 AWG':
                R = 1.05
            elif gauge == '1 AWG':
                R = 0.82
            elif gauge == '1/0 AWG':
                R = 0.66
            elif gauge == '2/0 AWG':
                R = 0.52
            elif gauge == '3/0 AWG':
                R = 0.43
            elif gauge == '4/0 AWG':
                R = 0.33
            elif gauge == '250 MCM':
                R = 0.279
            elif gauge == '300 MCM':
                R = 0.233
            elif gauge == '350 MCM':
                R = 0.200
            elif gauge == '400 MCM':
                R = 0.177
            elif gauge == '500 MCM':
                R = 0.141
            elif gauge == '600 MCM':
                R = 0.118
            elif gauge == '750 MCM':
                R = 0.095
            elif gauge == '1000 MCM':
                R = 0.075

    # 3. Preguntar si es conduit de acero o pvc para seleccionar la reactancia de c.a.
    if KC == 'st':
        if gauge == '14 AWG':
            X = 0.240
        elif gauge == '12 AWG':
            X = 0.223
        elif gauge == '10 AWG':
            X = 0.207
        elif gauge == '8 AWG':
            X = 0.213
        elif gauge == '6 AWG':
            X = 0.213
        elif gauge == '4 AWG':
            X = 0.197
        elif gauge == '3 AWG':
            X = 0.194
        elif gauge == '2 AWG':
            X = 0.187
        elif gauge == '1 AWG':
            X = 0.187
        elif gauge == '1/0 AWG':
            X = 0.180
        elif gauge == '2/0 AWG':
            X = 0.177
        elif gauge == '3/0 AWG':
            X = 0.171
        elif gauge == '4/0 AWG':
            X = 0.167
        elif gauge == '250 MCM':
            X = 0.171
        elif gauge == '300 MCM':
            X = 0.167
        elif gauge == '350 MCM':
            X = 0.164
        elif gauge == '400 MCM':
            X = 0.161
        elif gauge == '500 MCM':
            X = 0.157
        elif gauge == '600 MCM':
            X = 0.157
        elif gauge == '750 MCM':
            X = 0.157
        elif gauge == '1000 MCM':
            X = 0.151
    else:
        if gauge == '14 AWG':
            X = 0.190
        elif gauge == '12 AWG':
            X = 0.177
        elif gauge == '10 AWG':
            X = 0.164
        elif gauge == '8 AWG':
            X = 0.171
        elif gauge == '6 AWG':
            X = 0.167
        elif gauge == '4 AWG':
            X = 0.157
        elif gauge == '3 AWG':
            X = 0.154
        elif gauge == '2 AWG':
            X = 0.148
        elif gauge == '1 AWG':
            X = 0.151
        elif gauge == '1/0 AWG':
            X = 0.144
        elif gauge == '2/0 AWG':
            X = 0.141
        elif gauge == '3/0 AWG':
            X = 0.138
        elif gauge == '4/0 AWG':
            X = 0.135
        elif gauge == '250 MCM':
            X = 0.135
        elif gauge == '300 MCM':
            X = 0.135
        elif gauge == '350 MCM':
            X = 0.131
        elif gauge == '400 MCM':
            X = 0.131
        elif gauge == '500 MCM':
            X = 0.128
        elif gauge == '600 MCM':
            X = 0.128
        elif gauge == '750 MCM':
            X = 0.125
        elif gauge == '1000 MCM':
            X = 0.121

    return R, X

def adjustment_correction_factor(NC):
    """ Selecciona el factor de ajuste para más de tres conductores portadores de corriente en una misma canalización.
    Para eso se debe ingresar en número de conductores eléctricos que van por la misma canalización que el
    conductor al cual se le está calculando el calibre """
    if NC < 6:
        return 0.8
    elif NC < 9:
        return 0.7
    elif NC < 20:
        return 0.5
    elif NC < 30:
        return 0.45
    elif NC < 40:
        return 0.4
    else:
        return 0.35

def temperature_correction_factor(T_amb = '25', T = '60'):
    """ Selelcciona el factor de ajuste por temperatura para un conductor, basado en la temperatura ambiente
    y en la temperatura nominal del aislamiento del conductor. Este ajuste se realiza basado en la tabla
    310.15(B)(2) """

    # 1. Veriricar que temperatura tiene el aislamiento (variable T)
    if T == 60:
        # 2. Evaluar que temperatura ambiente tiene el conductor
        if T_amb < 10:
            return 1.29
        elif T_amb < 15:
            return 1.22
        elif T_amb < 20:
            return 1.15
        elif T_amb < 25:
            return 1.08
        elif T_amb < 30:
            return 1.00
        elif T_amb < 35:
            return 0.91
        elif T_amb < 40:
            return 0.82
        elif T_amb < 45:
            return 0.71
        elif T_amb < 50:
            return 0.58
        elif T_amb < 55:
            return 0.41
        else:
            return 'no temp. correc. factor'
    elif T == 75:
        if T_amb < 10:
            return 1.20
        elif T_amb < 15:
            return 1.15
        elif T_amb < 20:
            return 1.11
        elif T_amb < 25:
            return 1.05
        elif T_amb < 30:
            return 1.00
        elif T_amb < 35:
            return 0.94
        elif T_amb < 40:
            return 0.88
        elif T_amb < 45:
            return 0.82
        elif T_amb < 50:
            return 0.75
        elif T_amb < 55:
            return 0.67
        elif T_amb < 60:
            return 0.58
        elif T_amb < 65:
            return 0.47
        elif T_amb < 70:
            return 0.33
        else:
            return 'no temp. correc. factor'
    else:
        if T_amb < 10:
            return 1.15
        elif T_amb < 15:
            return 1.12
        elif T_amb < 20:
            return 1.08
        elif T_amb < 25:
            return 1.04
        elif T_amb < 30:
            return 1.00
        elif T_amb < 35:
            return 0.96
        elif T_amb < 40:
            return 0.91
        elif T_amb < 45:
            return 0.87
        elif T_amb < 50:
            return 0.82
        elif T_amb < 55:
            return 0.76
        elif T_amb < 60:
            return 0.71
        elif T_amb < 65:
            return 0.65
        elif T_amb < 70:
            return 0.58
        elif T_amb < 75:
            return 0.50
        elif T_amb < 80:
            return 0.41
        elif T_amb < 85:
            return 0.29
        else:
            return 'no temp. correc. factor'

def conductor_gauge(I, V, T, K):
    """ Esta función realiza la selección del calibre del conductor de fase de acuerdo a la corriente (I),
    la tensión (V), el tipo de conductor (K) y la temperatura (T). Para seleccionar dicho calibre es necesario recurrir a la
    tabla 310.15(B)(16) de la NTC 2050 del 2024 """

    # 1. Asignamos el calibre mínimo al conductor dependiendo del nivel de tensión. Esto lo hacemos por medio
    # busqueda en la tabla 310.15(B)(16). Es decir, dependiendo del nivel de tensión la búsqueda en la tabla
    # iniciará en el calibre mínimo.
    if V < 2000:
        cal, I_nom = search_table_31015(I, V, T, K, 1)
    elif V < 5000:
        cal, I_nom = search_table_31015(I, V, T, K, 2)
    elif V < 8000:
        cal, I_nom = search_table_31015(I, V, T, K, 3)
    elif V < 15000:
        cal, I_nom = search_table_31015(I, V, T, K, 4)
    elif V < 28000:
        cal, I_nom = search_table_31015(I, V, T, K, 5)
    elif V < 35000:
        cal, I_nom = search_table_31015(I, V, T, K, 6)

    return cal, I_nom

def search_table_31015(I, V, T, K, Pos):
    """ Esta función busca en la tabla 310.15(B)(16) el calibre del conductor y la corriente nominal de este.
    Para tener en cuenta el calibre mínimo del conductor la busqueda en la tabla inicia en la posición
    en la que se encuentra dicho calibre mínimo """

    # 1. Iniciamos la variable cal para que las posiciones 2, 3, 4, 5 y 6 puedan entrar en la tabla
    cal = 'no gauge'
    I_nom = ''

    # 2. Se selecciona el calibre del conductor dependiendo del material (Cu o Al) y la temperatura
    if K == 'Cu':
        if T == 60:
            if Pos == 1:
                if I <= 15:
                    cal = '14 AWG'
                    I_nom = 15
                elif I <= 20:
                    cal = '12 AWG'
                    I_nom = 20
                elif I <= 30:
                    cal = '10 AWG'
                    I_nom = 30
                else:
                    cal = 'no gauge'
                    Pos = 2
            if cal == 'no gauge' and Pos <= 2:
                if I <= 40:
                    cal = '8 AWG'
                    I_nom = 40
                else:
                    cal = 'no gauge'
                    Pos = 3
            if cal == 'no gauge' and Pos <= 3:
                if I <= 55:
                    cal = '6 AWG'
                    I_nom = 55
                elif I <= 70:
                    cal = '4 AWG'
                    I_nom = 70
                else:
                    cal = 'no gauge'
                    Pos = 4
            if cal == 'no gauge' and Pos <= 4:
                if I <= 95:
                    cal = '2 AWG'
                    I_nom = 95
                else:
                    cal = 'no gauge'
                    Pos = 5
            if cal == 'no gauge' and Pos <= 5:
                if I <= 110:
                    cal = '1 AWG'
                    I_nom = 110
                else:
                    cal = 'no gauge'
                    Pos = 6
            if cal == 'no gauge' and Pos <= 6:
                if I <= 125:
                    cal = '1/0 AWG'
                    I_nom = 125
                elif I <= 145:
                    cal = '2/0 AWG'
                    I_nom = 145
                elif I <= 165:
                    cal = '3/0 AWG'
                    I_nom = 165
                elif I <= 195:
                    cal = '4/0 AWG'
                    I_nom = 195
                elif I <= 215:
                    cal = '250 MCM'
                    I_nom = 215
                elif I <= 240:
                    cal = '300 MCM'
                    I_nom = 240
                elif I <= 260:
                    cal = '350 MCM'
                    I_nom = 260
                elif I <= 280:
                    cal = '400 MCM'
                    I_nom = 280
                elif I <= 320:
                    cal = '500 MCM'
                    I_nom = 320
                elif I <= 350:
                    cal = '600 MCM'
                    I_nom = 350
                elif I <= 385:
                    cal = '700 MCM'
                    I_nom = 385
                elif I <= 400:
                    cal = '750 MCM'
                    I_nom = 400
                elif I <= 410:
                    cal = '800 MCM'
                    I_nom = 410
                elif I <= 435:
                    cal = '900 MCM'
                    I_nom = 485
                elif I <= 455:
                    cal = '1000 MCM'
                    I_nom = 455
                else:
                    cal = 'no gauge'
        elif T == 75:
            if Pos == 1:
                if I <= 20:
                    cal = '14 AWG'
                    I_nom = 20
                elif I <= 25:
                    cal = '12 AWG'
                    I_nom = 25
                elif I <= 35:
                    cal = '10 AWG'
                    I_nom = 35
                else:
                    cal = 'no gauge'
                    Pos = 2
            if cal == 'no gauge' and Pos <= 2:
                if I <= 50:
                    cal = '8 AWG'
                    I_nom = 50
                else:
                    cal = 'no gauge'
                    Pos = 3
            if cal == 'no gauge' and Pos <= 3:
                if I <= 65:
                    cal = '6 AWG'
                    I_nom = 65
                elif I <= 85:
                    cal = '4 AWG'
                    I_nom = 85
                else:
                    cal = 'no gauge'
                    Pos = 4
            if cal == 'no gauge' and Pos <= 4:
                if I <= 115:
                    cal = '2 AWG'
                    I_nom = 115
                else:
                    cal = 'no gauge'
                    Pos = 5
            if cal == 'no gauge' and Pos <= 5:
                if I <= 130:
                    cal = '1 AWG'
                    I_nom = 130
                else:
                    cal = 'no gauge'
                    Pos = 6
            if cal == 'no gauge' and Pos <= 6:
                if I <= 150:
                    cal = '1/0 AWG'
                    I_nom = 150
                elif I <= 175:
                    cal = '2/0 AWG'
                    I_nom = 175
                elif I <= 200:
                    cal = '3/0 AWG'
                    I_nom = 200
                elif I <= 230:
                    cal = '4/0 AWG'
                    I_nom = 230
                elif I <= 255:
                    cal = '250 MCM'
                    I_nom = 255
                elif I <= 285:
                    cal = '300 MCM'
                    I_nom = 285
                elif I <= 310:
                    cal = '350 MCM'
                    I_nom = 310
                elif I <= 335:
                    cal = '400 MCM'
                    I_nom = 335
                elif I <= 380:
                    cal = '500 MCM'
                    I_nom = 380
                elif I <= 420:
                    cal = '600 MCM'
                    I_nom = 420
                elif I <= 460:
                    cal = '700 MCM'
                    I_nom = 460
                elif I <= 475:
                    cal = '750 MCM'
                    I_nom = 475
                elif I <= 490:
                    cal = '800 MCM'
                    I_nom = 490
                elif I <= 520:
                    cal = '900 MCM'
                    I_nom = 520
                elif I <= 545:
                    cal = '1000 MCM'
                    I_nom = 545
                else:
                    cal = 'no gauge'
        else:
            if Pos == 1:
                if I <= 25:
                    cal = '14 AWG'
                    I_nom = 25
                elif I <= 30:
                    cal = '12 AWG'
                    I_nom = 30
                elif I <= 40:
                    cal = '10 AWG'
                    I_nom = 40
                else:
                    cal = 'no gauge'
                    Pos = 2
            if cal == 'no gauge' and Pos <= 2:
                if I <= 55:
                    cal = '8 AWG'
                    I_nom = 55
                else:
                    cal = 'no gauge'
                    Pos = 3
            if cal == 'no gauge' and Pos <= 3:
                if I <= 75:
                    cal = '6 AWG'
                    I_nom = 75
                elif I <= 95:
                    cal = '4 AWG'
                    I_nom = 95
                else:
                    cal = 'no gauge'
                    Pos = 4
            if cal == 'no gauge' and Pos <= 4:
                if I <= 130:
                    cal = '2 AWG'
                    I_nom = 130
                else:
                    cal = 'no gauge'
                    Pos = 5
            if cal == 'no gauge' and Pos <= 5:
                if I <= 145:
                    cal = '1 AWG'
                    I_nom = 145
                else:
                    cal = 'no gauge'
                    Pos = 6
            if cal == 'no gauge' and Pos <= 6:
                if I <= 170:
                    cal = '1/0 AWG'
                    I_nom = 170
                elif I <= 195:
                    cal = '2/0 AWG'
                    I_nom = 195
                elif I <= 225:
                    cal = '3/0 AWG'
                    I_nom = 225
                elif I <= 260:
                    cal = '4/0 AWG'
                    I_nom = 260
                elif I <= 290:
                    cal = '250 MCM'
                    I_nom = 290
                elif I <= 320:
                    cal = '300 MCM'
                    I_nom = 320
                elif I <= 350:
                    cal = '350 MCM'
                    I_nom = 350
                elif I <= 380:
                    cal = '400 MCM'
                    I_nom = 380
                elif I <= 430:
                    cal = '500 MCM'
                    I_nom = 430
                elif I <= 475:
                    cal = '600 MCM'
                    I_nom = 475
                elif I <= 520:
                    cal = '700 MCM'
                    I_nom = 520
                elif I <= 535:
                    cal = '750 MCM'
                    I_nom = 535
                elif I <= 555:
                    cal = '800 MCM'
                    I_nom = 555
                elif I <= 585:
                    cal = '900 MCM'
                    I_nom = 585
                elif I <= 615:
                    cal = '1000 MCM'
                    I_nom = 615
                else:
                    cal = 'no gauge'
                    I_nom = 'no current'
    else:
        if T == 60:
            if Pos == 1:
                if I <= 15:
                    cal = '12 AWG'
                    I_nom = 15
                elif I <= 25:
                    cal = '10 AWG'
                    I_nom = 25
                elif I <= 35:
                    cal = '8 AWG'
                    I_nom = 35
                else:
                    cal = 'no gauge'
                    Pos = 2
            if cal == 'no gauge' and Pos <= 2:
                if I <= 40:
                    cal = '6 AWG'
                    I_nom = 40
                else:
                    cal = 'no gauge'
                    Pos = 3
            if cal == 'no gauge' and Pos <= 3:
                if I <= 55:
                    cal = '4 AWG'
                    I_nom = 55
                elif I <= 75:
                    cal = '2 AWG'
                    I_nom = 75
                else:
                    cal = 'no gauge'
                    Pos = 4
            if cal == 'no gauge' and Pos <= 4:
                if I <= 85:
                    cal = '1 AWG'
                    I_nom = 85
                else:
                    cal = 'no gauge'
                    Pos = 5
            if cal == 'no gauge' and Pos <= 5:
                if I <= 100:
                    cal = '1/0 AWG'
                    I_nom = 100
                else:
                    cal = 'no gauge'
                    Pos = 6
            if cal == 'no gauge' and Pos <= 6:
                if I <= 115:
                    cal = '2/0 AWG'
                    I_nom = 115
                elif I <= 130:
                    cal = '3/0 AWG'
                    I_nom = 130
                elif I <= 150:
                    cal = '4/0 AWG'
                    I_nom = 150
                elif I <= 170:
                    cal = '250 MCM'
                    I_nom = 170
                elif I <= 195:
                    cal = '300 MCM'
                    I_nom = 195
                elif I <= 210:
                    cal = '350 MCM'
                    I_nom = 210
                elif I <= 225:
                    cal = '400 MCM'
                    I_nom = 225
                elif I <= 260:
                    cal = '500 MCM'
                    I_nom = 260
                elif I <= 285:
                    cal = '600 MCM'
                    I_nom = 285
                elif I <= 315:
                    cal = '700 MCM'
                    I_nom = 315
                elif I <= 320:
                    cal = '750 MCM'
                    I_nom = 320
                elif I <= 330:
                    cal = '800 MCM'
                    I_nom = 330
                elif I <= 355:
                    cal = '900 MCM'
                    I_nom = 355
                elif I <= 375:
                    cal = '1000 MCM'
                    I_nom = 375
                else:
                    cal = 'no gauge'
        elif T == 75:
            if Pos == 1:
                if I <= 20:
                    cal = '12 AWG'
                    I_nom = 20
                elif I <= 30:
                    cal = '10 AWG'
                    I_nom = 30
                else:
                    cal = 'no gauge'
                    Pos = 2
            if cal == 'no gauge' and Pos <= 2:
                if I <= 40:
                    cal = '8 AWG'
                    I_nom = 40
                else:
                    cal = 'no gauge'
                    Pos = 3
            if cal == 'no gauge' and Pos <= 3:
                if I <= 50:
                    cal = '6 AWG'
                    I_nom = 50
                elif I <= 65:
                    cal = '4 AWG'
                    I_nom = 65
                else:
                    cal = 'no gauge'
                    Pos = 4
            if cal == 'no gauge' and Pos <= 4:
                if I <= 90:
                    cal = '2 AWG'
                    I_nom = 90
                else:
                    cal = 'no gauge'
                    Pos = 5
            if cal == 'no gauge' and Pos <= 5:
                if I <= 100:
                    cal = '1 AWG'
                    I_nom = 100
                else:
                    cal = 'no gauge'
                    Pos = 6
            if cal == 'no gauge' and Pos <= 6:
                if I <= 120:
                    cal = '1/0 AWG'
                    I_nom = 120
                elif I <= 135:
                    cal = '2/0 AWG'
                    I_nom = 135
                elif I <= 155:
                    cal = '3/0 AWG'
                    I_nom = 155
                elif I <= 180:
                    cal = '4/0 AWG'
                    I_nom = 180
                elif I <= 205:
                    cal = '250 MCM'
                    I_nom = 205
                elif I <= 230:
                    cal = '300 MCM'
                    I_nom = 230
                elif I <= 250:
                    cal = '350 MCM'
                    I_nom = 250
                elif I <= 270:
                    cal = '400 MCM'
                    I_nom = 270
                elif I <= 310:
                    cal = '500 MCM'
                    I_nom = 310
                elif I <= 340:
                    cal = '600 MCM'
                    I_nom = 340
                elif I <= 375:
                    cal = '700 MCM'
                    I_nom = 375
                elif I <= 385:
                    cal = '750 MCM'
                    I_nom = 385
                elif I <= 395:
                    cal = '800 MCM'
                    I_nom = 395
                elif I <= 425:
                    cal = '900 MCM'
                    I_nom = 425
                elif I <= 445:
                    cal = '1000 MCM'
                    I_nom = 445
                else:
                    cal = 'no gauge'
        else:
            if Pos == 1:
                if I <= 25:
                    cal = '12 AWG'
                    I_nom = 25
                elif I <= 35:
                    cal = '10 AWG'
                    I_nom = 35
                else:
                    cal = 'no gauge'
                    Pos = 2
            if cal == 'no gauge' and Pos <= 2:
                if I <= 45:
                    cal = '8 AWG'
                    I_nom = 45
                else:
                    cal = 'no gauge'
                    Pos = 3
            if cal == 'no gauge' and Pos <= 3:
                if I <= 55:
                    cal = '6 AWG'
                    I_nom = 55
                elif I <= 75:
                    cal = '4 AWG'
                    I_nom = 75
                else:
                    cal = 'no gauge'
                    Pos = 4
            if cal == 'no gauge' and Pos <= 4:
                if I <= 100:
                    cal = '2 AWG'
                    I_nom = 100
                else:
                    cal = 'no gauge'
                    Pos = 5
            if cal == 'no gauge' and Pos <= 5:
                if I <= 115:
                    cal = '1 AWG'
                    I_nom = 115
                else:
                    cal = 'no gauge'
                    Pos = 6
            if cal == 'no gauge' and Pos <= 6:
                if I <= 135:
                    cal = '1/0 AWG'
                    I_nom = 135
                elif I <= 150:
                    cal = '2/0 AWG'
                    I_nom = 150
                elif I <= 175:
                    cal = '3/0 AWG'
                    I_nom = 175
                elif I <= 205:
                    cal = '4/0 AWG'
                    I_nom = 205
                elif I <= 230:
                    cal = '250 MCM'
                    I_nom = 230
                elif I <= 260:
                    cal = '300 MCM'
                    I_nom = 260
                elif I <= 280:
                    cal = '350 MCM'
                    I_nom = 280
                elif I <= 305:
                    cal = '400 MCM'
                    I_nom = 305
                elif I <= 350:
                    cal = '500 MCM'
                    I_nom = 350
                elif I <= 385:
                    cal = '600 MCM'
                    I_nom = 385
                elif I <= 425:
                    cal = '700 MCM'
                    I_nom = 425
                elif I <= 435:
                    cal = '750 MCM'
                    I_nom = 435
                elif I <= 445:
                    cal = '800 MCM'
                    I_nom = 445
                elif I <= 480:
                    cal = '900 MCM'
                    I_nom = 480
                elif I <= 500:
                    cal = '1000 MCM'
                    I_nom = 500
                else:
                    cal = 'no gauge'
                    I_nom = 'no current'

    return cal, I_nom

def Motor_Current_Calculation(P, V, n, Ph):
    """ Esta función realiza la selección de la corriente de un motor basado en las tablas
    de la sección 430 de la NTC 2050 segunda actualización. Para eso toma como parámetros la potencia (P) en HP
    la tensión (V), si es sincrono o asincrono (n) y el número de fases (Ph).

    """

    # 1. Preguntar cuantas fases tiene el motor
    if Ph == 1:
        # 2. Preguntar por la potencia del motor
        if P == (1/6):
            # 3. Preguntar por el nivel de tensión del motor
            if V == 115:
                I = 4.4
            elif V == 200:
                I = 2.5
            elif V == 208:
                I = 2.4
            elif V == 230:
                I = 2.2
        elif P == (1/4):
            if V == 115:
                I = 5.8
            elif V == 200:
                I = 3.3
            elif V == 208:
                I = 3.2
            elif V == 230:
                I = 2.9
        elif P == (1/3):
            if V == 115:
                I = 7.2
            elif V == 200:
                I = 4.1
            elif V == 208:
                I = 4
            elif V == 230:
                I = 3.6
        elif P == (0.5):
            if V == 115:
                I = 9.8
            elif V == 200:
                I = 5.6
            elif V == 208:
                I = 5.4
            elif V == 230:
                I = 4.9
        elif P == (3/4):
            if V == 115:
                I = 13.8
            elif V == 200:
                I = 7.9
            elif V == 208:
                I = 7.6
            elif V == 230:
                I = 6.9
        elif P == 1:
            if V == 115:
                I = 16
            elif V == 200:
                I = 9.2
            elif V == 208:
                I = 8.8
            elif V == 230:
                I = 8
        elif P == 1.5:
            if V == 115:
                I = 20
            elif V == 200:
                I = 11.5
            elif V == 208:
                I = 11
            elif V == 230:
                I = 10
        elif P == 2:
            if V == 115:
                I = 24
            elif V == 200:
                I = 13.8
            elif V == 208:
                I = 13.2
            elif V == 230:
                I = 12
        elif P == 3:
            if V == 115:
                I = 34
            elif V == 200:
                I = 19.6
            elif V == 208:
                I = 18.7
            elif V == 230:
                I = 17
        elif P == 5:
            if V == 115:
                I = 56
            elif V == 200:
                I = 32.2
            elif V == 208:
                I = 30.8
            elif V == 230:
                I = 28
        elif P == 7.5:
            if V == 115:
                I = 80
            elif V == 200:
                I = 46
            elif V == 208:
                I = 44
            elif V == 230:
                I = 40
        elif P == 10:
            if V == 115:
                I = 100
            elif V == 200:
                I = 57.5
            elif V == 208:
                I = 55
            elif V == 230:
                I = 50

    # 1. Preguntar cuantas fases tiene el motor
    if Ph == 2:
        # 2. Preguntar por la potencia del motor
        if P == (1/2):
            # 3. Preguntar por el nivel de tensión del motor
            if V == 115:
                I = 4
            elif V == 230:
                I = 2
            elif V == 460:
                I = 1
            elif V == 575:
                I = 0.8
        elif P == (3/4):
            if V == 115:
                I = 4.8
            elif V == 230:
                I = 2.4
            elif V == 460:
                I = 1.2
            elif V == 575:
                I = 1
        elif P == 1:
            if V == 115:
                I = 6.4
            elif V == 230:
                I = 3.2
            elif V == 460:
                I = 1.6
            elif V == 575:
                I = 0.8
        elif P == (1.5):
            if V == 115:
                I = 9
            elif V == 230:
                I = 4.5
            elif V == 460:
                I = 2.3
            elif V == 575:
                I = 1.8
        elif P == 2:
            if V == 115:
                I = 11.8
            elif V == 230:
                I = 5.9
            elif V == 460:
                I = 3
            elif V == 575:
                I = 2.4
        elif P == 3:
            if V == 230:
                I = 8.3
            elif V == 460:
                I = 4.2
            elif V == 575:
                I = 3.3
        elif P == 5:
            if V == 230:
                I = 13.2
            elif V == 460:
                I = 6.6
            elif V == 575:
                I = 5.3
        elif P == 7.5:
            if V == 230:
                I = 19
            elif V == 460:
                I = 9
            elif V == 575:
                I = 8
        elif P == 10:
            if V == 230:
                I = 24
            elif V == 460:
                I = 12
            elif V == 575:
                I = 10
        elif P == 15:
            if V == 230:
                I = 36
            elif V == 460:
                I = 18
            elif V == 575:
                I = 14
        elif P == 20:
            if V == 230:
                I = 47
            elif V == 460:
                I = 23
            elif V == 575:
                I = 19
        elif P == 25:
            if V == 230:
                I = 59
            elif V == 460:
                I = 29
            elif V == 575:
                I = 24
        elif P == 30:
            if V == 230:
                I = 69
            elif V == 460:
                I = 35
            elif V == 575:
                I = 28
        elif P == 40:
            if V == 230:
                I = 90
            elif V == 460:
                I = 45
            elif V == 575:
                I = 36
        elif P == 50:
            if V == 230:
                I = 113
            elif V == 460:
                I = 56
            elif V == 575:
                I = 45
        elif P == 60:
            if V == 230:
                I = 133
            elif V == 460:
                I = 67
            elif V == 575:
                I = 53
        elif P == 75:
            if V == 230:
                I = 166
            elif V == 460:
                I = 83
            elif V == 575:
                I = 66
        elif P == 100:
            if V == 230:
                I = 218
            elif V == 460:
                I = 109
            elif V == 575:
                I = 87
        elif P == 125:
            if V == 230:
                I = 270
            elif V == 460:
                I = 135
            elif V == 575:
                I = 108
        elif P == 150:
            if V == 230:
                I = 312
            elif V == 460:
                I = 156
            elif V == 575:
                I = 125
        elif P == 200:
            if V == 230:
                I = 416
            elif V == 460:
                I = 208
            elif V == 575:
                I = 167
    if Ph == 3:
        if n == 'NTC2050-As':
            if P == 0.5:
                if V == 115:
                    I = 4.4
                elif V == 200:
                    I = 2.5
                elif V == 208:
                    I = 2.4
                elif V == 230:
                    I = 2.2
                elif V == 460:
                    I = 1.1
                elif V == 575:
                    I = 0.9
            elif P == 0.75:
                if V == 115:
                    I = 6.4
                elif V == 200:
                    I = 3.7
                elif V == 208:
                    I = 3.5
                elif V == 230:
                    I = 3.2
                elif V == 460:
                    I = 1.6
                elif V == 575:
                    I = 1.3
            elif P == 1:
                if V == 115:
                    I = 8.4
                elif V == 200:
                    I = 4.8
                elif V == 208:
                    I = 4.6
                elif V == 230:
                    I = 4.2
                elif V == 460:
                    I = 2.1
                elif V == 575:
                    I = 1.7
            elif P == 1.5:
                if V == 115:
                    I = 12
                elif V == 200:
                    I = 6.9
                elif V == 208:
                    I = 6.6
                elif V == 230:
                    I = 6
                elif V == 460:
                    I = 3
                elif V == 575:
                    I = 2.4
            elif P == 2:
                if V == 115:
                    I = 13.6
                elif V == 200:
                    I = 7.8
                elif V == 208:
                    I = 7.5
                elif V == 230:
                    I = 6.8
                elif V == 460:
                    I = 3.4
                elif V == 575:
                    I = 2.7
            elif P == 3:
                if V == 200:
                    I = 11
                elif V == 208:
                    I = 10.6
                elif V == 230:
                    I = 9.6
                elif V == 460:
                    I = 4.8
                elif V == 575:
                    I = 3.9
            elif P == 5:
                if V == 200:
                    I = 17.5
                elif V == 208:
                    I = 16.7
                elif V == 230:
                    I = 15.2
                elif V == 460:
                    I = 7.6
                elif V == 575:
                    I = 6.1
            elif P == 7.5:
                if V == 200:
                    I = 25.3
                elif V == 208:
                    I = 24.2
                elif V == 230:
                    I = 22
                elif V == 460:
                    I = 11
                elif V == 575:
                    I = 9
            elif P == 10:
                if V == 200:
                    I = 32.2
                elif V == 208:
                    I = 30.8
                elif V == 230:
                    I = 28
                elif V == 460:
                    I = 14
                elif V == 575:
                    I = 11
            elif P == 15:
                if V == 200:
                    I = 48.3
                elif V == 208:
                    I = 46.2
                elif V == 230:
                    I = 42
                elif V == 460:
                    I = 21
                elif V == 575:
                    I = 17
            elif P == 20:
                if V == 200:
                    I = 62.1
                elif V == 208:
                    I = 59.4
                elif V == 230:
                    I = 54
                elif V == 460:
                    I = 27
                elif V == 575:
                    I = 22
            elif P == 25:
                if V == 200:
                    I = 78.2
                elif V == 208:
                    I = 74.8
                elif V == 230:
                    I = 68
                elif V == 460:
                    I = 34
                elif V == 575:
                    I = 27
            elif P == 30:
                if V == 200:
                    I = 92
                elif V == 208:
                    I = 88
                elif V == 230:
                    I = 80
                elif V == 460:
                    I = 40
                elif V == 575:
                    I = 32
            elif P == 40:
                if V == 200:
                    I = 120
                elif V == 208:
                    I = 114
                elif V == 230:
                    I = 104
                elif V == 460:
                    I = 52
                elif V == 575:
                    I = 41
            elif P == 50:
                if V == 200:
                    I = 150
                elif V == 208:
                    I = 143
                elif V == 230:
                    I = 130
                elif V == 460:
                    I = 65
                elif V == 575:
                    I = 52
            elif P == 60:
                if V == 200:
                    I = 177
                elif V == 208:
                    I = 169
                elif V == 230:
                    I = 154
                elif V == 460:
                    I = 77
                elif V == 575:
                    I = 62
            elif P == 75:
                if V == 200:
                    I = 221
                elif V == 208:
                    I = 211
                elif V == 230:
                    I = 192
                elif V == 460:
                    I = 96
                elif V == 575:
                    I = 77
            elif P == 100:
                if V == 200:
                    I = 285
                elif V == 208:
                    I = 273
                elif V == 230:
                    I = 248
                elif V == 460:
                    I = 124
                elif V == 575:
                    I = 99
            elif P == 125:
                if V == 200:
                    I = 359
                elif V == 208:
                    I = 343
                elif V == 230:
                    I = 312
                elif V == 460:
                    I = 156
                elif V == 575:
                    I = 125
            elif P == 150:
                if V == 200:
                    I = 414
                elif V == 208:
                    I = 396
                elif V == 230:
                    I = 360
                elif V == 460:
                    I = 180
                elif V == 575:
                    I = 144
            elif P == 200:
                if V == 200:
                    I = 552
                elif V == 208:
                    I = 528
                elif V == 230:
                    I = 480
                elif V == 460:
                    I = 240
                elif V == 575:
                    I = 192
            elif P == 250:
                if V == 460:
                    I = 302
                elif V == 575:
                    I = 242
            elif P == 300:
                if V == 460:
                    I = 361
                elif V == 575:
                    I = 289
            elif P == 350:
                if V == 460:
                    I = 414
                elif V == 575:
                    I = 336
            elif P == 400:
                if V == 460:
                    I = 477
                elif V == 575:
                    I = 382
            elif P == 450:
                if V == 460:
                    I = 515
                elif V == 575:
                    I = 412
            elif P == 500:
                if V == 460:
                    I = 590
                elif V == 575:
                    I = 472
        else:
            if P == 25:
                if V == 230:
                    I = 53
                elif V == 460:
                    I = 26
                elif V == 575:
                    I = 21
            elif P == 30:
                if V == 230:
                    I = 63
                elif V == 460:
                    I = 32
                elif V == 575:
                    I = 26
            elif P == 40:
                if V == 230:
                    I = 83
                elif V == 460:
                    I = 41
                elif V == 575:
                    I = 33
            elif P == 50:
                if V == 230:
                    I = 104
                elif V == 460:
                    I = 52
                elif V == 575:
                    I = 42
            elif P == 60:
                if V == 230:
                    I = 123
                elif V == 460:
                    I = 61
                elif V == 575:
                    I = 49
            elif P == 75:
                if V == 230:
                    I = 155
                elif V == 460:
                    I = 78
                elif V == 575:
                    I = 62
            elif P == 100:
                if V == 230:
                    I = 202
                elif V == 460:
                    I = 101
                elif V == 575:
                    I = 81
            elif P == 125:
                if V == 230:
                    I = 253
                elif V == 460:
                    I = 126
                elif V == 575:
                    I = 101
            elif P == 150:
                if V == 230:
                    I = 302
                elif V == 460:
                    I = 151
                elif V == 575:
                    I = 121
            elif P == 200:
                if V == 230:
                    I = 400
                elif V == 460:
                    I = 201
                elif V == 575:
                    I = 161
    return I

def current_load(P, U, Ph, PF, V, n):
    """ Esta función calcula la corriente nominal de cualquier tipo de carga (motores y demás)
    a partir de la potencia nominal, el número de fases, el factor de potencia y la tensión nominal
    """

    # 1. Verificar si la carga es trifásica, monofásica o bifásica
    if Ph == 3:
        # 2. Calcular la corriente trifásica dependiendo si la potencia esta en HP, kW o kVA
        if U == 'kW':
            I = (P * 1000 ) / (V * PF * ( 3 ** 0.5))
        elif U == 'kVA':
            I = (P * 1000) / (V * (3 ** 0.5))
        else:
            if n == 'NTC2050-As' or n == 'NTC2050-Sin':
                I = Motor_Current_Calculation(P, V, n, Ph)
            else:
                I = (P * 746) / (V * PF * n * (3 ** 0.5))
    else:
        # 3. Calcular la corriente monofásica dependiendo si la potencia esta en HP, kW o kVA
        if U == 'kW':
            I = (P * 1000) / (V * PF)
        elif U == 'kVA':
            I = (P * 1000) / V
        else:
            if n == 'NTC2050-As' or n == 'NTC2050-Sin':
                I = Motor_Current_Calculation(P, V, n, Ph)
            else:
                I = (P * 746) / (V * PF * n)

    return I

def cable_calculation(P, U, Ph, PF, V, L, T = 75, T_amb = 25, CL = 'y', K = 'Cu', NC = 3, KC = 'st', n = 0.6):
    """ Esta función realiza el cálculo de conductores de baja tensión basado en la NTC 2050 del 2020
    a partir de los siguientes parametros ingresados por el usuario:

    P- Potencia (P)
    U- Unidades (kW, kVA, HP)
    Ph- Fases (1, 2 o 3)
    PF- Factor de potencia
    V- Tensión (V)
    L- Longitud (m)
    T- Temperatura del conductor (ºC)
    T_amb- Temperatura ambiente (ºC)
    CL- Carga continua (Si/No)
    K- Tipo de material del cable (Al, Cu)
    NC- Número de conductores
    KC- Tipo de conduit (Steal, PVC)

    """

    # 1. Calcular la corriente nominal del conductor a partir de la Potencia
    I = current_load(P, U, Ph, PF, V, n)

    print('Corriente nominal: ', I)

    # 2. Multiplicar las cargas continuas por 125%
    if CL == 'y':
        I_continuous = I * 1.25
    else:
        I_continuous = I

    print('Corriente de carga continua: ', I_continuous)

    # 3. Seleccionar la corriente nominal del conductor de acuerdo a la temperatura ambiente.
    correction_factor = temperature_correction_factor(T_amb, T)
    print('Factor de corrección por temperatura: ', correction_factor)

    # 4. Si no se puede seleccionar ningún factor de corrección entonces se asignará el valor de 1
    # a la variable correction_factor.
    if correction_factor == 'no temp. correc. factor':
        correction_factor = 1
        nota_1 = 'Se asumió un factor de corrección de ajuste de 1, debido a que no se encontró un factor para la TEMPERATURA AMBIENTE ingresada'
    else:
        nota_1 = ''

    # 5. Seleccionar el factor de ajuste para más de tres conductores portadores de corriente.
    # Si no hay más de tres conductores en una misma canalización se asignará el valor de 1
    # al factor de ajuste de más de tres conductores.
    if NC <= 3:
        adjustment_factor = 1
    else:
        adjustment_factor = adjustment_correction_factor(NC)
    print('Factor de ajuste: ', adjustment_factor)

    # 6. Evaluar si la corriente nominal ajustada del conductor es superior a la corriente nominal de la carga
    gauge, nominal_current = conductor_gauge((I_continuous / (correction_factor * adjustment_factor)), V, T, K)
    print('La corriente nominal del conductor de calibre %s es %.1f A' % (gauge, nominal_current))

    # 7. Ajustar la corriente nominal del conductor seleccionado de acuerdo al factor de correcciónote
    # y de acuerdo al valor de ajuste
    I_adjust = nominal_current * correction_factor * adjustment_factor
    print('Corriente ajustada: ', I_adjust)

    # 8. Calculo de la regulación de tensión
    Vdrop, Vdrop_percent, R, X = drop_voltage_calculation(Ph, V, L, I, PF, gauge, KC, K)

    # 9. Si la caída de tensión es superior al 3% se debe seleccionar un conductor con una caída de tensión
    # inferior a esta.
    while Vdrop_percent > 3:
        gauge = find_next_gauge(gauge)
        Vdrop_percent = drop_voltage_calculation(Ph, V, L, I, PF, gauge, KC, K)

    # 10. Calcular el conductor de neutro
    if Ph == 1:
        neutral_conductor = gauge
    else:
        neutral_conductor = '-'

    # 11. Calcular la protección del circuito
    protective = protective_device(nominal_current * correction_factor * adjustment_factor, I_continuous)

    if protective == '-':
        protective = protective_device(nominal_current * correction_factor * adjustment_factor, I)
    print('El dispositivo de protección es: ', protective)

    # 12. Selección del conductor de protección de equipos (o de puesta a tierra) de equipos
    earth = earth_conductor(protective, K)

    # 13. Imprimir los resultados del cálculo
    return gauge, neutral_conductor, earth, Vdrop_percent, protective, correction_factor
