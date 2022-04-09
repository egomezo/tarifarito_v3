/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    // FORM CAUSAL
    formItem: {
        idcausal: '',
        f_hechos: '',
        descripcion: ''
    },
    domItem: [
        {
            type: 'select',
            prop: 'idcausal',
            label: 'Causal',
            placeholder: 'Seleccione una causal'
        },
        {
            type: 'date',
            prop: 'f_hechos',
            label: 'Fecha hechos',
            placeholder: 'Seleccione una fecha de autorización'
        },
        {
            type: 'divider'
        },
        {
            type: 'textarea',
            prop: 'descripcion',
            label: 'Descripción',
            placeholder: 'Ingrese una descripción'
        },
        {
            type: 'divider'
        }
    ],
    rulesFormItem: {
        idcausal: [{
            required: true,
            message: 'Seleccione una causal',
            trigger: 'change'
        }],
        f_hechos: [{
            required: true,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }],
        descripcion: [{
            required: false,
            message: 'Ingrese una descripción del usuario',
            trigger: 'change'
        }],
    },
    dataFormItem: {
        // Aqui van todos los arreglos de objetos de los controles select, radiobutton, etc...
        idcausal: []
    }
};