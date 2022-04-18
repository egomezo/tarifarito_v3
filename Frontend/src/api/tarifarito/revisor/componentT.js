/* jshint esversion: 6 */
/* eslint-disable */
import request from '../../../utils/request';

export function getCpteTValues(data) {
    return request({
        url: `r_componentT/${data.ano}/${data.mes}/${data.id_empresa}/${data.id_mercado}/${data.nt_prop}`,
        method: 'get'
    });
}

export function postMDBCpteT(model) {
    return request({
        url: `r_componentT`,
        method: 'post',
        params: { 'params': model }
    });
}