/* jshint esversion: 6 */
/* eslint-disable */
const tokens = {
    admin: {
        token: 'admin-token'
    },
    gestor: {
        token: 'gestor-token'
    },
    revisor: {
        token: 'revisor-token'
    },
    aprobador: {
        token: 'aprobador-token'
    },
    consultor: {
        token: 'consultor-token'
    },
    editor: {
        token: 'editor-token'
    },
    visitor: {
        token: 'visitor-token'
    },
    juan: {
        token: 'juan-token'
    },
    diego: {
        token: 'gestor-token'
    }
}

const users = {
    'admin-token': {
        roles: ['admin'],
        introduction: 'I am a super administrator',
        avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        name: 'Administrador'
    },
    'gestor-token': {
        roles: ['gestor'],
        introduction: 'Soy un Gestor de datos',
        avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        name: 'Gestor de Datos'
    },
    'revisor-token': {
        roles: ['revisor'],
        introduction: 'Soy un revisor',
        avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        name: 'Revisor'
    },
    'aprobador-token': {
        roles: ['aprobador'],
        introduction: 'Soy un aprobador',
        avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        name: 'Aprobador'
    },
    'consultor-token': {
        roles: ['consultor'],
        introduction: 'Soy un consultor',
        avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        name: 'Consultor'
    },
    'editor-token': {
        roles: ['editor'],
        introduction: 'I am an editor',
        avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        name: 'Normal Editor'
    },
    'visitor-token': {
        roles: ['visitor'],
        introduction: 'I am an visitor',
        avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        name: 'Normal Visitor'
    },
    'juan-token': {
        roles: ['visitor'],
        introduction: 'I am an visitor',
        avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        name: 'Normal juan'
    }
}

export default [
    // user login
    {
        url: '/user/login',
        type: 'post',
        response: config => {
            const { username } = config.body
            const token = tokens[username]

            console.log('config', config);

            // mock error
            if (!token) {
                return {
                    code: 60204,
                    message: 'Usuario y contraseña incorrectos.'
                }
            }

            return {
                code: 20000,
                data: token
            }
        }
    },

    // get user info
    {
        url: '/user/info\.*',
        type: 'get',
        response: config => {
            const { token } = config.query
            const info = users[token]

            // mock error
            if (!info) {
                return {
                    code: 50008,
                    message: 'Error de inicio de sesión, no se pueden obtener los detalles del usuario.'
                }
            }

            return {
                code: 20000,
                data: info
            }
        }
    },

    // user logout
    {
        url: '/user/logout',
        type: 'post',
        response: _ => {
            return {
                code: 20000,
                data: 'success'
            }
        }
    }
]