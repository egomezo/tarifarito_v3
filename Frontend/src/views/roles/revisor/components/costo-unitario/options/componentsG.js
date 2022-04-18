/* jshint esversion: 6 */
/* eslint-disable */
const componentesGeneracion = [{
        title: 'Demanda Comercial Regulada',
        campo: '16',
        name: '1',
        data: [{
                campo: '16',
                concepto: 'Demanda Comercial Regulada',
                unidad: 'kWh',
                inputs: [
                    { key: 'c16_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c16_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c16_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
                ]
            },
            {
                campo: '12',
                concepto: 'Demanda Real Regulada',
                unidad: 'kWh',
                type: 'number',
                placeholder: 'Valor',
                inputs: [
                    { key: 'c12_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c12_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c12_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '13',
                concepto: 'Ajuste Demanda Real Regulada',
                unidad: 'kWh',
                type: 'number',
                placeholder: 'Valor',
                inputs: [
                    { key: 'c13_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c13_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c13_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '14',
                concepto: 'Pérdida Real de la Demanda Regulada',
                unidad: 'kWh',
                type: 'number',
                placeholder: 'Valor',
                inputs: [
                    { key: 'c14_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c14_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c14_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '15',
                concepto: 'Ajuste Pérdida Real de la Demanda Regulada',
                unidad: 'kWh',
                type: 'number',
                placeholder: 'Valor',
                inputs: [
                    { key: 'c15_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c15_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c15_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            }
        ]
    },
    {
        title: 'Fracción DCR atendida con compras en contratos',
        campo: '17',
        name: '2',
        data: [{
            campo: '17',
            concepto: 'Qc',
            unidad: '%',
            inputs: [
                { key: 'c17_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c17_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c17_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
            ]
        }]
    },
    {
        title: 'Costo promedio de la energía comprada en contratos',
        campo: '22',
        name: '3',
        data: [{
                campo: '22',
                concepto: 'Pc',
                unidad: 'kWh',
                inputs: [
                    { key: 'c22_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c22_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c22_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
                ]
            },
            {
                campo: '1',
                concepto: 'Compras en contratos MR (AGENTE)',
                unidad: 'kWh',
                type: 'number',
                placeholder: 'Valor',
                inputs: [
                    { key: 'c1_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c1_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c1_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '2',
                concepto: 'Compras en contratos MR (ASIC)',
                unidad: 'kWh',
                type: 'number',
                placeholder: 'Valor',
                inputs: [
                    { key: 'c2_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c2_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c2_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '3',
                concepto: 'Ajuste compras en contratos MR',
                unidad: 'kWh',
                type: 'number',
                placeholder: 'Valor',
                inputs: [
                    { key: 'c3_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c3_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c3_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '4',
                concepto: 'Valor compras en contratos MR (AGENTE)',
                unidad: '$',
                type: 'number',
                placeholder: 'Valor',
                inputs: [
                    { key: 'c4_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c4_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c4_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '5',
                concepto: 'Valor compras en contratos MR (ASIC)',
                unidad: '$',
                type: 'number',
                placeholder: 'Valor',
                inputs: [
                    { key: 'c5_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c5_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c5_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '6',
                concepto: 'Ajuste valor compras en contratos MR',
                unidad: '$',
                type: 'number',
                placeholder: 'Valor',
                inputs: [
                    { key: 'c6_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c6_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c6_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            }
        ]
    },
    {
        title: 'Fracción DCR atendida con compras en bolsa',
        campo: '18',
        name: '4',
        data: [{
            campo: '18',
            concepto: 'Qb',
            unidad: '%',
            inputs: [
                { key: 'c18_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c18_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c18_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
            ]
        }]
    },
    {
        title: 'Costo promedio ponderado de la energía comprada en bolsa',
        campo: '23',
        name: '5',
        data: [{
                campo: '23',
                concepto: 'Pb',
                unidad: '$/kWh',
                inputs: [
                    { key: 'c23_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c23_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c23_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
                ]
            },
            {
                campo: '7',
                concepto: 'Compras en bolsa MR',
                unidad: 'kWh',
                inputs: [
                    { key: 'c7_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c7_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c7_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '8',
                concepto: 'Valor compras en bolsa MR',
                unidad: '$',
                inputs: [
                    { key: 'c8_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c8_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c8_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            }
        ]
    },
    {
        title: 'Fracción demanda comercial atendida con AGD',
        campo: '21',
        name: '6',
        data: [{
                campo: '21',
                concepto: 'Qagd',
                unidad: '%',
                inputs: [
                    { key: 'c21_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c21_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c21_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
                ]
            },
            {
                campo: '19',
                concepto: 'AGPE',
                unidad: '%',
                inputs: [
                    { key: 'c19_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c19_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c19_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '20',
                concepto: 'GD',
                unidad: '%',
                inputs: [
                    { key: 'c20_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c20_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c20_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            }
        ]
    },
    {
        title: 'Costo promedio ponderado por energía (Mc) aplicado',
        campo: '11',
        name: '7',
        data: [{
                campo: '11',
                concepto: 'Mc aplicado',
                unidad: '$/kWh',
                inputs: [
                    { key: 'c11_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c11_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                    { key: 'c11_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
                ]
            },
            {
                campo: '9',
                concepto: 'Mc',
                unidad: '$/kWh',
                inputs: [
                    { key: 'c9_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c9_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c9_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            },
            {
                campo: '10',
                concepto: 'Ajuste Mc',
                unidad: '$/kWh',
                inputs: [
                    { key: 'c10_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                    { key: 'c10_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                    { key: 'c10_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
                ]
            }
        ]
    },
    {
        title: 'Factor de ajuste AJ',
        campo: '24',
        name: '8',
        data: [{
            campo: '24',
            concepto: 'Factor de Ajuste AJ',
            unidad: '$/kWh',
            inputs: [
                { key: 'c24_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                { key: 'c24_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                { key: 'c24_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
            ]
        }]
    },
    {
        title: 'Alfa',
        campo: '25',
        name: '9',
        data: [{
            campo: '25',
            concepto: 'Alfa',
            unidad: 'Adimensional',
            inputs: [
                { key: 'c25_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                { key: 'c25_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                { key: 'c25_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
            ]
        }]
    },
    {
        title: 'G Transitorio',
        campo: '26',
        name: '10',
        data: [{
            campo: '26',
            concepto: 'G Transitorio',
            unidad: '$/kWh',
            inputs: [
                { key: 'c26_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                { key: 'c26_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                { key: 'c26_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
            ]
        }]
    },
    {
        title: 'G Contratos',
        campo: '29',
        name: '11',
        data: [{
            campo: '29',
            concepto: 'G Contratos',
            unidad: '',
            inputs: [
                { key: 'c29_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c29_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c29_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
            ]
        }]
    },
    {
        title: 'G Bolsa',
        campo: '30',
        name: '12',
        data: [{
            campo: '30',
            concepto: 'G Bolsa',
            unidad: '',
            inputs: [
                { key: 'c30_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c30_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c30_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
            ]
        }]
    },
    {
        title: 'CFNC',
        campo: '27',
        name: '13',
        data: [{
            campo: '27',
            concepto: 'CFNC',
            unidad: '$/kWh',
            inputs: [
                { key: 'c27_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
                { key: 'c27_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
                { key: 'c27_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
            ]
        }]
    },
    {
        title: 'Componente Generación',
        campo: '28',
        name: '14',
        data: [{
            campo: '28',
            concepto: 'Componente Generación',
            unidad: '$/kWh',
            inputs: [
                { key: 'c28_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c28_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, disabled: true, value: 87 },
                { key: 'c28_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, disabled: true, value: 0 }
            ]
        }]
    }
];

export default componentesGeneracion;