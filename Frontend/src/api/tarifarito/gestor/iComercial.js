/* jshint esversion: 6 */
/* eslint-disable */
import request from '../../../utils/request';

export function getIComercialList() {
    return request({
        url: 'g_icomercial',
        method: 'get'
    });
}

export function getIComercial(query) {
    return request({
        url: `g_icomercial/${query}`,
        method: 'get'
    });
}

export function postIComercial(model) {
    return request({
        url: `g_icomercial`,
        method: 'post',
        params: { 'params': model }
    });
}

export function putIComercial(anio, empresa, model) {
    return request({
        url: `g_icomercial/${anio}`,
        method: 'put',
        params: { 'params': model, 'empresa': empresa }
    });
}

export function deleteIComercial(query) {
    return request({
        url: `g_icomercial/${query}`,
        method: 'delete'
    });
}