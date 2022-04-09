/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getNotificacionProceso(id) {
    return request({
        url: '/notificacion_proceso',
        method: 'get',
        params: { 'idproceso': id }
    });
}

export function createNotificacion(data) {
    return request({
        url: '/notificacion',
        method: 'post',
        data
    });
}

export function updateNotificacion(data) {
    return request({
        url: '/notificacion',
        method: 'put',
        data: data
    });
}

export function deleteNotificacion(id) {
    return request({
        url: '/notificacion',
        method: 'delete',
        params: { 'idnotificacion': id }
    });
}