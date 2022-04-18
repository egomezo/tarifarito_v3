/* jshint esversion: 6 */
/* eslint-disable */
const componentesTransmision = [{
        key: 1,
        start: true,
        show: true,
        title: 'Datos publicados',
        header: [
            { title: 'CONCEPTO', tamano: 12 },
            { title: 'UNIDAD', tamano: 4 },
            { title: 'VALORES', tamano: 8 }
        ],
        data: [{
                campo: '1',
                concepto: 'Cargos por uso del STN MO (AGENTE)',
                unidad: '$/kWh',
                input: { key: 'STNAGENTE', type: 'number', placeholder: 'Ingrese un valor', disabled: true }
            },
            {
                campo: '2',
                concepto: 'Cargos por uso del STN MO (LAC)',
                unidad: '$/kWh',
                input: { key: 'STNLAC', type: 'number', placeholder: 'Ingrese un valor', disabled: true }
            }
        ]
    },
    {
        key: 2,
        start: false,
        show: true,
        title: 'Cálculo SSPD',
        header: [
            { title: 'CONCEPTO', tamano: 12 },
            { title: 'UNIDAD', tamano: 4 },
            { title: 'VALORES', tamano: 8 }
        ],
        data: [{
                campo: '1',
                concepto: 'Cargos por uso T\' publicado por el LAC',
                unidad: '$/kWh',
                input: { key: 'TLAC', type: 'number', placeholder: 'Ingrese un valor', disabled: false }
            },
            {
                campo: '2',
                concepto: 'Delta cargo por uso T\' publicado por el LAC',
                unidad: '$/kWh',
                input: { key: 'DTLAC', type: 'number', placeholder: 'Ingrese un valor', disabled: false }
            },
            {
                campo: '3',
                concepto: 'Componente de Transmisión',
                unidad: '$/kWh',
                input: { key: 'CPT', type: 'number', placeholder: 'Ingrese un valor', disabled: true }
            }
        ]
    },
    {
        key: 3,
        start: false,
        show: true,
        title: 'Diferencias',
        header: [
            { title: 'CONCEPTO', tamano: 12 },
            { title: 'UNIDAD', tamano: 4 },
            { title: 'VALORES', tamano: 8 }
        ],
        data: [{
                campo: '1',
                concepto: 'Componente de Transmisión (AGENTE - SSPD)',
                unidad: '$/kWh',
                input: { key: 'CPTAGENTE', type: 'number', placeholder: 'Ingrese un valor', disabled: true }
            },
            {
                campo: '2',
                concepto: 'Componente de Transmisión (LAC - SSPD)',
                unidad: '$/kWh',
                input: { key: 'CPTLAC', type: 'number', placeholder: 'Ingrese un valor', disabled: true }
            }
        ]
    }
];

export default componentesTransmision;