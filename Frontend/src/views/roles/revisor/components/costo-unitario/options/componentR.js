const componentesRestricciones = [
  {
    title: 'CRS',
    campo: '5',
    name: '1',
    data: [
      {
        campo: '5',
        concepto: 'CRS',
        unidad: '$',
        inputs: [
          { key: 'crs_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
          { key: 'crs_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
          { key: 'crs_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
        ]
      },
      {
        campo: '1',
        concepto: 'Restricciones Aliviadas',
        unidad: '$',
        inputs: [
          { key: 'ra_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
          { key: 'ra_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
          { key: 'ra_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
        ]
      },
      {
        campo: '2',
        concepto: 'Desviaciones',
        unidad: '$',
        inputs: [
          { key: 'd_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
          { key: 'd_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
          { key: 'd_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
        ]
      },
      {
        campo: '3',
        concepto: 'Variante Guatapé',
        unidad: '$',
        inputs: [
          { key: 'vg_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
          { key: 'vg_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
          { key: 'vg_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
        ]
      },
      {
        campo: '4',
        concepto: 'Ajuste Restricciones',
        unidad: '$',
        inputs: [
          { key: 'ar_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
          { key: 'ar_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
          { key: 'ar_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
        ]
      }
    ]
  },
  {
    title: 'Ventas Totales',
    campo: '6',
    name: '2',
    data: [
      {
        campo: '6',
        concepto: 'Ventas Totales',
        unidad: 'kWh',
        inputs: [
          { key: 'vt_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
          { key: 'vt_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
          { key: 'vt_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
        ]
      }
    ]
  },
  {
    title: 'Componente de Restricciones',
    campo: '7',
    name: '3',
    data: [
      {
        campo: '7',
        concepto: 'Componente de Restricciones',
        unidad: '$/kWh',
        inputs: [
          { key: 'vt_1', type: 'number', placeholder: 'Ingrese un valor', start: true, show: true, diferencia: false, value: 87 },
          { key: 'vt_2', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: false, value: 87 },
          { key: 'vt_3', type: 'number', placeholder: 'Ingrese un valor', start: false, show: true, diferencia: true, value: 0 }
        ]
      }
    ]
  }
]

export default componentesRestricciones
