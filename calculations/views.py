from django.shortcuts import render
from django.http import HttpResponse

# import calculations (own library)
from electrical_lib import Cable_Calculations
from electrical_lib import Arc_Flash_Calculation
from electrical_lib import Conduits_Calculation
from electrical_lib import Safety_Calculations
from .models import AboutApp

# Create your views here.
def cable_choosing(request):
    # En esta vista el usuario selecciona el tipo de cálculo que quiere hacer:
    # Un cálculo para una carga general (un toma, iluminación, etc.)
    # Un motor para el cual tiene la potencia, la eficiencia, el factor de potencia y la tensión
    # O un motor del que solo tiene la tensión y la potencia. En este caso se selcciona de acuerdo
    # a la sección 430 de la NTC 2050 del 2020.
    return render(request, 'calculations/cable_choosing.html')

def cable_choosing_result(request):
    # Dependiendo del tipo de selección que haya hecho el usuario en la vista anterior se realiza
    # la redirección al formulario correspondiente.

    # 1. Se valida la selección del usuario
    validation = Cable_Calculations.is_choice(request.POST['ca_calculate_choosing'],'carga')

    if validation:
        select = request.POST['ca_calculate_choosing']

        if select == 'CV':
            return render(request, 'calculations/cable_calculations.html')
        elif select == 'M':
            return render(request, 'calculations/cable_motor_calculations.html')
        else:
            return render(request, 'calculations/cable_motorntc_calculations.html')
    else:
        return render(request, 'calculations/cable_choosing.html',{'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def cable_calculation(request):
    # Aquí se carga el formulario correspondiente a el cálculo de conductores eléctricos para
    # cargas generales.
    if request.method != 'POST':
        return render(request, 'calculations/cable_calculations.html')
    else:
        # Validar los datos de ingreso al formulario del HTML
        P = Cable_Calculations.is_number(request.POST['ca_potencia'])
        U = Cable_Calculations.is_choice(request.POST['ca_unidades'],'unidades')
        Ph = Cable_Calculations.is_choice(request.POST['ca_fases'],'fases')
        FP2 = Cable_Calculations.isin_range(request.POST['ca_fp'],0,1) # Se valida que el factor de potencia esté entre 0 y 1
        FP = Cable_Calculations.is_number(request.POST['ca_fp'])
        V = Cable_Calculations.is_number(request.POST['ca_tension'])
        V2 = Cable_Calculations.is_positive(request.POST['ca_tension']) # Se valida que la tensión sea mayor que cero
        L = Cable_Calculations.is_number(request.POST['ca_longitud'])
        L2 = Cable_Calculations.is_positive(request.POST['ca_longitud']) # Se valida que la longitud sea mayor que cero
        T_amb = Cable_Calculations.is_number(request.POST['ca_temperature'])
        T_cond = Cable_Calculations.is_choice(request.POST['ca_temp-conductor'],'temperatura')
        CL = Cable_Calculations.is_choice(request.POST['ca_carga_continua'],'carga continua')
        K = Cable_Calculations.is_choice(request.POST['ca_material'],'material')
        NC = Cable_Calculations.is_number(request.POST['ca_numero-conductores'])
        C = Cable_Calculations.is_choice(request.POST['ca_conduit'],'conduit')

        # Realizar cálculo de los conductores si el formulario no tiene errores
        if P and U and Ph and FP and FP2 and V and V2 and L and L2 and T_amb and T_cond and CL and K and NC and C:
            P = float(request.POST['ca_potencia'])
            U = request.POST['ca_unidades']
            Ph = float(request.POST['ca_fases'])
            FP = float(request.POST['ca_fp'])
            V = float(request.POST['ca_tension'])
            L = float(request.POST['ca_longitud'])
            T_amb = float(request.POST['ca_temperature'])
            T_cond = float(request.POST['ca_temp-conductor'])
            CL = request.POST['ca_carga_continua']
            K = request.POST['ca_material']
            NC = float(request.POST['ca_numero-conductores'])
            C = request.POST['ca_conduit']

            ph, n, g, V_drop, pd, fa_corr, ad_corr, nf = Cable_Calculations.cable_calculation(P, U,
            Ph, FP, V, L, T_cond, T_amb, CL, K, NC, C)
            return render(request, 'calculations/cable_calculations.html', {'phase':ph,
            'neutral':n,'ground':g, 'Vdrop':round(V_drop,2),
            'protective':pd, 'corrective_factor':fa_corr,'Pot':P,'Un':U,'Volts':V,
            'conductors_per_fase':nf, 'numb_phases':Ph, 'adjust_factor':ad_corr})
        else:
            return render(request, 'calculations/cable_calculations.html',
            {'error':'El formulario contiene errores'})

def cable_motor(request):
    # Esta función realiza el cálculo de conductores para un motor del cual se conocen
    # la eficiencia y el factor de potencia.

    if request.method != 'POST':
        return render(request, 'calculations/cable_motor_calculations.html')
    else:
        # Validar los datos de ingreso al formulario del HTML2
        P = Cable_Calculations.is_number(request.POST['mo_power'])
        n = Cable_Calculations.is_number(request.POST['mo_efficiency'])
        n2 = Cable_Calculations.isin_range(request.POST['mo_efficiency'],0.01,1) # Validación de eficiencia entre 0 y 1
        Ph = Cable_Calculations.is_choice(request.POST['mo_fases'],'fases')
        FP = Cable_Calculations.is_number(request.POST['mo_fp'])
        FP2 = Cable_Calculations.isin_range(request.POST['mo_fp'],0.01,1) # Validación de factor de potencia entre 0 y 1
        V = Cable_Calculations.is_number(request.POST['mo_tension'])
        V2 = Cable_Calculations.is_positive(request.POST['mo_tension']) # Validación de que la tensión es mayor a cero
        L = Cable_Calculations.is_number(request.POST['mo_longitud'])
        L2 = Cable_Calculations.is_positive(request.POST['mo_longitud']) # Validación de que la longitud es mayor a cero
        T_amb = Cable_Calculations.is_number(request.POST['mo_temperature'])
        T_cond = Cable_Calculations.is_choice(request.POST['mo_temp-conductor'],'temperatura')
        CL = Cable_Calculations.is_choice(request.POST['mo_carga_continua'],'carga continua')
        K = Cable_Calculations.is_choice(request.POST['mo_material'],'material')
        NC = Cable_Calculations.is_number(request.POST['mo_numero-conductores'])
        C = Cable_Calculations.is_choice(request.POST['mo_conduit'],'conduit')

        # Realizar cálculo de los conductores si el formulario no tiene errores
        if P and n and n2 and Ph and FP and FP2 and V and V2 and L and L2 and T_amb and T_cond and CL and K and NC and C:
            P = float(request.POST['mo_power'])
            n = float(request.POST['mo_efficiency'])
            Ph = float(request.POST['mo_fases'])
            FP = float(request.POST['mo_fp'])
            V = float(request.POST['mo_tension'])
            L = float(request.POST['mo_longitud'])
            T_amb = float(request.POST['mo_temperature'])
            T_cond = float(request.POST['mo_temp-conductor'])
            CL = request.POST['mo_carga_continua']
            K = request.POST['mo_material']
            NC = float(request.POST['mo_numero-conductores'])
            C = request.POST['mo_conduit']

            ph, n, g, V_drop, pd, fa_corr, ad_corr, nf = Cable_Calculations.cable_calculation(P,
            'HP', Ph, FP, V, L, T_cond, T_amb, CL, K, NC, C, n)
            return render(request, 'calculations/cable_motor_calculations.html', {'phase':ph,
            'neutral':n,'ground':g, 'Vdrop':round(V_drop,2),
            'protective':pd, 'corrective_factor':fa_corr, 'conductors_per_fase':nf,
            'numb_phases':Ph, 'adjust_factor':ad_corr,'Pot':P,'Un':'HP','Volts':V})
        else:
            return render(request, 'calculations/cable_motor_calculations.html',
            {'error':'El formulario contiene errores'})

def cable_motorntc(request):
    # Esta función realiza el cálculo de conductores para un motor del cual se conocen
    # la eficiencia y el factor de potencia.

    if request.method != 'POST':
        return render(request, 'calculations/cable_motorntc_calculations.html')
    else:
        # Validar los datos de ingreso al formulario del HTML
        print(request.POST)
        P = Cable_Calculations.is_choice(request.POST['mon_power'],'potencia')
        Ph = Cable_Calculations.is_choice(request.POST['mon_fases'],'fases')
        S = Cable_Calculations.is_choice(request.POST['mon_sinchronous'],'sincrono')
        V = Cable_Calculations.is_choice(request.POST['mon_voltage'],'tension')
        L = Cable_Calculations.is_number(request.POST['mon_longitud'])
        T_amb = Cable_Calculations.is_number(request.POST['mon_temperature'])
        T_cond = Cable_Calculations.is_choice(request.POST['mon_temp-conductor'],'temperatura')
        CL = Cable_Calculations.is_choice(request.POST['mon_carga_continua'],'carga continua')
        K = Cable_Calculations.is_choice(request.POST['mon_material'],'material')
        NC = Cable_Calculations.is_number(request.POST['mon_numero-conductores'])
        C = Cable_Calculations.is_choice(request.POST['mon_conduit'],'conduit')

        # Validar que los valores de potencia ingresados enten dentro del rango de tensión de la NTC 2050
        if P and V and Ph:
            # Averiguar si el sistema es monofásico, bifásico o trifásico
            if float(request.POST['mon_fases']) == 1:
                min = 1/6
                max = 10
            elif float(request.POST['mon_fases']) == 2:
                # Preguntar por el nivel de tensión
                min = 1/2
                if (float(request.POST['mon_voltage'])) == 115:
                    max = 2
                else:
                    max = 200
            else:
                # Preguntar si el motor es síncrono o asíncrono
                if request.POST['mon_sinchronous'] == 'NTC2050-As':
                    # Preguntar por el nivel de tensión
                    min = 1/2
                    if (float(request.POST['mon_voltage'])) == 115:
                        max = 2
                    elif float(request.POST['mon_voltage']) == 200 or float(request.POST['mon_voltage']) == 208 or (float(request.POST['mon_voltage'])) == 230:
                        max = 200
                    elif float(request.POST['mon_voltage']) == 460 or float(request.POST['mon_voltage']) == 575:
                        max = 500
                    else:
                        min = 60
                        max = 500
                else:
                    # Preguntar por el nivel de tensión
                    min = 25
                    if (float(request.POST['mon_voltage'])) == 230:
                        max = 200
                    elif float(request.POST['mon_voltage']) == 460 or float(request.POST['mon_voltage']) == 575:
                        max = 200
                    else:
                        min = 60
                        max = 200

        # Validar si el valor de potencia ingresado se encuentra dentro del rango de min y max de la sección 430
        P2 = Cable_Calculations.isin_range(request.POST['mon_power'],min,max)

        # Realizar cálculo de los conductores si el formulario no tiene errores
        if P and P2 and Ph and S and V and L and T_amb and T_cond and CL and K and NC and C:
            P = float(request.POST['mon_power'])
            Ph = float(request.POST['mon_fases'])
            S = request.POST['mon_sinchronous']
            V = float(request.POST['mon_voltage'])
            L = float(request.POST['mon_longitud'])
            T_amb = float(request.POST['mon_temperature'])
            T_cond = float(request.POST['mon_temp-conductor'])
            CL = request.POST['mon_carga_continua']
            K = request.POST['mon_material']
            NC = float(request.POST['mon_numero-conductores'])
            C = request.POST['mon_conduit']

            ph, n, g, V_drop, pd, fa_corr, ad_corr, nf = Cable_Calculations.cable_calculation(P, 'HP',
            Ph, 0.85, V, L, T_cond, T_amb, CL, K, NC, C, S)
            return render(request, 'calculations/cable_motorntc_calculations.html',
            {'phase':ph, 'neutral':n,'ground':g,'Vdrop':round(V_drop,2), 'protective':pd,
            'corrective_factor':fa_corr,'conductors_per_fase':nf, 'numb_phases':Ph,
            'Pot':P,'Un':'HP','Volts':V,'adjust_factor':ad_corr})
        else:
            return render(request, 'calculations/cable_motorntc_calculations.html',
            {'error':'El formulario contiene errores'})

def cable_result(request):
    # Esta función realiza el cálculo de conductores para una carga general (que no es un motor)
    # Validar los datos de ingreso al formulario del HTML
    P = Cable_Calculations.is_number(request.POST['ca_potencia'])
    U = Cable_Calculations.is_choice(request.POST['ca_unidades'],'unidades')
    Ph = Cable_Calculations.is_choice(request.POST['ca_fases'],'fases')
    FP2 = Cable_Calculations.isin_range(request.POST['ca_fp'],0,1) # Se valida que el factor de potencia esté entre 0 y 1
    FP = Cable_Calculations.is_number(request.POST['ca_fp'])
    V = Cable_Calculations.is_number(request.POST['ca_tension'])
    V2 = Cable_Calculations.is_positive(request.POST['ca_tension']) # Se valida que la tensión sea mayor que cero
    L = Cable_Calculations.is_number(request.POST['ca_longitud'])
    L2 = Cable_Calculations.is_positive(request.POST['ca_longitud']) # Se valida que la longitud sea mayor que cero
    T_amb = Cable_Calculations.is_number(request.POST['ca_temperature'])
    T_cond = Cable_Calculations.is_choice(request.POST['ca_temp-conductor'],'temperatura')
    CL = Cable_Calculations.is_choice(request.POST['ca_carga_continua'],'carga continua')
    K = Cable_Calculations.is_choice(request.POST['ca_material'],'material')
    NC = Cable_Calculations.is_number(request.POST['ca_numero-conductores'])
    C = Cable_Calculations.is_choice(request.POST['ca_conduit'],'conduit')

    # Realizar cálculo de los conductores si el formulario no tiene errores
    if P and U and Ph and FP and FP2 and V and V2 and L and L2 and T_amb and T_cond and CL and K and NC and C:
        P = float(request.POST['ca_potencia'])
        U = request.POST['ca_unidades']
        Ph = float(request.POST['ca_fases'])
        FP = float(request.POST['ca_fp'])
        V = float(request.POST['ca_tension'])
        L = float(request.POST['ca_longitud'])
        T_amb = float(request.POST['ca_temperature'])
        T_cond = float(request.POST['ca_temp-conductor'])
        CL = request.POST['ca_carga_continua']
        K = request.POST['ca_material']
        NC = float(request.POST['ca_numero-conductores'])
        C = request.POST['ca_conduit']

        ph, n, g, V_drop, pd, fa_corr, ad_corr, nf = Cable_Calculations.cable_calculation(P, U, Ph, FP, V, L, T_cond, T_amb, CL, K, NC, C)
        return render(request, 'calculations/cable_result.html', {'phase':ph,
        'neutral':n,'ground':g, 'Vdrop':round(V_drop,2),
        'protective':pd, 'corrective_factor':fa_corr,
        'conductors_per_fase':nf, 'numb_phases':Ph, 'adjust_factor':ad_corr})
    else:
        return render(request, 'calculations/cable_calculations.html', {'error':'El formulario contiene errores'})

def drop_voltage(request):
    # En esta parte del código se carga el formulario correspondiente al cálculo de caída de
    # tensión.

    if request.method != 'POST':
        return render(request, 'calculations/drop_voltage.html')
    else:
        # Validar datos de ingreso del usuario. Las funciones retornan True or False
        V = Cable_Calculations.is_number(request.POST['dro_voltage'])
        V2 = Cable_Calculations.is_positive(request.POST['dro_voltage']) # Se valida que la caída de tensión sea mayor que cero
        L = Cable_Calculations.is_number(request.POST['dro_length'])
        L2 = Cable_Calculations.is_positive(request.POST['dro_length'])
        I = Cable_Calculations.is_number(request.POST['dro_current'])
        FP = Cable_Calculations.is_number(request.POST['dro_pf'])
        Ph = Cable_Calculations.is_choice(request.POST['dro_system'],'sistema')
        gauge = Cable_Calculations.is_choice(request.POST['dro_cable_gauge'],'calibre')
        KC = Cable_Calculations.is_choice(request.POST['dro_cable_kind'],'material')
        K = Cable_Calculations.is_choice(request.POST['dro_conduit_kind'],'conduit')

        # Validrar que para conductores de aluminio no se pueda seleccionar el calibre #14AWG no se pueda seleccionar
        if request.POST['dro_cable_kind'] == 'Al' and request.POST['dro_cable_gauge'] == '14 AWG':
            gauge2 = False
        else:
            gauge2 = True

        if (V and V2 and L and L2 and I and FP and Ph and gauge and gauge2 and KC and K):
            # Capturar los datos del formulario HTML para realizar el cálculo
            V = float(request.POST['dro_voltage'])
            L = float(request.POST['dro_length'])
            I = float(request.POST['dro_current'])
            FP = float(request.POST['dro_pf'])
            Ph = float(request.POST['dro_system'])
            gauge = request.POST['dro_cable_gauge']
            KC = request.POST['dro_conduit_kind']
            K = request.POST['dro_cable_kind']

            VDrop, VDrop100, R, X = Cable_Calculations.drop_voltage_calculation(Ph, V, L, I, FP, gauge, KC, K)
            print('R= %f y X= %f' %(R,X))
            return render(request, 'calculations/drop_voltage.html',{'drop_voltage':round(VDrop,2),
            'drop_voltage_percentage':round(VDrop100,2),'resistance':R,'reactance':X,'length':L,
            'volts':V,'gauge':gauge})
        else:
            return render(request, 'calculations/drop_voltage.html',
            {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def drop_voltage_result(request):
    # Esta función se encarga de realizar el cálculo de la caída de tensión para una carga
    # ingresada por un usuario.

    # Validar datos de ingreso del usuario. Las funciones retornan True or False
    V = Cable_Calculations.is_number(request.POST['dro_voltage'])
    V2 = Cable_Calculations.is_positive(request.POST['dro_voltage']) # Se valida que la caída de tensión sea mayor que cero
    L = Cable_Calculations.is_number(request.POST['dro_length'])
    L2 = Cable_Calculations.is_positive(request.POST['dro_length'])
    I = Cable_Calculations.is_number(request.POST['dro_current'])
    FP = Cable_Calculations.is_number(request.POST['dro_pf'])
    Ph = Cable_Calculations.is_choice(request.POST['dro_system'],'sistema')
    gauge = Cable_Calculations.is_choice(request.POST['dro_cable_gauge'],'calibre')
    KC = Cable_Calculations.is_choice(request.POST['dro_cable_kind'],'material')
    K = Cable_Calculations.is_choice(request.POST['dro_conduit_kind'],'conduit')

    # Validrar que para conductores de aluminio no se pueda seleccionar el calibre #14AWG no se pueda seleccionar
    if request.POST['dro_cable_kind'] == 'Al' and request.POST['dro_cable_gauge'] == '14 AWG':
        gauge2 = False
    else:
        gauge2 = True

    if (V and V2 and L and L2 and I and FP and Ph and gauge and gauge2 and KC and K):
        # Capturar los datos del formulario HTML para realizar el cálculo
        V = float(request.POST['dro_voltage'])
        L = float(request.POST['dro_length'])
        I = float(request.POST['dro_current'])
        FP = float(request.POST['dro_pf'])
        Ph = float(request.POST['dro_system'])
        gauge = request.POST['dro_cable_gauge']
        KC = request.POST['dro_conduit_kind']
        K = request.POST['dro_cable_kind']

        VDrop, VDrop100, R, X = Cable_Calculations.drop_voltage_calculation(Ph, V, L, I, FP, gauge, KC, K)
        print('R= %f y X= %f' %(R,X))
        return render(request, 'calculations/drop_voltage_result.html',{'drop_voltage':round(VDrop,2),
        'drop_voltage_percentage':round(VDrop100,2), 'resistance':R, 'reactance':X})
    else:
        return render(request, 'calculations/drop_voltage.html',{'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def protective_device(request):
    # Esta vista carga el formulario que permite seleccionar un dispositivo de protección a partir de
    # la corriente continua y de la corriente ajustada.
    if request.method != 'POST':
        return render(request, 'calculations/protective_device.html')
    else:
        # Validar los datos de ingreso al formulario del HTML
        I_ad = Cable_Calculations.is_number(request.POST['pro_current_ad'])
        I_cont = Cable_Calculations.is_number(request.POST['pro_current_cont'])
        print(I_ad, I_cont)

        # Realizar cálculo de conduits si el formulario no tiene errores
        if I_ad and I_cont:
            I_ad = float(request.POST['pro_current_ad']) # Variable de corriente ajustada
            I_cont = float(request.POST['pro_current_cont']) # Variable de corriente continua

            protective = Cable_Calculations.protective_device(I_ad, I_cont)
            print(protective)
            return render(request, 'calculations/protective_device.html', {'I_continuous':I_cont,
            'I_adjust':I_ad,'protective_device':protective})
        else:
            return render(request, 'calculations/protective_device.html',
            {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def protective_result(request):
    # Con esta función se realiza la selección del dispositivo de protección basado en la corriente
    # continua y en la corriente ajustada.

    # Validar los datos de ingreso al formulario del HTML
    I_ad = Cable_Calculations.is_number(request.POST['pro_current_ad'])
    I_cont = Cable_Calculations.is_number(request.POST['pro_current_cont'])
    print(I_ad, I_cont)

    # Realizar cálculo de conduits si el formulario no tiene errores
    if I_ad and I_cont:
        I_ad = float(request.POST['pro_current_ad']) # Variable de corriente ajustada
        I_cont = float(request.POST['pro_current_cont']) # Variable de corriente continua

        protective = Cable_Calculations.protective_device(I_ad, I_cont)
        print(protective)
        return render(request, 'calculations/protective_result.html', {'column_1':'-','column_2':'Corriente Contina (A)',
        'column_3':'Corriente Ajustada (A)','gauge':'-','material':I_cont,'temperature':I_ad,
        'protective_device':protective})
    else:
        return render(request, 'calculations/protective_device.html',
        {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def protective_choosing(request):
    # Esta función carga el formulario de ingreso de datos para que el usuario
    # seleccione el tipo de cálculo que quiere realizar.
    return render(request, 'calculations/protective_choosing.html')

def protective_choosing_result(request):
    # Dependiendo del tipo de selección que haya hecho el usuario en la vista anterior se realiza
    # la redirección al formulario correspondiente.

    # 1. Se valida la selección del usuario
    validation = Cable_Calculations.is_choice(request.POST['pro_calculate_choosing'],'proteccion')

    if validation:
        select = request.POST['pro_calculate_choosing']

        if select == 'C':
            return render(request, 'calculations/protective_device.html')
        else:
            return render(request, 'calculations/protective_device_gauge.html')
    else:
        return render(request, 'calculations/protective_choosing.html',{'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def protective_device_gauge(request):
    # Esta vista carga el formulario que permite seleccionar un dispositivo de protección a partir del
    # calibre del conductor.
    if request.method != 'POST':
        return render(request, 'calculations/protective_device_gauge.html')
    else:
        # Validar los datos de ingreso al formulario del HTML
        gauge = Cable_Calculations.is_choice(request.POST['pro_gauge'],'calibre')
        material = Cable_Calculations.is_choice(request.POST['pro_material'],'material')
        temperature = Cable_Calculations.is_choice(request.POST['pro_temperature'],'temperatura')

        # Realizar cálculo de conduits si el formulario no tiene errores
        if gauge and material and temperature:
            gauge = request.POST['pro_gauge'] # Variable del calibre del conductor
            material = request.POST['pro_material'] # Variable del material del conductor
            temperature = request.POST['pro_temperature'] # Variable de la temperatura del conductor
            print(gauge, material, temperature)

            protective = Cable_Calculations.protective_device_gauge(material, temperature, gauge)
            print(protective)
            return render(request, 'calculations/protective_device_gauge.html', {'protective_device':protective,
            'gauge':gauge,'material':material,'temperature':temperature})
        else:
            return render(request, 'calculations/protective_device_gauge.html',
            {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def protective_gauge_result(request):
    # Con esta función se realiza la selección del dispositivo de protección basado en la corriente
    # continua y en la corriente ajustada.

    # Validar los datos de ingreso al formulario del HTML
    gauge = Cable_Calculations.is_choice(request.POST['pro_gauge'],'calibre')
    material = Cable_Calculations.is_choice(request.POST['pro_material'],'material')
    temperature = Cable_Calculations.is_choice(request.POST['pro_temperature'],'temperatura')

    # Realizar cálculo de conduits si el formulario no tiene errores
    if gauge and material and temperature:
        gauge = request.POST['pro_gauge'] # Variable del calibre del conductor
        material = request.POST['pro_material'] # Variable del material del conductor
        temperature = request.POST['pro_temperature'] # Variable de la temperatura del conductor
        print(gauge, material, temperature)

        protective = Cable_Calculations.protective_device_gauge(material, temperature, gauge)
        print(protective)
        return render(request, 'calculations/protective_result.html', {'column_1':'Calibre','column_2':'Material',
        'column_3':'Temperatura ºC','protective_device':protective,'gauge':gauge,'material':material,
        'temperature':temperature})
    else:
        return render(request, 'calculations/protective_device.html',
        {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def grounding_cable(request):
    # En esta vista se carga el formulario de selección del conductor de puesta a tierra
    # de equipos.
    if request.method != 'POST':
        return render(request, 'calculations/grounding_cable.html')
    else:
        # Validar los datos ingresados por el usuario
        Protective = Cable_Calculations.is_number(request.POST['gro_protective'])
        Material = Cable_Calculations.is_choice(request.POST['gro_material'],'material')

        if Protective and Material:
            # Obtener los valores ingresados por el usuario en el formulario HTML
            Protective = float(request.POST['gro_protective'])
            Material = request.POST['gro_material']

            # Realizar la selección del conductor de puesta a tierra
            grounding_cable = Cable_Calculations.earth_conductor(Protective, Material)

            return render(request, 'calculations/grounding_cable.html',{'protective':Protective,
            'gauge':grounding_cable,'material':Material})
        else:
            return render(request, 'calculations/grounding_cable.html',{'error':'El formulario contiene errores.'})

def grounding_result(request):
    # Con esta función se realiza la selección del conductor de puesta a tierra de equipos basado
    # en el dispositivo de protección que ingrese el usuario.

    # Validar los datos ingresados por el usuario
    Protective = Cable_Calculations.is_number(request.POST['gro_protective'])
    Material = Cable_Calculations.is_choice(request.POST['gro_material'],'material')

    if Protective and Material:
        # Obtener los valores ingresados por el usuario en el formulario HTML
        Protective = float(request.POST['gro_protective'])
        Material = request.POST['gro_material']

        # Realizar la selección del conductor de puesta a tierra
        grounding_cable = Cable_Calculations.earth_conductor(Protective, Material)

        return render(request, 'calculations/grounding_result.html',{'protective':Protective,
        'gauge':grounding_cable,'material':Material})
    else:
        return render(request, 'calculations/grounding_cable.html',{'error':'El formulario contiene errores.'})

def electrode_cable(request):
    # Esta vista carga el formulario de ingreso de datos para que a partir del conductor
    # de fase el usuario pueda seleccionar el conductor del electrodo de puesta a tierra.
    if request.method != 'POST':
        return render(request, 'calculations/electrode_cable.html')
    else:
        # Validar los datos ingresados por el usuario
        gauge = Cable_Calculations.is_choice(request.POST['ele_cable_gauge'], 'calibre')
        material = Cable_Calculations.is_choice(request.POST['ele_material'], 'material')

        if gauge and material:
            # Obtener los valores ingresados por el usuario en el formulario HTML
            gauge = request.POST['ele_cable_gauge']
            material = request.POST['ele_material']

            # Realizar la selección del conductor de puesta a tierra
            electrode_cu, electrode_al = Cable_Calculations.electrode_conductor(gauge, material)

            return render(request, 'calculations/electrode_cable.html',{'ele_cu':electrode_cu,
            'ele_al':electrode_al,'material':material, 'gauge':gauge})
        else:
            return render(request, 'calculations/electrode_cable.html',{'error':'El formulario contiene errores.'})

def electrode_result(request):
    # Aquí en esta parte del código se realiza la selección del conductor del electrodo de puesta
    # a tierra.

    # Validar los datos ingresados por el usuario
    gauge = Cable_Calculations.is_choice(request.POST['ele_cable_gauge'], 'calibre')
    material = Cable_Calculations.is_choice(request.POST['ele_material'], 'material')

    if gauge and material:
        # Obtener los valores ingresados por el usuario en el formulario HTML
        gauge = request.POST['ele_cable_gauge']
        material = request.POST['ele_material']

        # Realizar la selección del conductor de puesta a tierra
        electrode_cu, electrode_al = Cable_Calculations.electrode_conductor(gauge, material)

        return render(request, 'calculations/electrode_result.html',{'ele_cu':electrode_cu,
        'ele_al':electrode_al,'material':material, 'gauge':gauge})
    else:
        return render(request, 'calculations/electrode_cable.html',{'error':'El formulario contiene errores.'})

def conduit_choosing(request):
    # Esta función carga el formulario de ingreso de datos para que el usuario
    # seleccione el tipo de cálculo que quiere realizar.
    return render(request, 'calculations/conduit_choosing.html')

def conduit_choosing_result(request):
    # Dependiendo del tipo de selección que haya hecho el usuario en la vista anterior se realiza
    # la redirección al formulario correspondiente.

    # 1. Se valida la selección del usuario
    validation = Cable_Calculations.is_choice(request.POST['co_calculate_choosing'],'conduit')

    if validation:
        select = request.POST['co_calculate_choosing']

        if select == 'DoA':
            return render(request, 'calculations/conduits_calculation.html')
        else:
            return render(request, 'calculations/conduits_calculation_gauge.html')
    else:
        return render(request, 'calculations/conduit_choosing.html',{'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def conduit_calculation(request):
    # Esta función carga el formulario de ingreso de datos para que el usuario
    # ingrese bien sea los diámetros o las áreas de cada uno de los conductores.
    if request.method != 'POST':
        return render(request, 'calculations/conduits_calculation.html')
    else:
        # Validar los datos de ingreso al formulario del HTML
        validation = Conduits_Calculation.data_validation(request.POST['co_ingreso'],
        request.POST['co_diametro'], request.POST['co_conduit_kind'])

        # Realizar cálculo de conduits si el formulario no tiene errores
        if not validation == 'Error':
            DoA = Conduits_Calculation.convert2list_or_value(request.POST['co_ingreso']) # Variable de Diámetro o Área

            SDA = request.POST['co_diametro'] # Variable de selección de diámetro o área
            CK = request.POST['co_conduit_kind'] # Tipo de tubería
            conduit = Conduits_Calculation.conduit_sizing('','','','',DoA,CK,SDA)
            if SDA == 'd':
                title_1 = 'Diámetros (mm) Ingresados'
            else:
                title_1 = 'Áreas (mm2) Ingresadas'
            return render(request, 'calculations/conduits_calculation.html',
            {'kind_of_conduit':CK, 'conduit':conduit,'areameters':DoA,'title_1':title_1})
        else:
            return render(request, 'calculations/conduits_calculation.html',
            {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def conduit_gauge_result(request):
    # Una vez que el usuario ha realizado el ingreso de los datos de los calibres
    # se realiza el cálculo de los conduits.

    # Validar los datos de ingreso al formulario del HTML
    k_phases = Cable_Calculations.is_choice(request.POST['co_phainsulation'],'insulation')
    k_earth = Cable_Calculations.is_choice(request.POST['co_earinsulation'],'insulation')
    k_conduit = Cable_Calculations.is_choice(request.POST['co_conduit_kind'],'KoC')

    # Realizar cálculo de conduits si el formulario no tiene errores
    if k_phases and k_earth:
        phases = request.POST['co_phainput'].split(',') # Arreglo de fases
        earth = request.POST['co_earinput'].split(',') # Variable de tierras

        k_phases = request.POST['co_phainsulation'] # Variable de selección de aislamiento de fases
        k_earth = request.POST['co_earinsulation'] # Variable de selección de aislamiento de tierra
        k_conduit = request.POST['co_conduit_kind'] # Variable de selección de tipo de tubería

        conduit = Conduits_Calculation.conduit_sizing(k_phases, phases, k_earth, earth,'',k_conduit,'g')
        print(conduit)
        return render(request, 'calculations/conduits_result.html',
        {'kind_of_conduit':k_conduit, 'conduit':conduit})
    else:
        return render(request, 'calculations/conduits_calculation_gauge.html',
        {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def conduit_result(request):
    # Una vez que el usuario ha realizado el ingreso de los datos de los diámetros o de las
    # áreas se realiza el cálculo de los conduits.

    # Validar los datos de ingreso al formulario del HTML
    validation = Conduits_Calculation.data_validation(request.POST['co_ingreso'],
    request.POST['co_diametro'], request.POST['co_conduit_kind'])

    # Realizar cálculo de conduits si el formulario no tiene errores
    if not validation == 'Error':
        DoA = Conduits_Calculation.convert2list_or_value(request.POST['co_ingreso']) # Variable de Diámetro o Área

        SDA = request.POST['co_diametro'] # Variable de selección de diámetro o área
        CK = request.POST['co_conduit_kind'] # Tipo de tubería
        conduit = Conduits_Calculation.conduit_sizing('','','','',DoA,CK,SDA)
        return render(request, 'calculations/conduits_result.html', {'kind_of_conduit':CK, 'conduit':conduit})
    else:
        return render(request, 'calculations/conduits_calculation.html', {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def conduit_gauge_calculation(request):
    # Esta vista carga el formulario en el que se pueden ingresar los calibres
    # para realizar el cálculo de los conduits.

    if request.method != 'POST':
        return render(request,'calculations/conduits_calculation_gauge.html')
    else:
        # Validar los datos de ingreso al formulario del HTML
        k_phases = Cable_Calculations.is_choice(request.POST['co_phainsulation'],'insulation')
        k_earth = Cable_Calculations.is_choice(request.POST['co_earinsulation'],'insulation')
        k_conduit = Cable_Calculations.is_choice(request.POST['co_conduit_kind'],'KoC')

        # Realizar cálculo de conduits si el formulario no tiene errores
        if k_phases and k_earth:
            phases = request.POST['co_phainput'].split(',') # Arreglo de fases
            earth = request.POST['co_earinput'].split(',') # Variable de tierras

            k_phases = request.POST['co_phainsulation'] # Variable de selección de aislamiento de fases
            k_earth = request.POST['co_earinsulation'] # Variable de selección de aislamiento de tierra
            k_conduit = request.POST['co_conduit_kind'] # Variable de selección de tipo de tubería

            conduit = Conduits_Calculation.conduit_sizing(k_phases, phases, k_earth, earth,'',k_conduit,'g')
            print(conduit)
            return render(request, 'calculations/conduits_calculation_gauge.html',
            {'kind_of_conduit':k_conduit,'conduit':conduit, 'gauges':(phases,earth)})
        else:
            return render(request, 'calculations/conduits_calculation_gauge.html',
            {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def conduit_cable_table(request):
    # Esta función se encarga de mostrarle al usuario una tabla con los diámetros y las áreas de
    # los calibres comerciales de los conductores eléctricos.
    return render(request, 'calculations/conduits_cable_table.html')

def work_clearances_calculation(request):
    # En esta vista se carga el formulario que le permite al usuario ingresar los datos correspondientes
    # al ancho, anto y condición en la que se encuentra el tablero para realizar el cálculo del
    # espacio de trabajo.
    if request.method != 'POST':
        return render(request, 'calculations/workclearances_calculations.html')
    else:
        # Validar los datos de ingreso al formulario del HTML
        V = Safety_Calculations.is_number(request.POST['wc_voltage'])
        V2 = Safety_Calculations.is_positive(request.POST['wc_voltage'])
        H = Safety_Calculations.is_number(request.POST['wc_height'])
        H2 = Safety_Calculations.is_positive(request.POST['wc_height'])
        W = Safety_Calculations.is_number(request.POST['wc_width'])
        W2 = Safety_Calculations.is_positive(request.POST['wc_width'])
        VS = Safety_Calculations.is_choice(request.POST['wc_voltage_system'],'Sistema')
        BS = Safety_Calculations.is_choice(request.POST['wc_backspace'],'Acceso posterior?')
        CO = Safety_Calculations.is_choice(request.POST['wc_condition'],'Condicion?')

        # Realizar cálculo de los espacios de trabajo si el formulario no tiene errores
        if V and V2 and H and H2 and W and W2 and VS and BS and CO:
            # Importar las variables del formulario
            V = float(request.POST['wc_voltage'])
            H = float(request.POST['wc_height'])
            W = float(request.POST['wc_width'])
            VS = request.POST['wc_voltage_system'] # Sistema monofásico, bifásico o trifásico
            BS = request.POST['wc_backspace'] # Espacio de trabajo en la parte posterior
            CO = request.POST['wc_condition'] # Condición en la cual se encuentra el tablero

            DC, HC, WC, BC = Safety_Calculations.work_clearances(V, H, W, VS, CO, BS)
            print(DC, HC, WC, BC)

            # Se envían los resultados del espacio de trabajo a la vista correspondiente.
            return render(request, 'calculations/workclearances_calculations.html', {'height':HC,
            'width': WC, 'depth':DC, 'back':BC, 'condition':CO,'voltage':V})
        else:
            return render(request, 'calculations/workclearances_calculations.html',
            {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def work_clearances_result(request):
    # Una vez que en la vista anterior se han ingresado los datos se realiza el cálculo del espacio
    # de trabajo.

    # Validar los datos de ingreso al formulario del HTML
    V = Safety_Calculations.is_number(request.POST['wc_voltage'])
    V2 = Safety_Calculations.is_positive(request.POST['wc_voltage'])
    H = Safety_Calculations.is_number(request.POST['wc_height'])
    H2 = Safety_Calculations.is_positive(request.POST['wc_height'])
    W = Safety_Calculations.is_number(request.POST['wc_width'])
    W2 = Safety_Calculations.is_positive(request.POST['wc_width'])
    VS = Safety_Calculations.is_choice(request.POST['wc_voltage_system'],'Sistema')
    BS = Safety_Calculations.is_choice(request.POST['wc_backspace'],'Acceso posterior?')
    CO = Safety_Calculations.is_choice(request.POST['wc_condition'],'Condicion?')

    # Realizar cálculo de los espacios de trabajo si el formulario no tiene errores
    if V and V2 and H and H2 and W and W2 and VS and BS and CO:
        # Importar las variables del formulario
        V = float(request.POST['wc_voltage'])
        H = float(request.POST['wc_height'])
        W = float(request.POST['wc_width'])
        VS = request.POST['wc_voltage_system'] # Sistema monofásico, bifásico o trifásico
        BS = request.POST['wc_backspace'] # Espacio de trabajo en la parte posterior
        CO = request.POST['wc_condition'] # Condición en la cual se encuentra el tablero

        DC, HC, WC, BC = Safety_Calculations.work_clearances(V, H, W, VS, CO, BS)
        print(DC, HC, WC, BC)

        # Se envían los resultados del espacio de trabajo a la vista correspondiente.
        return render(request, 'calculations/workclearances_result.html', {'height':HC, 'width': WC, 'depth':DC, 'back':BC, 'condition':CO,'voltage':V})
    else:
        # Si el formulario presenta errores en alguno de los datos ingresados, entonces se muestra
        # un error al usuario en la misma vista de ingreso de datos.
        return render(request, 'calculations/workclearances_calculations.html',
        {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def safety_clearances_calculation(request):
    # Esta función se encarga de determinar las distancias de seguridad
    # basado en el RETIE actual legal y vigente. Esta vista carga el formulario
    # de ingreso de datos. El usuario deberá ingresar si el sistema es corriente,
    # alterna o continua.
    if request.method != 'POST':
        return render(request, 'calculations/safetyclearances_calculations.html')
    else:
        # Una vez que el usuario ha ingresado los datos de cálculo se determina
        # en esta vista cuáles son las distancias de seguridad para el nivel de tensión
        # indicado.

        # Validar los datos ingresados por el usuario.
        R = Safety_Calculations.isin_range(request.POST['sc_voltage'],50,550000)
        V = Safety_Calculations.is_number(request.POST['sc_voltage'])
        S = Safety_Calculations.is_choice(request.POST['sc_voltage_system'],'¿Tipo de Sistema?')

        if V and S and R:
            # Importar las variables del formulario
            V = float(request.POST['sc_voltage'])
            S = request.POST['sc_voltage_system'] # Sistema monofásico, bifásico o trifásico

            SCM, SCS, RC = Safety_Calculations.safety_clearances(V, S)

            # Se renderizan los resultados de las distancias de seguridad en la vista de resultados.
            return render(request, 'calculations/safetyclearances_calculations.html',
            {'error':'BAJA PARA VER EL RESULTADO','safety_clearance_movil':SCM, 'safety_clearance_static': SCS,
            'restricted_clearance':RC, 'voltage':V, 'system':S})
        else:
            return render(request, 'calculations/safetyclearances_calculations.html',
            {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def safety_clearances_result(request):
    # Una vez que el usuario ha ingresado los datos de cálculo se determina
    # en esta vista cuáles son las distancias de seguridad para el nivel de tensión
    # indicado.

    # Validar los datos ingresados por el usuario.
    R = Safety_Calculations.isin_range(request.POST['sc_voltage'],50,550000)
    V = Safety_Calculations.is_number(request.POST['sc_voltage'])
    S = Safety_Calculations.is_choice(request.POST['sc_voltage_system'],'¿Tipo de Sistema?')

    if V and S and R:
        # Importar las variables del formulario
        V = float(request.POST['sc_voltage'])
        S = request.POST['sc_voltage_system'] # Sistema monofásico, bifásico o trifásico

        SCM, SCS, RC = Safety_Calculations.safety_clearances(V, S)

        # Se renderizan los resultados de las distancias de seguridad en la vista de resultados.
        return render(request, 'calculations/safetyclearances_result.html', {'safety_clearance_movil':SCM, 'safety_clearance_static': SCS, 'restricted_clearance':RC, 'voltage':V})
    else:
        # Si hay un error en el ingreso de los datos entonces se muestra un error en le misma vista del
        # formulario.
        return render(request, 'calculations/safetyclearances_calculations.html', {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def arcflash_calculation(request):
    # Esta vista carga el formulario de ingreso de datos al usuario. Aquí el usuario puede
    # ingresar el nivel de tensión, la corriente de cortocircuito y el tiempo de despeje de falla.
    if request.method != 'POST':
        return render(request, 'calculations/arcflash_calculations.html')
    else:
        # Validar los datos ingresados en el formulario HTML
        V = Arc_Flash_Calculation.is_number(request.POST['ar_voltage'])
        I = Arc_Flash_Calculation.is_number(request.POST['ar_current'])
        t = Arc_Flash_Calculation.is_number(request.POST['ar_time'])
        D = Arc_Flash_Calculation.is_number(request.POST['ar_distance'])
        G = Arc_Flash_Calculation.is_number(request.POST['ar_conductors_separation'])
        V2 = Arc_Flash_Calculation.is_positive(request.POST['ar_voltage'])
        I2 = Arc_Flash_Calculation.is_positive(request.POST['ar_current'])
        t2 = Arc_Flash_Calculation.is_positive(request.POST['ar_time'])
        D2 = Arc_Flash_Calculation.is_positive(request.POST['ar_distance'])
        G2 = Arc_Flash_Calculation.is_positive(request.POST['ar_conductors_separation'])
        KP = Arc_Flash_Calculation.is_choice(request.POST['ar_panel_kind'],'tablero')
        KA = Arc_Flash_Calculation.is_choice(request.POST['ar_arc_kind'],'arco')
        KE = Arc_Flash_Calculation.is_choice(request.POST['ar_earth_kind'],'tierra')
        KM = Arc_Flash_Calculation.is_choice(request.POST['ar_method'],'metodo')

        # Se realiza el cálculo si todos los valores ingresados por el usuario son correctos
        if V and V2 and I and I2 and t and t2 and D and D2 and G and G2 and KP and KA and KE and KM:
            # Importar las variables del formulario
            V = float(request.POST['ar_voltage'])
            I = float(request.POST['ar_current'])
            t = float(request.POST['ar_time'])
            D = float(request.POST['ar_distance'])
            G = float(request.POST['ar_conductors_separation'])
            KP = request.POST['ar_panel_kind'] # Kind of Panel (CCM o PP)
            KA = request.POST['ar_arc_kind'] # Kind of arc flash (O - Opened, C - Closed)
            KE = request.POST['ar_earth_kind'] # Kind of earth (HR - High Resistance or WR - Without Resistance)
            KM = request.POST['ar_method'] # Method of calculation

            IE, Category, EPPs_1, EPPs_2 = Arc_Flash_Calculation.incident_energy(V, I, t, D, G, KP, KA, KE, KM)
            print(IE)

            # Se envía el resultado a la vista de resultado de arco eléctrico.
            return render(request, 'calculations/arcflash_calculations.html', {'result':round(IE,3),
            'category':Category,'volts':V,'amperes':I,'seconds':t,'EPPs_1':EPPs_1,'EPPs_2':EPPs_2,'meth':KM})
        else:
            return render(request, 'calculations/arcflash_calculations.html',
            {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def arcflash_result(request):
    # Una vez que en la vista anterior el usuario ha ingresado los datos en el formulario
    # se realiza el cálculo de la energía incidente y se le recomienda al usuario unos epps de categoría
    # dependiendo del valor de la energía incidente.

    # Validar los datos ingresados en el formulario HTML
    V = Arc_Flash_Calculation.is_number(request.POST['ar_voltage'])
    I = Arc_Flash_Calculation.is_number(request.POST['ar_current'])
    t = Arc_Flash_Calculation.is_number(request.POST['ar_time'])
    D = Arc_Flash_Calculation.is_number(request.POST['ar_distance'])
    G = Arc_Flash_Calculation.is_number(request.POST['ar_conductors_separation'])
    V2 = Arc_Flash_Calculation.is_positive(request.POST['ar_voltage'])
    I2 = Arc_Flash_Calculation.is_positive(request.POST['ar_current'])
    t2 = Arc_Flash_Calculation.is_positive(request.POST['ar_time'])
    D2 = Arc_Flash_Calculation.is_positive(request.POST['ar_distance'])
    G2 = Arc_Flash_Calculation.is_positive(request.POST['ar_conductors_separation'])
    KP = Arc_Flash_Calculation.is_choice(request.POST['ar_panel_kind'],'tablero')
    KA = Arc_Flash_Calculation.is_choice(request.POST['ar_arc_kind'],'arco')
    KE = Arc_Flash_Calculation.is_choice(request.POST['ar_earth_kind'],'tierra')
    KM = Arc_Flash_Calculation.is_choice(request.POST['ar_method'],'metodo')

    # Se realiza el cálculo si todos los valores ingresados por el usuario son correctos
    if V and V2 and I and I2 and t and t2 and D and D2 and G and G2 and KP and KA and KE and KM:
        # Importar las variables del formulario
        V = float(request.POST['ar_voltage'])
        I = float(request.POST['ar_current'])
        t = float(request.POST['ar_time'])
        D = float(request.POST['ar_distance'])
        G = float(request.POST['ar_conductors_separation'])
        KP = request.POST['ar_panel_kind'] # Kind of Panel (CCM o PP)
        KA = request.POST['ar_arc_kind'] # Kind of arc flash (O - Opened, C - Closed)
        KE = request.POST['ar_earth_kind'] # Kind of earth (HR - High Resistance or WR - Without Resistance)
        KM = request.POST['ar_method'] # Method of calculation

        IE, Category, EPPs_1, EPPs_2 = Arc_Flash_Calculation.incident_energy(V, I, t, D, G, KP, KA, KE, KM)
        print(IE)

        # Se envía el resultado a la vista de resultado de arco eléctrico.
        return render(request, 'calculations/arcflash_result.html', {'result':round(IE,3),'category':Category,
        'voltage':V,'current':I,'time':t,'EPPs_1':EPPs_1,'EPPs_2':EPPs_2})
    else:
        # Si los datos ingresados no son correctos entonces se muestra un error en la vista del formulario
        return render(request, 'calculations/arcflash_calculations.html', {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def arcflash_epps(request):
    # Esta vista le muestra al usuario la tabla de elementos de protección personal
    # para que él pueda elegir cuales le aplican basado en la categoría del riesgo.
    return render(request, 'calculations/arcflash_epps.html')

def arcflash_gtable(request):
    # Esta vista se encarga de mostrarle al usuario las distancias de separación
    # típicas entre conductores de acuerdo al anexo D de la NFPA 70E.
    return render(request, 'calculations/arcflash_gtable.html')

def about(request):
    # Se carga en esta vista la plantilla que muestra lo correspondiente a esta vista
    about_items = AboutApp.objects.order_by('id')
    return render(request, 'calculations/about.html', {'abouts':about_items})
