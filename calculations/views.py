from django.shortcuts import render
from django.http import HttpResponse

# import calculations (own library)
from electrical_lib import Cable_Calculations
from electrical_lib import Arc_Flash_Calculation
from electrical_lib import Conduits_Calculation
from electrical_lib import Safety_Calculations

# Create your views here.
def cable_calculation(request):
    return render(request, 'calculations/cable_calculations.html')

def cable_result(request):

    # Validar los datos de ingreso al formulario del HTML
    validation = Cable_Calculations.cable_validation(request.POST['ca_potencia'],
    request.POST['ca_unidades'], request.POST['ca_fases'], request.POST['ca_fp'],
    request.POST['ca_tension'], request.POST['ca_longitud'], request.POST['ca_temperature'],
    request.POST['ca_temp-conductor'], request.POST['ca_carga_continua'], request.POST['ca_material'],
    request.POST['ca_numero-conductores'], request.POST['ca_conduit'])
    print(validation)

    # Realizar cálculo de los conductores si el formulario no tiene errores
    if not validation == 'Error':
        P = float(request.POST['ca_potencia'])
        U = request.POST['ca_unidades']
        Ph = float(request.POST['ca_fases'])
        FP = float(request.POST['ca_fp'])
        V = float(request.POST['ca_tension'])
        L = float(request.POST['ca_longitud'])
        T_amb = float(request.POST['ca_temperature'])
        T_cond = float(request.POST['ca_temp-conductor'])
        print(T_amb)
        CL = request.POST['ca_carga_continua']
        K = request.POST['ca_material']
        NC = float(request.POST['ca_numero-conductores'])
        C = request.POST['ca_conduit']

        ph, n, g, V_drop, pd, fa_corr = Cable_Calculations.cable_calculation(P, U, Ph, FP, V, L, T_cond, T_amb, CL, K, NC, C)
        return render(request, 'calculations/cable_result.html', {'phase':ph, 'neutral':n,'ground':g, 'Vdrop':round(V_drop,2),
        'protective':pd, 'corrective_factor':fa_corr})
    else:
        return render(request, 'calculations/cable_calculations.html', {'error':'El formulario contiene errores'})

def drop_voltage(request):
    return render(request, 'calculations/drop_voltage.html')

def drop_voltage_result(request):

    # Validar datos de ingreso del usuario. Las funciones retornan True or False
    V = Cable_Calculations.is_number(request.POST['dro_voltage'])
    L = Cable_Calculations.is_number(request.POST['dro_length'])
    I = Cable_Calculations.is_number(request.POST['dro_current'])
    FP = Cable_Calculations.is_number(request.POST['dro_pf'])
    Ph = Cable_Calculations.is_choice(request.POST['dro_system'],'sistema')
    gauge = Cable_Calculations.is_choice(request.POST['dro_cable_gauge'],'calibre')
    KC = Cable_Calculations.is_choice(request.POST['dro_cable_kind'],'material')
    K = Cable_Calculations.is_choice(request.POST['dro_conduit_kind'],'conduit')

    print(Ph, gauge, KC, K)
    if (V and L and I and FP and Ph and gauge and KC and K):
        # Capturar los datos del formulario HTML para realizar el cálculo
        V = float(request.POST['dro_voltage'])
        L = float(request.POST['dro_length'])
        I = float(request.POST['dro_current'])
        FP = float(request.POST['dro_pf'])
        Ph = float(request.POST['dro_system'])
        gauge = request.POST['dro_cable_gauge']
        KC = request.POST['dro_cable_kind']
        K = request.POST['dro_conduit_kind']

        VDrop, VDrop100, R, X = Cable_Calculations.drop_voltage_calculation(Ph, V, L, I, FP, gauge, KC, K)
        return render(request, 'calculations/drop_voltage_result.html',{'drop_voltage':round(VDrop,2),
        'drop_voltage_percentage':round(VDrop100,2), 'resistance':R, 'reactance':X})
    else:
        return render(request, 'calculations/drop_voltage.html',{'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def protective_device(request):
    return render(request, 'calculations/protective_device.html')

def protective_result(request):
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
        return render(request, 'calculations/protective_result.html', {'protective_device':protective})
    else:
        return render(request, 'calculations/protective_device.html', {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def grounding_cable(request):
    return render(request, 'calculations/grounding_cable.html')

def grounding_result(request):

    # Validar los datos ingresados por el usuario
    Protective = Cable_Calculations.is_number(request.POST['gro_ingreso'])
    Material = Cable_Calculations.is_choice(request.POST['gro_diametro'],'material')

    if Protective and Material:
        # Obtener los valores ingresados por el usuario en el formulario HTML
        Protective = float(request.POST['gro_ingreso'])
        Material = request.POST['gro_diametro']

        # Realizar la selección del conductor de puesta a tierra
        grounding_cable = Cable_Calculations.earth_conductor(Protective, Material)

        return render(request, 'calculations/grounding_result.html',{'protective':Protective,
        'gauge':grounding_cable,'material':Material})
    else:
        return render(request, 'calculations/grounding_cable.html',{'error':'El formulario contiene errores.'})

def electrode_cable(request):
    return render(request, 'calculations/electrode_cable.html')

def electrode_result(request):

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

def conduit_calculation(request):
    return render(request, 'calculations/conduits_calculation.html')

def conduit_result(request):

    # Validar los datos de ingreso al formulario del HTML
    validation = Conduits_Calculation.data_validation(request.POST['co_ingreso'],
    request.POST['co_diametro'], request.POST['co_conduit_kind'])
    print(validation)

    # Realizar cálculo de conduits si el formulario no tiene errores
    if not validation == 'Error':
        DoA = Conduits_Calculation.convert2list_or_value(request.POST['co_ingreso']) # Variable de Diámetro o Área
        print(DoA)

        SDA = request.POST['co_diametro'] # Variable de selección de diámetro o área
        CK = request.POST['co_conduit_kind'] # Tipo de tubería
        conduit = Conduits_Calculation.conduit_sizing(DoA,CK,SDA)
        return render(request, 'calculations/conduits_result.html', {'kind_of_conduit':CK, 'conduit':conduit})
    else:
        return render(request, 'calculations/conduits_calculation.html', {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def work_clearances_calculation(request):
    return render(request, 'calculations/workclearances_calculations.html')

def work_clearances_result(request):

    # Validar los datos de ingreso al formulario del HTML
    validation = Safety_Calculations.work_validation(request.POST['wc_voltage'],
    request.POST['wc_height'], request.POST['wc_width'], request.POST['wc_voltage_system'],
    request.POST['wc_backspace'], request.POST['wc_condition'])
    print(validation)

    # Realizar cálculo de los espacios de trabajo si el formulario no tiene errores
    if not validation == 'Error':
        # Importar las variables del formulario
        V = float(request.POST['wc_voltage'])
        H = float(request.POST['wc_height'])
        W = float(request.POST['wc_width'])
        VS = request.POST['wc_voltage_system'] # Sistema monofásico, bifásico o trifásico
        BS = request.POST['wc_backspace'] # Espacio de trabajo en la parte posterior
        CO = request.POST['wc_condition'] # Condición en la cual se encuentra el tablero

        DC, HC, WC, BC = Safety_Calculations.work_clearances(V, H, W, VS, CO, BS)
        print(DC, HC, WC, BC)

        return render(request, 'calculations/workclearances_result.html', {'height':HC, 'width': WC, 'depth':DC, 'back':BC, 'condition':CO,'voltage':V})
    else:
        return render(request, 'calculations/workclearances_calculations.html', {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def safety_clearances_calculation(request):
    return render(request, 'calculations/safetyclearances_calculations.html')

def safety_clearances_result(request):

    validation = Safety_Calculations.safety_validation(request.POST['sc_voltage'],
    request.POST['sc_voltage_system'])
    print(validation)

    if not validation == 'Error':
        # Importar las variables del formulario
        V = float(request.POST['sc_voltage'])
        S = request.POST['sc_voltage_system'] # Sistema monofásico, bifásico o trifásico

        SCM, SCS, RC = Safety_Calculations.safety_clearances(V, S)

        return render(request, 'calculations/safetyclearances_result.html', {'safety_clearance_movil':SCM, 'safety_clearance_static': SCS, 'restricted_clearance':RC, 'voltage':V})
    else:
        return render(request, 'calculations/safetyclearances_calculations.html', {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})

def arcflash_calculation(request):
    return render(request, 'calculations/arcflash_calculations.html')

def arcflash_result(request):

    # Validar los datos ingresados en el formulario HTML
    validation = Arc_Flash_Calculation.data_validation(request.POST['ar_voltage'],
    request.POST['ar_short_circuit_current'], request.POST['ar_time'],
    request.POST['ar_distance'], request.POST['ar_conductors_separation'],
    request.POST['ar_panel_kind'], request.POST['ar_arc_kind'], request.POST['ar_earth_kind'],
    request.POST['method'])

    if not validation == 'Error':
        # Importar las variables del formulario
        V = float(request.POST['ar_voltage'])
        I = float(request.POST['ar_short_circuit_current'])
        t = float(request.POST['ar_time'])
        D = float(request.POST['ar_distance'])
        G = float(request.POST['ar_conductors_separation'])
        KP = request.POST['ar_panel_kind'] # Kind of Panel (CCM o PP)
        KA = request.POST['ar_arc_kind'] # Kind of arc flash (O - Opened, C - Closed)
        KE = request.POST['ar_earth_kind'] # Kind of earth (HR - High Resistance or WR - Without Resistance)
        KM = request.POST['method'] # Method of calculation

        IE, EPPs = Arc_Flash_Calculation.incident_energy(V, I, t, D, G, KP, KA, KE, KM)
        print(IE)

        return render(request, 'calculations/arcflash_result.html', {'result':round(IE,3), 'epps':EPPs})
    else:
        return render(request, 'calculations/arcflash_calculations.html', {'error':'El formulario tiene errores, por favor verifica los datos ingresados'})
