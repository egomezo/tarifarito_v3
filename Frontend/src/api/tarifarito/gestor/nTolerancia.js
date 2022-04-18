/* jshint esversion: 6 */
/* eslint-disable */
import request from '../../../utils/request';

export function getNToleranciaList() {
    return request({
        url: 'g_ntolerancia',
        method: 'get'
    });
}

export function getNTolerancia(query) {
    return request({
        url: `g_ntolerancia/${query}`,
        method: 'get'
    });
}

export function getNToleranciaMes(ano, mes) {
    return request({
        url: `g_ntolerancia/${ano}/${mes}`,
        method: 'get'
    });
}

export function postNTolerancia(model) {
    return request({
        url: `g_ntolerancia`,
        method: 'post',
        params: { 'params': model }
    });
}

export function putNTolerancia(anio, mes, model) {
    return request({
        url: `g_ntolerancia/${anio}`,
        method: 'put',
        params: { 'params': model, 'mes': mes }
    });
}

export function deleteNTolerancia(query) {
    return request({
        url: `g_ntolerancia/${query}`,
        method: 'delete'
    });
}