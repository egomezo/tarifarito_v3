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

export function getArea(id) {
    return request({
        url: '/area',
        method: 'get',
        params: { 'iddependencia': id }
    });
}