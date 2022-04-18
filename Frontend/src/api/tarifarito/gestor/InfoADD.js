/* jshint esversion: 6 */
/* eslint-disable */
import request from '../../../utils/request';

export function getInfoADDList() {
    return request({
        url: 'g_infoADD',
        method: 'get'
    });
}

export function getInfoADD(query) {
    return request({
        url: `g_infoADD/${query}`,
        method: 'get'
    });
}

export function postInfoADD(model) {
    return request({
        url: `g_infoADD`,
        method: 'post',
        params: { 'params': model }
    });
}

export function putInfoADD(mercado, model) {
    return request({
        url: `g_infoADD`,
        method: 'put',
        params: { 'mercado': mercado, 'params': model }
    });
}

export function deleteInfoADD() {
    return request({
        url: `g_infoADD`,
        method: 'delete',
        params: { 'mercado': mercado }
    });
}