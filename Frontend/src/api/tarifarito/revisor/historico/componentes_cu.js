/* jshint esversion: 6 */
/* eslint-disable */
import request from '../../../../utils/request';

export function getComponentes(anio, mes, empresa, mercado) {
    return request({
        url: `r_componentesMDB/${anio}/${mes}/${empresa}/${mercado}`,
        method: 'get'
    });
}

export function getDataComponente(anio, mes, empresa, mercado, cpte, ntprop) {
    return request({
        url: `r_componentesMDB/${anio}/${mes}/${empresa}/${mercado}/${cpte}/${ntprop}`,
        method: 'get'
    });
}

export function postCpte(model) {
    return request({
        url: 'r_componentesMDB',
        method: 'post',
        params: { 'params': model }
    });
}