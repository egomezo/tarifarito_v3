/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    formItem: {
        idtercero: '',
        persona: '',
        documento: '',
        nombre: '',
        direccion: '',
        email: ''
    },
    domItem: [
        {
            type: 'radiogroup',
            prop: 'persona'
        },
        {
            type: 'divider'
        },
        {
            type: 'number',
            prop: 'documento',
            label: 'Identificación',
            placeholder: 'Ingrese una identificación'
        },
        {
            type: 'text',
            prop: 'nombre',
            label: 'Nombre',
            placeholder: 'Ingrese un nombre'
        },
        {
            type: 'text',
            prop: 'direccion',
            label: 'Dirección',
            placeholder: 'Ingrese una dirección'
        },
        {
            type: 'email',
            prop: 'email',
            label: 'E-mail',
            placeholder: 'Ingrese un correo válido'
        }
    ],
    rulesFormItem: {
        persona: [{required: true, message: 'Seleccione un tipo de persona', trigger: 'change'}],
        documento: [
            { required: true, message: 'Ingrese un documento' },
            { type: 'number', message: 'Este campo debe ser numérico' }
        ],
        nombre: [{ required: true, message: 'Ingrese un nombre', trigger: 'blur' }],
        direccion: [{ required: true, message: 'Ingrese una dirección', trigger: 'blur' }],
        email: [{ type: "email", required: true, message: 'Ingrese un correo electrónico válido', trigger: 'blur' }]
    },
    dataFormItem: {
        // Aqui van todos los arreglos de objetos de los controles select, radiobutton, etc...
        persona: [{
            id: 1,
            label: 'Persona natural'
        },
        {
            id: 2,
            label: 'Persona jurídica'
        }]
    }
};