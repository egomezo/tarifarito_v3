/* jshint esversion: 6 */
/* eslint-disable */
import { login, logout, getInfo } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'
import router, { resetRouter } from '@/router'

const state = {
    token: getToken(),
    name: '',
    avatar: '',
    introduction: '',
    roles: [],
    usuario: '',
    privilegio: '',
    dependencia: '',
    idusuario: '',
    keyaccess: ''
};

const mutations = {
    SET_TOKEN: (state, token) => {
        state.token = token;
    },
    SET_INTRODUCTION: (state, introduction) => {
        state.introduction = introduction;
    },
    SET_NAME: (state, name) => {
        state.name = name;
    },
    SET_AVATAR: (state, avatar) => {
        state.avatar = avatar;
    },
    SET_ROLES: (state, roles) => {
        state.roles = roles;
    },
    SET_USERNAME: (state, usuario) => {
        state.usuario = usuario;
    },
    SET_PRIVILEGIO: (state, privilegio) => {
        state.privilegio = privilegio;
    },
    SET_KEYACCESS: (state, keyaccess) => {
        state.keyaccess = keyaccess;
    },
    SET_DEPENDENCIA: (state, dependencia) => {
        state.dependencia = dependencia;
    },
    SET_IDUSUARIO: (state, idusuario) => {
        state.idusuario = idusuario;
    }
}

const actions = {
    // user login
    login({ commit }, userInfo) {
        return new Promise((resolve, reject) => {
            // console.log('userInfo :>> ', userInfo)
            login(userInfo).then(response => {
                const { data } = response;
                commit('SET_TOKEN', data.token)
                setToken(data.token)
                resolve()
            }).catch(error => {
                reject(error)
            })
        })
    },

    // get user info
    getInfo({ commit, state }) {
        return new Promise((resolve, reject) => {
            getInfo({ token: state.token, loginGestor: JSON.parse(window.localStorage.getItem('login_gestor')), api: process.env.VUE_APP_GESTOR_API }).then(response => {
                // console.log('get info! token :>> ', state.token)
                // console.log('response - store - user - getinfo -> ', JSON.stringify(response));
                const { data } = response

                // console.log('data :>> ', data)

                if (!data) {
                    reject('Error de verificación, inicie sesión de nuevo.')
                }

                const { roles, name, avatar, introduction, usuario, privilegio, dependencia, idusuario, token, publicKey } = data

                // roles must be a non-empty array
                if (!roles || roles.length <= 0) {
                    reject('getInfo: roles must be a non-null array!')
                }

                commit('SET_ROLES', roles)
                commit('SET_NAME', name)
                commit('SET_AVATAR', avatar)
                commit('SET_INTRODUCTION', introduction)
                commit('SET_USERNAME', usuario)
                commit('SET_PRIVILEGIO', privilegio)
                commit('SET_DEPENDENCIA', dependencia)
                commit('SET_IDUSUARIO', idusuario)
                commit('SET_KEYACCESS', publicKey)
                commit('SET_TOKEN', token)
                resolve(data)
            }).catch(error => {
                reject(error)
            })
        })
    },

    // user logout
    logout({ commit, state }) {
        return new Promise((resolve, reject) => {
            logout(state.token).then((response) => {
                // console.log('Response LOGOUT --> ', response);
                commit('SET_TOKEN', '')
                // commit('SET_PUBLICKEY', '')
                commit('SET_ROLES', [])
                removeToken()
                resetRouter()
                resolve()
            }).catch(error => {
                reject(error)
            })
        })
    },

    // remove token
    resetToken({ commit }) {
        return new Promise(resolve => {
            commit('SET_TOKEN', '')
            // commit('SET_PUBLICKEY', '')
            commit('SET_ROLES', [])
            removeToken()
            resolve()
        })
    },

    // dynamically modify permissions
    changeRoles({ commit, dispatch }) {
        return new Promise(async resolve => {
            const { roles } = await dispatch('getInfo')

            resetRouter()

            // generate accessible routes map based on roles
            const accessRoutes = await dispatch('permission/generateRoutes', roles, { root: true })

            // dynamically add accessible routes
            router.addRoutes(accessRoutes)

            // reset visited views and cached views
            // dispatch('tagsView/delAllViews', null, { root: true })

            resolve()
        })
    }
}

export default {
    namespaced: true,
    state,
    mutations,
    actions
}