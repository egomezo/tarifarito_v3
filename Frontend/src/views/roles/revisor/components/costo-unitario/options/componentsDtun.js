const componentesTransmision = [
  {
    key: 1,
    start: true,
    show: true,
    header: [
      { title: 'CONCEPTO', tamano: 12 },
      { title: 'UNIDAD', tamano: 4 },
      { title: 'VALORES', tamano: 8 }
    ],
    data: [
      {
        campo: '1',
        start: true,
        show: true,
        concepto: 'DtUn NT-Prop ADD XXXXX (LAC)',
        unidad: '$/kWh',
        input: { key: 'dtunntlac_1', type: 'number', placeholder: 'Ingrese un valor', value: 87 }
      },
      {
        campo: '2',
        start: true,
        show: true,
        concepto: 'DtUn NT-Prop ADD XXXXX (AGENTE)',
        unidad: '$/kWh',
        input: { key: 'dtunntage_1', type: 'number', placeholder: 'Ingrese un valor', value: 80 }
      },
      {
        campo: '3',
        start: false,
        show: true,
        concepto: 'DtUn NT-Prop ADD XXXXX (SSPD)',
        unidad: '$/kWh',
        input: { key: 'dtunntsspd_1', type: 'number', placeholder: 'Ingrese un valor', value: '' }
      }
    ]
  },
  {
    key: 2,
    start: false,
    show: true,
    header: [
      { title: 'CONCEPTO', tamano: 12 },
      { title: 'UNIDAD', tamano: 4 },
      { title: 'VALORES', tamano: 8 }
    ],
    data: [
      {
        campo: '1',
        concepto: 'DtUn NT-Prop ADD XXXXX (LAC)',
        unidad: '$/kWh',
        input: { key: 'dtunlacsspd_1', type: 'number', placeholder: '', value: '0' }
      },
      {
        campo: '2',
        concepto: 'DtUn NT-Prop ADD XXXXX (AGENTE)',
        unidad: '$/kWh',
        input: { key: 'dtunagesspd_1', type: 'number', placeholder: '', value: '0' }
      }
    ]
  }
]

export default componentesTransmision
