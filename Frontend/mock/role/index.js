import Mock from 'mockjs'
import { deepClone } from '../../src/utils/index.js'
import { asyncRoutes, constantRoutes } from './routes.js'

const routes = deepClone([...constantRoutes, ...asyncRoutes])

// son los permisos del rol que se pueden modificar desde la vista -> '/permission/role' src\views\permission\role.vue
const roles = [
  {
    key: '1',
    name: 'admin',
    description: 'Realizará la administración de los usuarios (creación de usuarios, Estados y demás parámetros del aplicativo).',
    routes: routes
  },
  {
    key: '2',
    name: 'gestor',
    description: 'Gestor de datos. Realizar la actualización mes a mes de la información requerida en el proceso de verificación del CU y Tarifas, información que no podrá ser capturada a través del SUI, debido a que la fuente de información son bases de datos que no están dentro de la administración de esta entidad y a la que no se podrá acceder en línea.',
    routes: routes
  },
  {
    key: '3',
    name: 'revisor',
    description: '-	Verificar la correcta aplicación del cálculo del Costo Unitario de Prestación del Servicio – CU. ' +
                 '-	Verificar la correcta aplicación del cálculo de los porcentajes de subsidios y contribución (tarifas). ' +
                 '-	Gestionar las solicitudes (aclaraciones y/o justificaciones) que se deriven de los procesos de verificación. ',
    routes: routes
  },
  {
    key: '4',
    name: 'aprobador',
    description: '-	Realizar la verificación de las novedades e indicar las acciones a tomar según los resultados obtenidos por parte de los profesionales en su rol de revisor. ' +
                 '-	Realizar las solicitudes de creación o modificación de usuarios y/o permisos cuando lo considere necesario.',
    routes: routes
  },
  {
    key: '5',
    name: 'consultor',
    description: 'Este rol no tendrá asignadas actividades, esto debido a que es un perfil netamente de consulta.',
    routes: routes
  },
  // {
  //   key: 'editor',
  //   name: 'editor',
  //   description: 'Normal Editor. Can see all pages except permission page',
  //   routes: routes.filter(i => i.path !== '/permission')// just a mock
  // },
  // {
  //   key: 'visitor',
  //   name: 'visitor',
  //   description: 'Just a visitor. Can only see the home page and the document page',
  //   routes: [{
  //     path: '',
  //     redirect: 'dashboard',
  //     children: [
  //       {
  //         path: 'dashboard',
  //         name: 'Dashboard',
  //         meta: { title: 'dashboard', icon: 'dashboard' }
  //       }
  //     ]
  //   }]
  // }
]

export default [
  // mock get all routes form server
  {
    url: '/routes',
    type: 'get',
    response: _ => {
      return {
        code: 20000,
        data: routes
      }
    }
  },

  // mock get all roles form server
  {
    url: '/roles',
    type: 'get',
    response: _ => {
      return {
        code: 20000,
        data: roles
      }
    }
  },

  // add role
  {
    url: '/role',
    type: 'post',
    response: {
      code: 20000,
      data: {
        key: Mock.mock('@integer(300, 5000)')
      }
    }
  },

  // update role
  {
    url: '/role/[A-Za-z0-9]',
    type: 'put',
    response: {
      code: 20000,
      data: {
        status: 'success'
      }
    }
  },

  // delete role
  {
    url: '/role/[A-Za-z0-9]',
    type: 'delete',
    response: {
      code: 20000,
      data: {
        status: 'success'
      }
    }
  }
]
