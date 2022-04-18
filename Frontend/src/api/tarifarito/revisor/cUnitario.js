/* jshint esversion: 6 */
/* eslint-disable */
import request from '../../../utils/request';

export function getCUnitarioList(anio, mes) {
    return request({
        url: `r_cunitario/${anio}/${mes}`,
        method: 'get'
    });
}

export function getCUnitarioEmpresa(anio, mes, empresa) {
    return request({
        url: `r_cunitario/${anio}/${mes}/${empresa}`,
        method: 'get'
    });
}