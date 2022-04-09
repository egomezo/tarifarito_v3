/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    formItem: {
        radicado: '',
        fechaAutorizacion: ''
    },
    domItem: [
        {
            type: 'text',
            prop: 'radicado',
            label: 'Radicado',
            maxlength: 14,
            showwordlimit: true,
            placeholder: 'Ingrese no. del radicado'
        },
        {
            type: 'date',
            prop: 'fechaAutorizacion',
            label: 'Autorización',
            placeholder: 'Seleccione una fecha de autorización'
        },
        {
            type: 'divider'
        },
        {
            type: 'buttonInput',
            text: 'Agregar correo autorizado'
        },
        {
            type: 'divider'
        }
    ],
    rulesFormItem: {
        radicado: [
            { required: true, message: 'Ingrese un radicado', trigger: 'blur' },
            { min: 14, max: 14, message: 'La longitud debe ser de 14 caracteres', trigger: 'blur' }
        ],
        fechaAutorizacion: [{
            required: true,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }],
    },
    dataFormItem: {
        // Aqui van todos los arreglos de objetos de los controles select, radiobutton, etc...
    }
};