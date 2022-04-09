/* jshint esversion: 6 */
/* eslint-disable */
export const CONSTANTS = {
    tableColumnsAdmin: [
        // {
        //     label: '#',
        //     prop: 'idproceso',
        //     width: 67
        // },
        {
            label: 'Expediente',
            prop: 'expediente',
            width: 156,
            filter: 'filterExpediente'
        },
        {
            label: 'Servicio',
            prop: 'servicio',
            width: 112,
            filter: 'filterServicio'
        },
        {
            label: 'Empresa',
            prop: 'empresa',
            width: 245,
            filter: 'filterEmpresa'
        },
        {
            label: 'Caducidad',
            prop: 'caducidadsancion',
            width: 135,
            filter: 'filterCaducidadsancion'
        },
        {
            label: 'Estado',
            prop: 'estado',
            width: 300,
            filter: 'filterEstado'
        },
        {
            label: 'Proyectista',
            prop: 'usuario',
            width: 170,
            filter: 'filterAbogado'
        },
        {
            label: 'Revisor',
            prop: 'revisor',
            width: 170,
            filter: 'filterRevisor'
        }
    ],
    tableColumnsAbogado: [
        // {
        //     label: '#',
        //     prop: 'idproceso',
        //     width: 70
        // },
        {
            label: 'Expediente',
            prop: 'expediente',
            width: 156,
            filter: 'filterExpediente'
        },
        {
            label: 'Servicio',
            prop: 'servicio',
            width: 112,
            filter: 'filterServicio'
        },
        {
            label: 'Empresa',
            prop: 'empresa',
            width: 245,
            filter: 'filterEmpresa'
        },
        {
            label: 'Caducidad',
            prop: 'caducidadsancion',
            width: 135,
            filter: 'filterCaducidadsancion'
        },
        {
            label: 'Estado',
            prop: 'estado',
            width: 300,
            filter: 'filterEstado'
        },
        {
            label: 'Proyectista',
            prop: 'usuario',
            width: 170,
            filter: 'filterAbogado'
        },
        {
            label: 'Revisor',
            prop: 'revisor',
            width: 170,
            filter: 'filterRevisor'
        }
    ],
    tableColumnsEtapas: [{
            label: '#',
            prop: 'idetapa',
            width: 70
        },
        {
            label: 'Radicado',
            prop: 'radicadoEtapa'
        },
        {
            label: 'Etapa',
            prop: 'nombreEtapa',
            width: 300
        },
        {
            label: 'Fecha de inicio',
            prop: 'fechaInicioEtapa'
        },
        {
            label: 'Fecha fin',
            prop: 'fechaFinEtapa'
        },
        {
            label: 'Observación',
            prop: 'observacionEtapa',
            width: 300
        }
    ],
    filter: [
        { text: 'Energía', value: 'Energía' },
        { text: 'Gas', value: 'Gas' },
        { text: 'GLP', value: 'GLP' },
    ],
    formAgregar: {
        radicado: '',
        servicio: '',
        empresa: '',
        usuario: '',
        revisor: '',
        fecha_caducidad_sancion: null,
        fecha_caducidad_recurso: null
    },
    rulesFormProceso: {
        radicado: [
            { required: true, message: 'Ingrese un expediente', trigger: 'blur' },
            { min: 17, max: 17, message: 'La longitud del expediente debe ser de 17 caracteres', trigger: 'blur' }
        ],
        servicio: [{
            required: true,
            message: 'Seleccione un servicio',
            trigger: 'change'
        }],
        empresa: [{
            required: true,
            message: 'Seleccione una empresa',
            trigger: 'change'
        }],
        usuario: [{
            required: true,
            message: 'Seleccione un abogado',
            trigger: 'change'
        }],
        revisor: [{
            required: true,
            message: 'Seleccione un revisor',
            trigger: 'change'
        }],
        fecha_caducidad_sancion: [{
            type: 'date',
            required: false,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }],
        fecha_caducidad_recurso: [{
            type: 'date',
            required: false,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }]
    },
    formUsuario: {
        idproceso: '',
        expediente: '',
        usuario: '',
        revisor: '',
    },
    formDetalleProceso: {
        expediente: '',
        tipo_sancion: '',
        decision: '',
        caducidadsancion: '',
        caducidadrecurso: '',
        causa: [],
        descripcion: ''
    },
    rulesDetalleProceso: {
        expediente: [
            { required: true, message: 'Ingrese un expediente', trigger: 'blur' },
            { min: 17, max: 17, message: 'La longitud debe ser de 17 caracteres', trigger: 'blur' }
        ],
        empresa: [{
            required: true,
            message: 'Seleccione una empresa',
            trigger: 'change'
        }],
        tipo_sancion: [{
            required: false,
            message: 'Seleccione un tipo de sanción',
            trigger: 'change'
        }],
        sancion: [
            { required: false, message: 'Valor sanción requerido' }
        ],
        decision: [{
            required: false,
            message: 'Seleccione una decision',
            trigger: 'change'
        }],
        causa: [{
            required: true,
            message: 'Seleccione una causal',
            trigger: 'change'
        }],
        caducidadsancion: [{
            required: false,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }],
        caducidadrecurso: [{
            required: false,
            message: 'Ingrese una fecha válida',
            trigger: 'change'
        }]
    },
    formUser: {
        nombre: '',
        apellido: '',
        genero: '',
        nickname: '',
        contrasena: '',
        rol: '',
        descripcion: '',
        avatar: '',
        token: '',
        email: ''
    },
    rulesFormUser: {
        nombre: [
            { required: true, message: 'Ingrese nombre', trigger: 'blur' }
        ],
        apellido: [
            { required: true, message: 'Ingrese apellido', trigger: 'blur' }
        ],
        genero: [{
            required: true,
            message: 'Seleccione un género',
            trigger: 'change'
        }],
        rol: [{
            required: true,
            message: 'Seleccione un rol',
            trigger: 'change'
        }],
        email: [
            { type: "email", required: true, message: 'Ingrese un correo electrónico válido', trigger: 'blur' },
        ],
        descripcion: [{
            required: true,
            message: 'Ingrese una descripción del usuario',
            trigger: 'change'
        }],
    },
    dataGenero: [{
            idgenero: 1,
            nombre: 'Hombre'
        },
        {
            idgenero: 2,
            nombre: 'Mujer'
        }
    ]
};