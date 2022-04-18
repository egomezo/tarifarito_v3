/* jshint esversion: 6 */
/* eslint-disable */
import request from '../../utils/request';

export function getSUIEmpresasList() {
    return request({
        url: 'empresas',
        method: 'get'
    });
}

export function getSUIEmpresas(query) {
    return request({
        url: `empresas/${query}`,
        method: 'get'
    });
}