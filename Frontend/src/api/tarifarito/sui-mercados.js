/* jshint esversion: 6 */
/* eslint-disable */
import request from '../../utils/request';

export function getSUIMercadosList() {
    return request({
        url: 'mercados',
        method: 'get'
    });
}

export function getSUIMercados(query) {
    return request({
        url: `mercados/${query}`,
        method: 'get'
    });
}