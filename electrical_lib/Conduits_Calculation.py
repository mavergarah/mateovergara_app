    # Definimos las funciones para seleccionar cada uno de los conduits
def emtselecction(A_conduit):
    """ Función para seleccionar el calibre de un conduit tipo EMT.
    Los valores de las áreas de los conduits acá han sido tomados de la tabla
    4 de la NTC 2050 del 2020 (NEC) """
    if A_conduit <= 196:
        return '1/2'
    elif A_conduit <= 343:
        return '3/4'
    elif A_conduit <= 556:
        return '1'
    elif A_conduit <= 968:
        return '1 1/4'
    elif A_conduit <= 1314:
        return '1 1/2'
    elif A_conduit <= 2165:
        return '2'
    elif A_conduit <= 3783:
        return '2 1/2'
    elif A_conduit <= 5701:
        return '3'
    elif A_conduit <= 7451:
        return '3 1/2'
    elif A_conduit <= 9521:
        return '4'
    else:
        return 'no conduit'

def entselecction(A_conduit):
    """ Función para seleccionar el calibre de un conduit tipo ENT """
    if A_conduit <= 184:
        return '1/2'
    elif A_conduit <= 328:
        return '3/4'
    elif A_conduit <= 537:
        return '1'
    elif A_conduit <= 937:
        return '1 1/4'
    elif A_conduit <= 1281:
        return '1 1/2'
    elif A_conduit <= 2123:
        return '2'
    else:
        return 'no conduit'

def fmcselecction(A_conduit):
    """ Función para seleccionar el calibre de un conduit tipo FMC """
    if A_conduit <= 204:
        return '1/2'
    elif A_conduit <= 343:
        return '3/4'
    elif A_conduit <= 527:
        return '1'
    elif A_conduit <= 824:
        return '1 1/4'
    elif A_conduit <= 1201:
        return '1 1/2'
    elif A_conduit <= 2107:
        return '2'
    elif A_conduit <= 3167:
        return '2 1/2'
    elif A_conduit <= 4560:
        return '3'
    elif A_conduit <= 6207:
        return '3 1/2'
    elif A_conduit <= 8107:
        return '4'
    else:
        return 'no conduit'

def imcselecction(A_conduit):
    """ Función para seleccionar el calibre de un conduit tipo IMC """
    if A_conduit <= 222:
        return '1/2'
    elif A_conduit <= 377:
        return '3/4'
    elif A_conduit <= 620:
        return '1'
    elif A_conduit <= 1064:
        return '1 1/4'
    elif A_conduit <= 1432:
        return '1 1/2'
    elif A_conduit <= 2341:
        return '2'
    elif A_conduit <= 3308:
        return '2 1/2'
    elif A_conduit <= 5115:
        return '3'
    elif A_conduit <= 6822:
        return '3 1/2'
    elif A_conduit <= 8725:
        return '4'
    else:
        return 'no conduit'

def pvc80selecction(A_conduit):
    """ Función para seleccionar el calibre de un conduit tipo PVC Schedule 80.
    Los valores de las áreas de los conduits acá han sido tomados de la tabla
    4 de la NTC 2050 del 2020 (NEC) """
    if A_conduit <= 141:
        return '1/2'
    elif A_conduit <= 263:
        return '3/4'
    elif A_conduit <= 445:
        return '1'
    elif A_conduit <= 799:
        return '1 1/4'
    elif A_conduit <= 1104:
        return '1 1/2'
    elif A_conduit <= 1855:
        return '2'
    elif A_conduit <= 2660:
        return '2 1/2'
    elif A_conduit <= 4151:
        return '3'
    elif A_conduit <= 5608:
        return '3 1/2'
    elif A_conduit <= 7268:
        return '4'
    elif A_conduit <= 11518:
        return '5'
    elif A_conduit <= 16513:
        return '6'
    else:
        return 'no conduit'

def pvc40selecction(A_conduit):
    """ Función para seleccionar el calibre de un conduit tipo PVC Schedule 40.
    Los valores de las áreas de los conduits acá han sido tomados de la tabla
    4 de la NTC 2050 del 2020 (NEC) """
    if A_conduit <= 184:
        return '1/2'
    elif A_conduit <= 327:
        return '3/4'
    elif A_conduit <= 535:
        return '1'
    elif A_conduit <= 935:
        return '1 1/4'
    elif A_conduit <= 1282:
        return '1 1/2'
    elif A_conduit <= 2124:
        return '2'
    elif A_conduit <= 3029:
        return '2 1/2'
    elif A_conduit <= 4693:
        return '3'
    elif A_conduit <= 6277:
        return '3 1/2'
    elif A_conduit <= 8091:
        return '4'
    elif A_conduit <= 12748:
        return '5'
    elif A_conduit <= 18433:
        return '6'
    else:
        return 'no conduit'

def pvcAselecction(A_conduit):
    """ Función para seleccionar el calibre de un conduit tipo PVC tipo A.
    Los valores de las áreas de los conduits acá han sido tomados de la tabla
    4 de la NTC 2050 del 2020 (NEC) """
    if A_conduit <= 249:
        return '1/2'
    elif A_conduit <= 419:
        return '3/4'
    elif A_conduit <= 697:
        return '1'
    elif A_conduit <= 1140:
        return '1 1/4'
    elif A_conduit <= 1500:
        return '1 1/2'
    elif A_conduit <= 2350:
        return '2'
    elif A_conduit <= 3515:
        return '2 1/2'
    elif A_conduit <= 5281:
        return '3'
    elif A_conduit <= 6896:
        return '3 1/2'
    elif A_conduit <= 8858:
        return '4'
    else:
        return 'no conduit'

def rmcselecction(A_conduit):
    """ Función para seleccionar el calibre de un conduit tipo RMC """
    if A_conduit <= 204:
        return '1/2'
    elif A_conduit <= 353:
        return '3/4'
    elif A_conduit <= 573:
        return '1'
    elif A_conduit <= 984:
        return '1 1/4'
    elif A_conduit <= 1333:
        return '1 1/2'
    elif A_conduit <= 2198:
        return '2'
    elif A_conduit <= 3137:
        return '2 1/2'
    elif A_conduit <= 4840:
        return '3'
    elif A_conduit <= 6461:
        return '3 1/2'
    elif A_conduit <= 8316:
        return '4'
    else:
        return 'no conduit'

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def data_validation(DA, diameter_or_area, kind_of_conduit):
    """ Esta función se encarga de validar los datos ingresados por el usuario para
    el cálculo de arco eléctrico. En caso de que alguno no sea valido se pondrá un
    error en el HTML en el <input> respectivo.

    """
    validation = 'No error'

    # Se valida que la tensión sea un número entero o de coma flotante
    try:
        DA = DA.split(",")
    except ValueError:
        pass

    print(isinstance(DA,list))

    if isinstance(DA,list):
        for data in DA:
            if not is_number(data):
                validation = 'Error'
                print(validation)
    elif not is_number(DA):
        validation = 'Error'
        print(DA)

    if diameter_or_area == 'DoA':
        validation = 'Error'

    if kind_of_conduit == 'KoC':
        validation = 'Error'

    return validation

def convert2list(list):
    try:
        list = list.split(',')
        float_list = []
        for data in list:
            if is_number(data):
                float_list.append(float(data))
        return float_list
    except ValueError:
        return False

def convert2list_or_value(list_or_value):

    list = convert2list(list_or_value)

    if list == False:
        float_list_or_value = float(list_or_value)
    else:
        float_list_or_value = list

    return float_list_or_value

def conduit_sizing(areas_or_diameters, conduit_type = 'pvc', variable = 'd'):
    """ Esta función calcula en calibre del conduit dependiendo de la cantidad de conductores.
    Para eso se deben ingresar las áreas de los conductores (areas), el tipo de conduit (conduit_type)
    e indicarle al software si estamos ingresando las áreas (a) o los diámetros (d).
    """
    import math

    # Sumar las áreas ingresadas por el usuario

    if isinstance(areas_or_diameters,float):
        percentage_ocuppancy = 0.53

        if variable == 'd':
            areas = math.pi * (areas_or_diameters ** 2) / 4
        else:
            areas = areas_or_diameters
        At_cables = areas
    else:
        # Porcentaje de llenado de los conduits de acuerdo a la NTC 2050
        if (len(areas_or_diameters)) == 2:
            percentage_ocuppancy = 0.31
        else:
            percentage_ocuppancy = 0.40

        areas = []
        # Verificar si el usuario ingresó los diámetros o las áreas
        if variable == 'd':
            for diameter in areas_or_diameters:
                area = math.pi * (diameter ** 2) / 4
                areas.append(area)
        else:
            areas = areas_or_diameters

        At_cables = sum(areas)

    # Calculo del area del área del conduit_type
    A_conduit = At_cables / percentage_ocuppancy
    print(A_conduit)

    # Selección del conduit
    print(conduit_type)
    if conduit_type == 'emt':
        conduit_gauge = emtselecction(A_conduit)
    elif conduit_type == 'ent':
        conduit_gauge = entselecction(A_conduit)
    elif conduit_type == 'fmc':
        conduit_gauge = fmcselecction(A_conduit)
    elif conduit_type == 'imc':
        conduit_gauge = imcselecction(A_conduit)
    elif conduit_type == 'pvc-80':
        conduit_gauge = pvc80selecction(A_conduit)
    elif conduit_type == 'pvc-40':
        conduit_gauge = pvc40selecction(A_conduit)
    elif conduit_type == 'pvc-A':
        conduit_gauge = pvcAselecction(A_conduit)
    elif conduit_type == 'rmc':
        conduit_gauge = rmcselecction(A_conduit)
    else:
        conduit_gauge = 'No conduit gauge'
    return conduit_gauge
