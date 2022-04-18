/* jshint esversion: 6 */
/* eslint-disable */
import request from '../../../../utils/request';

export function getTarifas(anio, mes, empresa) {
    return request({
        url: `r_tarifas/${anio}/${mes}/${empresa}`,
        method: 'get'
    });
}