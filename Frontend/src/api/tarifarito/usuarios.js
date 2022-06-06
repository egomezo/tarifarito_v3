/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getListUsuarios(iddependencia) {
    return request({
        url: '/usuarios',
        method: 'get',
        params: { 'dependencia': iddependencia }
    });
}

export function getListRevisores(iddependencia) {
    return request({
        url: '/revisores',
        method: 'get',
        params: { 'dependencia': iddependencia }
    });
}

export function getAllUsuarios(iddependencia) {
    return request({
        url: '/lista_usuarios',
        method: 'get',
        params: { 'dependencia': iddependencia }
    });
}

export function getListNicknames() {
    return request({
        url: '/nicknames',
        method: 'get'
    });
}

export function getListRol() {
    return request({
        url: '/rol',
        method: 'get'
    });
}

export function getUsuario(id) {
    return request({
        url: '/usuario/detalle',
        method: 'get',
        params: { 'idusuario': id }
    });
}

export function createUsuario(data) {
    return request({
        url: '/usuarios',
        method: 'post',
        data
    });
}

export function updateUsuario(data) {
    data.api = process.env.VUE_APP_BASE_API;
    return request({
        url: '/usuarios',
        method: 'put',
        data
    });
}

export function deleteUsuario(id, username) {
    return request({
        url: '/usuarios',
        method: 'delete',
        params: { 'idusuario': id, 'nickname': username }
    });
}

export function createUser(data) {
    data.api = process.env.VUE_APP_BASE_API;
    return request({
        url: '/user/create',
        method: 'post',
        data
    });
}