// Validación de datos para el formulario de distancias de seguridad
const submit = document.getElementById('sc_calculate');
const voltage = document.getElementById('sc_voltage');
const voltage_system = document.getElementById('sc_voltage_system');

submit.addEventListener('submit',(event) => {
  event.preventDefault();

  voltage_value = parseInt(voltage.value);

  if (voltage.value < 0 || voltage.value > 550000 || isNan(voltage.value)){
    document.getElementById('sc_voltage').classList.add('group_form-mistaken');
    document.getElementById('voltage_error_paragraph').classList.add('form_input-error-active');
  } else if (voltage_system.value === '¿Tipo de Sistema?') {
    document.getElementById('select-form').classList.add('group_form-mistaken');
    document.getElementById('system_error_paragraph').classList.add('form_input-error-active');
  } else {
    submit.submit();
  }
});
