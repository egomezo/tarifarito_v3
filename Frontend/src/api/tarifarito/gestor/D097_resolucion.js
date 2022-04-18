/* jshint esversion: 6 */
/* eslint-disable */
import request from '../../../utils/request';

export function getD097ResList() {
    return request({
        url: 'g_resolucion',
        method: 'get'
    });
}

export function getD097Res(query) {
    return request({
        url: `g_resolucion/${query}`,
        method: 'get'
    });
}

export function postD097Res(model) {
    return request({
        url: `g_resolucion`,
        method: 'post',
        params: { 'params': model }
    });
}

export function putD097Res(anio, empresa, model) {
    return request({
        url: `g_resolucion/${anio}`,
        method: 'put',
        params: { 'params': model, 'empresa': empresa }
    });
}

export function deleteD097Res(query) {
    return request({
        url: `g_resolucion/${query}`,
        method: 'delete'
    });
}