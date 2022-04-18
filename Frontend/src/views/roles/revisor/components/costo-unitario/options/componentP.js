/* jshint esversion: 6 */
/* eslint-disable */
const componentePerdidas = [{
        title: 'Componente de Generación',
        campo: '1',
        name: '1',
        data: [{
            campo: '1',
            concepto: 'Componente de Generación',
            unidad: '$/kWh',
            inputs: [
                { key: 'c1_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                { key: 'c1_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                { key: 'c1_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
            ]
        }]
    },
    {
        title: 'Componente de Transmisión',
        campo: '14',
        name: '2',
        data: [{
            campo: '14',
            concepto: 'Componente de Transmisión',
            unidad: '$/kWh',
            inputs: [
                { key: 'c14_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                { key: 'c14_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                { key: 'c14_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
            ]
        }]
    },
    {
        title: 'IPRSTN',
        campo: '9',
        name: '3',
        data: [{
            campo: '9',
            concepto: 'IPRSTN',
            unidad: '%',
            inputs: [
                { key: 'c9_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c9_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c9_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
            ]
        }]
    },
    {
        title: 'Demanda Comercial',
        campo: '8',
        name: '4',
        data: [{
                campo: '8',
                concepto: 'Demanda Comercial',
                unidad: '%',
                inputs: [
                    { key: 'c8_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c8_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c8_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
                ]
            },
            {
                campo: '2',
                concepto: 'Demanda Real Regulada',
                unidad: 'kWh',
                inputs: [
                    { key: 'c2_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c2_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c2_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '3',
                concepto: 'Pérdidas Real de la Demanda Regulada',
                unidad: 'kWh',
                inputs: [
                    { key: 'c3_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c3_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c3_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '4',
                concepto: 'Demanda Real No Regulada',
                unidad: 'kWh',
                inputs: [
                    { key: 'c4_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c4_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c4_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '5',
                concepto: 'Pérdida Real de la Demanda No Regulada',
                unidad: 'kWh',
                inputs: [
                    { key: 'c5_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c5_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c5_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '6',
                concepto: 'Ajuste Demanda Real',
                unidad: 'kWh',
                inputs: [
                    { key: 'c6_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c6_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c6_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '7',
                concepto: 'Ajuste Pérdida Real',
                unidad: 'kWh',
                inputs: [
                    { key: 'c7_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c7_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c7_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            }
        ]
    },
    {
        title: 'Pérdidas Reconocidas de Generación NT1',
        campo: '16',
        name: '5',
        data: [{
            campo: '16',
            concepto: 'Pérdidas Reconocidas de Generación NT1',
            unidad: '$/kWh',
            inputs: [
                { key: 'c16_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c16_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c16_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
            ]
        }]
    },
    {
        title: 'Pérdidas Reconocidas de Transmisión NT1',
        campo: '20',
        name: '6',
        data: [{
                campo: '20',
                concepto: 'Pérdidas Reconocidas de Transmisión NT1',
                unidad: '$/kWh',
                inputs: [
                    { key: 'c20_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c20_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c20_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
                ]
            },
            {
                campo: '10',
                concepto: 'IPR1',
                unidad: '%',
                inputs: [
                    { key: 'c10_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c10_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c10_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            }
        ]
    },
    {
        title: 'Pérdidas Reconocidas de Generación NT2',
        campo: '17',
        name: '7',
        data: [{
            campo: '17',
            concepto: 'Pérdidas Reconocidas de Generación NT2',
            unidad: '$/kWh',
            inputs: [
                { key: 'c17_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c17_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c17_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
            ]
        }]
    },
    {
        title: 'Pérdidas Reconocidas de Transmisión NT2',
        campo: '21',
        name: '8',
        data: [{
                campo: '21',
                concepto: 'Pérdidas Reconocidas de Transmisión NT2',
                unidad: '$/kWh',
                inputs: [
                    { key: 'c21_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c21_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c21_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
                ]
            },
            {
                campo: '11',
                concepto: 'IPR2',
                unidad: '%',
                inputs: [
                    { key: 'c11_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c11_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c11_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            }
        ]
    },
    {
        title: 'Pérdidas Reconocidas de Generación NT3',
        campo: '18',
        name: '9',
        data: [{
            campo: '18',
            concepto: 'Pérdidas Reconocidas de Generación NT3',
            unidad: '$/kWh',
            inputs: [
                { key: 'c18_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c18_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c18_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
            ]
        }]
    },
    {
        title: 'Pérdidas Reconocidas de Transmisión NT3',
        campo: '22',
        name: '10',
        data: [{
                campo: '22',
                concepto: 'Pérdidas Reconocidas de Transmisión NT3',
                unidad: '$/kWh',
                inputs: [
                    { key: 'c22_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c22_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c22_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
                ]
            },
            {
                campo: '23',
                concepto: 'IPR3',
                unidad: '%',
                inputs: [
                    { key: 'c12_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c12_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c12_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            }
        ]
    },
    {
        title: 'Pérdidas Reconocidas de Generación NT4',
        campo: '19',
        name: '11',
        data: [{
            campo: '19',
            concepto: 'Pérdidas Reconocidas de Generación NT4',
            unidad: '$/kWh',
            inputs: [
                { key: 'c19_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c19_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c19_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
            ]
        }]
    },
    {
        title: 'Pérdidas Reconocidas de Transmisión NT4',
        campo: '23',
        name: '12',
        data: [{
                campo: '23',
                concepto: 'Pérdidas Reconocidas de Transmisión NT4',
                unidad: '$/kWh',
                inputs: [
                    { key: 'c23_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c23_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c23_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
                ]
            },
            {
                campo: '13',
                concepto: 'IPR4',
                unidad: '$/kWh',
                inputs: [
                    { key: 'c13_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c13_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c13_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            }
        ]
    },
    {
        title: 'CPROG',
        campo: '15',
        name: '13',
        data: [{
            campo: '15',
            concepto: 'CPROG',
            unidad: '$/kWh',
            inputs: [
                { key: 'c15_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                { key: 'c15_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                { key: 'c15_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
            ]
        }]
    },
    {
        title: 'Componente de Pérdidas NT1',
        campo: '24',
        name: '14',
        data: [{
            campo: '24',
            concepto: 'Componente de Pérdidas NT1',
            unidad: '$/kWh',
            inputs: [
                { key: 'c24_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c24_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c24_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
            ]
        }]
    },
    {
        title: 'Componente de Pérdidas NT2',
        campo: '25',
        name: '15',
        data: [{
            campo: '25',
            concepto: 'Componente de Pérdidas NT2',
            unidad: '$/kWh',
            inputs: [
                { key: 'c25_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c25_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c25_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
            ]
        }]
    },
    {
        title: 'Componente de Pérdidas NT3',
        campo: '26',
        name: '16',
        data: [{
            campo: '26',
            concepto: 'Componente de Pérdidas NT3',
            unidad: '$/kWh',
            inputs: [
                { key: 'c26_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c26_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c26_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
            ]
        }]
    },
    {
        title: 'Componente de Pérdidas NT4',
        campo: '27',
        name: '17',
        data: [{
            campo: '27',
            concepto: 'Componente de Pérdidas NT4',
            unidad: '$/kWh',
            inputs: [
                { key: 'c27_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c27_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c27_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
            ]
        }]
    }
];

export default componentePerdidas;