def arc_flash_boundary(V_phases, P_trafo, Z_trafo, t, output = 'm'):

    """ 1.Método de cálculo de Ralph Lee: la distancia de la frontera de relámpago se calcula de acuerdo con la
    siguiente formula:

    Dc = [2.65 x MVAbf x t]^1/2

    Donde,
    t: es el tiempo en segundos de exposición al arco en segundos. Normalmente depende del tiempo de despeje del
    dispositivo de protección.
    MVAbf: es la falla sólida en MVA en el punto involucrado
    Dc: es la distancia en pies de la persona a la fuente de arco para justo una quemadura curable
    (es decir, la temperatura de la piel se mantiene a menos de 80 ºC).

    La potencia máxima en un arco trifásico se puede calcular de acuerdo a la siguiente ecuación:

    P = 1.732 x V x Isc x 10^6 x 0.707^2

    Donde,
    V: es la tensión entre fases y está en V.
    Isc se calcula de acuerdo a la siguiente formula:

    Isc = {[MVAbase x 10^6]/[1.732 x V]} x {100/%Z}

    Donde,
    %Z: es la impedancia de cortocircuito del transformador la cual se debe tomar de la NTC 818, 819 o 3445.

    Un método alternativo para calcular esta distancia de frontera es el que describe la siguiente ecuación:

    Dc = [53 x MVA x t]^1/2

    Donde,
    MVA: son los MVA nominales del transformador. Para transformadores
    con valores nominales menores de 0.75 MVA multiplique los MVA nominales del transformador por 1.25.

    Isc = [(MVAbase x 10^6) / (1.723 x V)]*[100 / %Z]"""

    # Calculo de la corriente de cortocircuito
    Isc = ((P_trafo * 10e6)/(1.732 * V_phases)) * (100 / Z_trafo)

    # Potencia aparente en MVA
    P = 1.732 * V_phases * Isc * 1e-6

    # Distancia de arco en pies
    Dc = (2.65 * P * t)**0.5

    # Convertir a metros si es necesario
    if output == 'm':
        return Dc * 0.3048
    else:
        return Dc

def incident_energy_600_more(V, F, d, t = 2):
    """ Esta función calcula la energía incidente basado en el anexo D de la NFPA 70E del 2015

    Para realizar dicho cálculo es necesario ingresar la tensión entre fases del sistema (V, kV), la corriente de
    falla de cortocircuito sólido (F, kA), la distancia a la fuente de arco (cm), el tiempo de duración del arco
    (s). El resultado se da en cal/cm2 """

    """Este método se puede utilizar solo para arcos trifásicos abierto en sistemas con valores nominales
    superiores a 600 V """

    D = d * 100
    V_phases = V / 1000

    E = (793 * F * V_phases * t) / D**2

    return E

    """ Dependiendo del nivel de tensión vamos a seleccionar el tipo de método de cálculo de la
    energía incidente """

def incident_energy_doughty_neal(F, kind_of_panel, t, kind_of_arc):
    """ Esta función calcula el arco eléctrico de acuerdo al ensayo de Daughty Neal, para ello es necesario
    la máxima corriente de falla de cortocircuito trifásico sólido disponible en el equipo y el mínimo nivel
    de falla en el que el arco se sostendrá (ver página 66 de la NFPA 70E del 2015). Hay dos ecuaciones:
    una para el cálculo al aire libre y otra para en una caja cúbica, por eso uno de los parámetros de ingreso a
    la función es la variable kind_of_arc la cual puede tomar dos valores: C- Closed o O- Open. """

    if kind_of_panel == 'CCM':
        D = 45
    else:
        D = 61

    if kind_of_arc == 'C':
        E = 1038.7 * (D ** (-1.4738)) * t * (0.0093 * (F ** 2) - 0.3453 * F + 5.9675)
    else:
        E = 5271 * (D ** (-1.9593)) * t * (0.0016 * (F ** 2) - 0.0076 * F + 0.8938)

    return E

def incident_energy_IEEE1584(V, Ibf, G, t, d, kind_of_arc, kind_of_panel, kind_of_earth):
    """ Esta función calcula el arco eléctrico de acuerdo a la IEEE 1584 Guía para Efectuar el cálculo del
    riesgo de relámpago de arco. Las limitantes de este método de cálculo son:
    0.208 kV a 15 kV trifásico
    50 - 60 Hz
    0.7 - 106 kA de corriente de cortocircuito
    13 - 152 mm de distancia entre conductores.

    Este método es para fallas trifásicas """

    # Se importa el módulo math para poder realizar operaciones logaritmicas
    import math

    # La distancia d ingresada está en metros, pero el método de la IEEE1584 exige que sea en mm.
    # Por lo que en este punto se realiza la conversión de metros a milímetros.
    D = d * 1000

    V_phases = V/1000

    if V_phases < 1:
        # Se asigna valor a la constante K dependiendo del tipo de arco (O- Open, C- Closed)
        if kind_of_arc == 'O':
            K = -0.153
        else:
            K = -0.097
        print('K= ',K)

        # Se calcula la corriente de arco en kA
        Ia = 10 ** (K + 0.662 * math.log10(Ibf) + 0.0966 * V_phases + 0.000526 * G + 0.5588 * V_phases * math.log10(Ibf) - 0.00304 * G * math.log10(Ibf))
    else:
        # Se calcula la corriente de arco en kA
        Ia = 10 ** (0.00402 + 0.983 * math.log10(Ibf))

    # Se calcula la energía incidente para un segundo tiempo de arco de acuerdo a como lo establece
    # el estandar IEEE 1584.
    Ia_2t = 0.85 * Ia

    # Se asignan los valores a las constantes k1 y k2
    if kind_of_arc == 'O':
        k1 = -0.792
    else:
        k1 = -0.555

    # HR se refiere a alta resistencia
    if kind_of_earth == 'HR':
        k2 = -0.113
    else:
        k2 = 0

    # Se calcula la energía incidente normalizada
    En = 10 ** (k1 + k2 + 1.081 * math.log10(Ia) + 0.0011 * G)
    En_2t = 10 ** (k1 + k2 + 1.081 * math.log10(Ia_2t) + 0.0011 * G)

    # Se le asigna valor a la constante X:
    if kind_of_arc == 'O':
        x = 2
    else:
        if V_phases <= 1:
            if kind_of_panel == 'PP':
                x = 1.473
            else:
                x = 1.641
        elif V_phases <= 15000:
            x = 0.973

    # Se le asigna un valor a la constante Cf
    if V_phases <= 1:
        Cf = 1.5
    else:
        Cf = 1

    # Se calcula la energía incidente
    E = 4.184 * Cf * En * (t / 0.2) * ((610 ** x) / (D ** x))
    E_2t = 4.184 * Cf * En_2t * (t / 0.2) * ((610 ** x) / (D ** x))

    if E > E_2t:
        return (E * 0.238)
    else:
        return (E_2t * 0.238)# se multiplica por este valor para convertir las unidades de Joules a Calorias

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def data_validation(V, F, t, D, G, kind_of_panel, kind_of_arc, kind_of_earth, method):
    """ Esta función se encarga de validar los datos ingresados por el usuario para
    el cálculo de arco eléctrico. En caso de que alguno no sea valido se pondrá un
    error en el HTML en el <input> respectivo.

    """
    validation = 'No error'

    # Se valida que la tensión sea un número entero o de coma flotante
    if not is_number(V):
        validation = 'Error'
        print(V.isdigit())

    # Se valida que la corriente de cortocircuito sea un número entero o de coma flotante
    if not is_number(F):
        validation = 'Error'

    # Se valida que el tiempo sea un número entero o de coma flotante
    if not is_number(t):
        validation = 'Error'

    # Se valida que la distancia sea un número entero o de coma flotante
    if not is_number(D):
        validation = 'Error'

    # Se valida que la separación entre conductores sea un número entero o de coma flotante
    if not is_number(G):
        validation = 'Error'

    if kind_of_panel == 'Tipo de tablero':
        validation = 'Error'

    if kind_of_arc == 'Tipo de arco':
        validation = 'Error'

    if kind_of_earth == 'Conexión a tierra':
        validation = 'Error'

    if method == 'Método de cálculo':
        validation = 'Error'

    return validation

def incident_energy(V, F, t, D, G, kind_of_panel, kind_of_arc, kind_of_earth, method):
    """ Esta función lo que hace es seleccionar el tipo de método con el cual se realizará el cálculo de
    la energía incidente. Se puede aplicar el método de la IEEE 1584 o los demás.
    Los valores que pueden tomar las variables son:

    kind_of_panel = CCM (incluye CCM y tableros), PP (Power Panel, tablero de potencia)
    kind_of_earth = HR (High Resistance), WR (Without Resistance)
    kind_of_arc = O (Opened), C (Closed)
    method = IE15 (IEEE 1584), AU (Automatic)
    G = Separation between conductors (see table D.4.2)

    """

    if method == 'IE15':
        incident_energy = incident_energy_IEEE1584(V, F, G, t, D, kind_of_arc, kind_of_panel, kind_of_earth)
    else:
        if V > 600:
            incident_energy = incident_energy_600_more(V, F, D, t)
        else:
            incident_energy = incident_energy_doughty_neal(F, kind_of_panel, t, kind_of_arc)
    print(incident_energy)
    if incident_energy <= 4:
        epps = 'Cat. 1'
    elif incident_energy <= 8:
        epps = 'Cat. 2'
    elif incident_energy <= 25:
        epps = 'Cat. 3'
    elif incident_energy <= 40:
        epps = 'Cat. 4'

    return incident_energy, epps
