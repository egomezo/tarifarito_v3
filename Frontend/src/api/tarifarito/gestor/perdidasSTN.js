/* jshint esversion: 6 */
/* eslint-disable */
import request from '../../../utils/request';

export function getPerdidasSTNList() {
    return request({
        url: 'g_perdidasSTN',
        method: 'get'
    });
}

export function getPerdidasSTN(query) {
    return request({
        url: `g_perdidasSTN/${query}`,
        method: 'get'
    });
}

export function postPerdidasSTN(model) {
    return request({
        url: `g_perdidasSTN`,
        method: 'post',
        params: { 'params': model }
    });
}

export function putPerdidasSTN(anio, mercado, model) {
    return request({
        url: `g_perdidasSTN/${anio}`,
        method: 'put',
        params: { 'params': model, 'mercado': mercado }
    });
}

export function deletePerdidasSTN(query) {
    return request({
        url: `g_perdidasSTN/${query}`,
        method: 'delete'
    });
}