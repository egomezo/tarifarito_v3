/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    formItem: {
        etapa: '',
        radicado: '',
        fechaInicio: null,
        fechaFin: null,
        observacion: ''
    },
    domItem: [{
        type: 'select',
        prop: 'etapa',
        label: 'Etapa',
        placeholder: 'Seleccione una etapa',
        disabled: false
    },
    {
        type: 'text',
        prop: 'radicado',
        label: 'Radicado',
        placeholder: 'Ingrese no. del radicado',
        maxlength: 14,
        showwordlimit: true
    },
    {
        type: 'date',
        prop: 'fechaInicio',
        label: 'Fecha radicado',
        placeholder: 'Seleccione una fecha de radicado'
    },
    {
        type: 'date',
        prop: 'fechaRecepcion',
        label: 'Fecha recepción',
        placeholder: 'Seleccione una fecha de recepción'
    },
    {
        type: 'textarea',
        prop: 'observacion',
        label: 'Observación',
        placeholder: 'Ingrese aquí el texto'
    }],
    rulesFormItem: {
        etapa: [{
            required: true,
            message: 'Seleccione una etapa',
            trigger: 'change'
        }],
        radicado: [
            { required: true, message: 'Ingrese un radicado', trigger: 'blur' },
            { min: 14, max: 14, message: 'La longitud del radicado debe ser de 14 caracteres', trigger: 'blur' }
        ],
        fechaInicio: [{
            required: true,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }],
        observacion: [{
            required: false,
            message: 'Ingrese una observación',
            trigger: 'blur'
        }]
    },
    dataFormItem: {
        // Aqui van todos los arreglos de objetos de los controles select, radiobutton, etc...
        etapa: [],
    }
};