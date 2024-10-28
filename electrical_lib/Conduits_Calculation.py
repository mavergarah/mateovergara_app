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
        return '-'

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
        return '-'

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
        return '-'

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
        return '-'

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
        return '-'

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
        return '-'

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
        return '-'

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
        return '-'

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def data_validation(DA, diameter_or_area, kind_of_conduit):
    """ Esta función se encarga de validar los datos ingresados por el usuario para
    el cálculo del área de conduits. En caso de que alguno no sea valido se pondrá un
    error en el HTML en el <input> respectivo.

    """
    validation = 'No error'

    # Se divide la cadena de texto ingresada por el usuario
    try:
        DA = DA.split(",")
    except ValueError:
        pass

    # Se valida que el usuario haya ingresado una tupla y que cada dato de la tupla
    # sea mayor que cero.
    if isinstance(DA,list):
        for data in DA:
            if not is_number(data):
                validation = 'Error'
            elif float(data) < 0:
                validation = 'Error'
    elif not is_number(DA):
        # Sino se ingresó una tupla se valida que se haya ingresado un número mayor que cero.
        validation = 'Error'
    elif is_number(DA):
        if float(DA) < 0:
            validation = 'Error'

    if diameter_or_area == 'DoA':
        validation = 'Error'

    if kind_of_conduit == 'KoC':
        validation = 'Error'

    return validation

def convert2list(list):
    # Esta función se encarga de convertir la cadena ingresada por el usuario en una lista.
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
    # Esta función se encarga de convertir la cadena ingresada por el usuario en el formulario
    # en una lista o en un valor dependiendo de lo que haya ingresado el usuario.

    list = convert2list(list_or_value)

    if list == False:
        float_list_or_value = float(list_or_value)
    else:
        float_list_or_value = list

    return float_list_or_value

def area_from_gauge(k_ph,phases,k_earth,earth):
    """ Esta función se encarga de seleccionar el área de un conductor de una tabla de un fábricante de cables
    (PROCABLES) dependiendo del tipo de conductor y del calibre (AWG) de cada uno. La función recibe un arreglo
    con los calibres y el tipo de cable tanto de la fase como de la tierra. """

    # Se definen los arreglos que contienen las áreas y los calibres y de cada conductor
    bare_cable_Cu = [2.079,3.302,5.259,8.318,13.21,21.12,33.54,42.62,53.47,67.70,85.04,107.2,126.6,151.8,177.5,202.8,253.1,304.1,354.5,380.1,506.4]
    THHN_THWN2_Cu = [6.61,9.0,14.3,23.8,32.3,52.6,73.1,98.5,116.9,138.9,167.4,201.1,248.8,286.5,326.9,363.1,441.2,539.1,651.4,834.7]
    THHW_CT_Cu = [8.87,11.58,15.55,28.09,46.57,62.49,84.95,122.72,143.14,169.72,201.06,237.79,292.55,651.44,380.13,422.73,506.71,651.44,749.91,951.15]
    RHW2_USE2_Cu = [36.32,46.57,62.21,83.32,120.76,141.03,165.13,196.07,232.35,286.52,330.06,373.25,411.87,490.87,602.63,759.64,962.11]
    No_Halogenuros = [2.69,12.13,16.12,27.90,46.45,61.79,84.30,134.78,158.14,221.93,287.72,370.86,491.27]
    XHHW2 = [28.09,37.28,51.40,71.78,93.31,111.22,132.73,158.37,191.13,243.28,283.53,320.47,359.68,433.74,539.13,688.13,829.58]

    gauge_no_h = ['14 AWG','12 AWG','10 AWG','8 AWG','6 AWG','4 AWG','2 AWG','1/0 AWG','2/0 AWG','4/0 AWG','250 MCM','350 MCM','500 MCM']
    gauge_no_h_2 = ['14AWG','12AWG','10AWG','8AWG','6AWG','4AWG','2AWG','1/0AWG','2/0AWG','4/0AWG','250MCM','350MCM','500MCM']
    gauge_bare_THHN = ['14 AWG','12 AWG','10 AWG','8 AWG','6 AWG','4 AWG','2 AWG','1 AWG','1/0 AWG','2/0 AWG','3/0 AWG','4/0 AWG','250 MCM','300 MCM','350 MCM','400 MCM','500 MCM','600 MCM','700 MCM','750 MCM','1000 MCM']
    gauge_bare_THHN_2 = ['14AWG','12AWG','10AWG','8AWG','6AWG','4AWG','2AWG','1AWG','1/0AWG','2/0AWG','3/0AWG','4/0AWG','250MCM','300MCM','350MCM','400MCM','500MCM','600MCM','700MCM','750MCM','1000MCM']
    gauge_RHW2 = ['8 AWG','6 AWG','4 AWG','2 AWG','1 AWG','1/0 AWG','2/0 AWG','3/0 AWG','4/0 AWG','250 MCM','300 MCM','350 MCM','400 MCM','500 MCM','600 MCM','1000 MCM']
    gauge_RHW2_2 = ['8AWG','6AWG','4AWG','2AWG','1AWG','1/0AWG','2/0AWG','3/0AWG','4/0AWG','250MCM','300MCM','350MCM','400MCM','500MCM','600MCM','1000MCM']
    gauge_XHHW2 = ['8 AWG','6 AWG','4 AWG','2 AWG','1 AWG','1/0 AWG','2/0 AWG','3/0 AWG','4/0 AWG','250 MCM','300 MCM','350 MCM','400 MCM','500 MCM','600 MCM','750 MCM','1000 MCM']
    gauge_XHHW2_2 = ['8AWG','6AWG','4AWG','2AWG','1AWG','1/0AWG','2/0AWG','3/0AWG','4/0AWG','250MCM','300MCM','350MCM','400MCM','500MCM','600MCM','750MCM','1000MCM']

    # Se suman las áreas de los conductores de FASE
    if k_ph == 'THHN_THWN2':
        all_gauges = gauge_bare_THHN
        all_gauges_2 = gauge_bare_THHN_2
        area = THHN_THWN2_Cu
    elif k_ph == 'THHW_CT':
        all_gauges = gauge_bare_THHN
        all_gauges_2 = gauge_bare_THHN_2
        area = THHW_CT_Cu
    elif k_ph == 'RHW2_USE2':
        all_gauges = gauge_RHW2
        all_gauges_2 = gauge_RHW2_2
        area = RHW2_USE2_Cu
    elif k_ph == 'No_Halogenuros':
        all_gauges = gauge_no_h
        all_gauges_2 = gauge_no_h_2
        area = No_Halogenuros
    elif k_ph == 'XHHW2':
        all_gauges = gauge_XHHW2
        all_gauges_2 = gauge_XHHW2_2
        area = XHHW2

    area_phases_1 = sum_array(phases,all_gauges,area)
    print('El area 1 de los conductores es: %f' %area_phases_1)
    area_phases_2 = sum_array(phases,all_gauges_2,area)
    print('El area 2 de los conductores es: %f' %area_phases_2)
    area_phases = area_phases_1 + area_phases_2

    # Se suman las áreas de los conductores de TIERRA
    if k_earth == 'THHN_THWN2':
        all_gauges = gauge_bare_THHN
        all_gauges_2 = gauge_bare_THHN_2
        area = THHN_THWN2_Cu
    elif k_earth == 'bare':
        all_gauges = gauge_bare_THHN
        all_gauges_2 = gauge_bare_THHN_2
        area = bare_cable_Cu
    elif k_earth == 'THHW_CT':
        all_gauges = gauge_bare_THHN
        all_gauges_2 = gauge_bare_THHN_2
        area = THHW_CT_Cu
    elif k_earth == 'RHW2_USE2':
        all_gauges = gauge_RHW2
        all_gauges_2 = gauge_RHW2_2
        area = RHW2_USE2_Cu
    elif k_earth == 'No_Halogenuros':
        all_gauges = gauge_no_h
        all_gauges_2 = gauge_no_h_2
        area = No_Halogenuros
    elif k_earth == 'XHHW2':
        all_gauges = gauge_XHHW2
        all_gauges_2 = gauge_XHHW2_2
        area = XHHW2

    area_earth_1 = sum_array(earth,all_gauges,area)
    print('El area 1 de los conductores es: %f' %area_earth_1)
    area_earth_2 = sum_array(earth,all_gauges_2,area)
    print('El area 2 de los conductores es: %f' %area_earth_2)
    area_earth = area_earth_1 + area_earth_2

    return area_phases + area_earth

def sum_array(values,array_1,array_2):
    """ Esta función realiza la suma de los valores de un arreglo (array 2) a partir de los
    valores que coincidan entre otros dos arreglos (values y array_1). """
    suma_total = 0
    for value in values:
        i = 0
        flag = True
        while flag == True:
            if i == len(array_1):
                value_array2 = '-'
                flag = False
            elif value != array_1[i] and i < len(array_1):
                i = i + 1
                flag = True
            else:
                flag = False
                value_array2 = array_2[i]

        if value_array2 != '-':
            suma_total = suma_total + value_array2
    return suma_total

def conduit_sizing(k_ph, phases, k_earth, earth, areas_or_diameters, conduit_type = 'pvc', variable = 'd'):
    """ Esta función calcula en calibre del conduit dependiendo de la cantidad de conductores.
    Para eso se deben ingresar las áreas de los conductores (areas), el tipo de conduit (conduit_type)
    e indicarle al software si estamos ingresando las áreas (a) o los diámetros (d).
    """
    import math

    # Sumar las áreas ingresadas por el usuario
    if variable == 'd' or variable == 'a':
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
    else:
        At_cables = area_from_gauge(k_ph, phases, k_earth, earth)
        print(At_cables)
        print(phases)
        if len(phases) + len(earth) < 1:
            percentage_ocuppancy = 0.53
        elif (len(phases) + len(earth)) == 2:
            percentage_ocuppancy = 0.31
        else:
            percentage_ocuppancy = 0.4

    # Calculo del area del área del conduit_type
    A_conduit = At_cables / percentage_ocuppancy
    print(A_conduit)

    # Selección del conduit
    print(conduit_type)
    if conduit_type == 'EMT':
        conduit_gauge = emtselecction(A_conduit)
    elif conduit_type == 'ENT':
        conduit_gauge = entselecction(A_conduit)
    elif conduit_type == 'FMC':
        conduit_gauge = fmcselecction(A_conduit)
    elif conduit_type == 'IMC':
        conduit_gauge = imcselecction(A_conduit)
    elif conduit_type == 'PVC-80':
        conduit_gauge = pvc80selecction(A_conduit)
    elif conduit_type == 'PVC-40':
        conduit_gauge = pvc40selecction(A_conduit)
    elif conduit_type == 'PVC-A':
        conduit_gauge = pvcAselecction(A_conduit)
    elif conduit_type == 'RMC':
        conduit_gauge = rmcselecction(A_conduit)
    else:
        conduit_gauge = '-'
    return conduit_gauge
