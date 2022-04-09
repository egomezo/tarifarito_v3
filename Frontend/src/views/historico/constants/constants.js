/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    tHeaderGeneral: [
        'Año', 'Expediente', 'Empresa', 'NIT', 'Servicio', 'r_memorado_devolucion_ig',
        'Fecha memorando devolución IG', 'acto_administrativo_archivo_preliminar', 'Fecha acto administrativo archivo preliminar', 'acto_administrativo_acumulacion',
        'Fecha acto administrativo acumulación', 'resolucion_decision', 'Fecha decisión', 'Tipo decisión',
        'Valor sanción (si aplica)', 'resolucion_recurso', 'Fecha resolución recurso', 'Tipo decisión recurso',
        'Valor sanción recurso (si aplica)', 'Fecha firmeza', 'firmeza'],
    filterValGeneral: [
        'anio', 'expediente', 'n_empresa', 'nit_empresa', 'n_servicio', 'r_memorado_devolucion_ig', 'f_memorando_devolucion_ig', 'acto_administrativo_archivo_preliminar',
        'f_acto_administrativo_archivo_preliminar', 'acto_administrativo_acumulacion', 'f_acto_administrativo_acumulacion', 'resolucion_decision',
        'f_decision', 'n_tipo_decision', 'valor_sancion', 'resolucion_recurso', 'f_resolucion_recurso',
        'n_decision_recurso', 'valor_sancion_recurso', 'f_firmeza', 'firmeza'],
    tHeaderEspecifica: ['Año', 'Expediente', 'Empresa', 'Servicio', 'Número cargo', 'Cargo', 'Norma infringida', 'Causal', 'Subcausal'],
    filterValEspecifica: ['anio', 'expediente', 'empresa', 'servicio', 'numero_cargo', 'cargo', 'norma_infringida', 'causal', 'sub_causal'],
    tableColumnsGeneral: [
        {
            label: 'Año',
            prop: 'anio',
            width: '',
            align: 'center',
            sortable: true
        },
        {
            label: 'Expediente',
            prop: 'expediente',
            width: '157',
            align: 'center',
            sortable: true
        },
        {
            label: 'Empresa',
            prop: 'n_empresa',
            width: '245',
            align: 'center',
            sortable: true
        },
        {
            label: 'Nit',
            prop: 'nit_empresa',
            width: '110',
            align: 'center',
            sortable: true
        },
        {
            label: 'Decisión',
            prop: 'f_decision',
            width: '135',
            align: 'center',
            sortable: true
        },
        {
            // label: 'Resolución recurso',
            label: 'Recurso',
            prop: 'f_resolucion_recurso',
            width: '135',
            align: 'center',
            sortable: true
        },
        {
            label: 'Firmeza',
            prop: 'f_firmeza',
            width: '135',
            align: 'center',
            sortable: true
        },
        {
            label: 'Causas',
            prop: 'causas',
            width: '450',
            align: '',
            sortable: false
        },
        {
            label: 'Subcausales',
            prop: 'subcausales',
            width: '655',
            align: '',
            sortable: false
        },
    ],
    tableExpandGeneral: [
        {
            label: 'Servicio',
            prop: 'n_servicio',
            width: '',
        },
        {
            label: 'Fecha devolución IG',
            prop: 'f_memorando_devolucion_ig',
            width: '',
        },
        {
            label: 'Memorando devolución IG',
            prop: 'r_memorado_devolucion_ig',
            width: '',
            download: true
        },
        {
            label: 'Acto administrativo archivo preliminar',
            prop: 'acto_administrativo_archivo_preliminar',
            width: '',
            download: true
        },
        {
            label: 'Fecha acto administrativo archivo preliminar',
            prop: 'f_acto_administrativo_archivo_preliminar',
            width: '',
        },
        {
            label: 'Acto administrativo acumulación',
            prop: 'acto_administrativo_acumulacion',
            width: '',
            download: true
        },
        {
            label: 'Fecha acto administrativo acumulación',
            prop: 'f_acto_administrativo_acumulacion',
            width: '',
        },
        {
            label: 'Resolución decisión',
            prop: 'resolucion_decision',
            width: '',
            download: true
        },
        {
            label: 'Tipo decisión',
            prop: 'n_tipo_decision',
            width: '',
        },
        {
            label: 'Valor sanción',
            prop: 'valor_sancion',
            width: '',
        },
        {
            label: 'Resolución recurso',
            prop: 'resolucion_recurso',
            width: '',
            download: true
        },
        {
            label: 'Decisión recurso',
            prop: 'n_decision_recurso',
            width: '',
        },
        {
            label: 'Valor sanción recurso',
            prop: 'valor_sancion_recurso',
            width: '',
        },
        {
            label: 'Firmeza',
            prop: 'firmeza',
            width: '',
            download: true
        },
        {
            label: 'Ver cargos',
            prop: 'cargos',
            width: ''
        },
    ]
};