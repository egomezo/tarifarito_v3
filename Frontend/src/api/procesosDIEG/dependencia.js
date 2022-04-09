/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getDependencia(id) {
    return request({
        url: '/dependencia',
        method: 'get',
        params: { 'iddependencia': id }
    });
}