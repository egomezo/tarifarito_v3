/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getListProcesos(iddependencia) {
    return request({
        url: '/procesos',
        method: 'get',
        params: { 'dependencia': iddependencia }
    });
}

export function getProceso(id) {
    return request({
        url: '/proceso/detalle',
        method: 'get',
        params: { 'idproceso': id }
    });
}

export function createProceso(data) {
    return request({
        url: '/procesos',
        method: 'post',
        data
    });
}

export function updateProcesoUsuario(data) {
    return request({
        url: '/procesos/usuarioupdate',
        method: 'put',
        data: data
    });
}

export function updateProceso(data) {
    return request({
        url: '/procesos/update',
        method: 'put',
        data: data
    });
}

export function deleteProceso(id) {
    return request({
        url: '/procesos',
        method: 'delete',
        params: { 'idProceso': id }
    });
}