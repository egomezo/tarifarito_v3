/* jshint esversion: 6 */
/* eslint-disable */
import request from '../../utils/request';

export function getSUIMercados(empresa) {
    return request({
        url: `empresa_mercado/${empresa}`,
        method: 'get'
    });
}