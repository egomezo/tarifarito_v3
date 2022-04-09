/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getListProcesosEmpresa(idservicio, iddependencia) {
    return request({
        url: '/procesos_empresa',
        method: 'get',
        params: { 'idservicio': idservicio, 'iddependencia': iddependencia }
    });
}

export function getListProcesosCausal(idservicio) {
    return request({
        url: '/procesos_causal',
        method: 'get',
        params: { 'idservicio': idservicio }
    });
}

export function getListProcesosEstado(idservicio, iddependencia) {
    return request({
        url: '/procesos_estado',
        method: 'get',
        params: { 'idservicio': idservicio, 'iddependencia': iddependencia }
    });
}

export function getListProcesosUsuario(idservicio, iddependencia) {
    return request({
        url: '/procesos_usuario',
        method: 'get',
        params: { 'idservicio': idservicio, 'iddependencia': iddependencia }
    });
}

export function getListCantidadProcesos(idservicio, iddependencia) {
    return request({
        url: '/cantidad_procesos',
        method: 'get',
        params: { 'idservicio': idservicio, 'iddependencia': iddependencia }
    });
}