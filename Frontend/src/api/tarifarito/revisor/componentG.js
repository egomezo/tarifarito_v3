/* jshint esversion: 6 */
/* eslint-disable */
import request from '../../../utils/request';

export function getCpteGValues(data) {
    return request({
        url: `r_componentg/${data.ano}/${data.mes}/${data.id_empresa}/${data.id_mercado}`,
        method: 'get'
    });
}

export function postMDBCpteG(model) {
    return request({
        url: `r_componentg`,
        method: 'post',
        params: { 'params': model }
    });
}