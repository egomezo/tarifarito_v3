/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getListNorma() {
    return request({
        url: '/norma',
        method: 'get'
    });
}

export function getSearchNorma(param) {
    return request({
        url: '/norma_param',
        method: 'get',
        params: { 'query': param }
    });
}

export function createNorma(data) {
    return request({
        url: '/norma',
        method: 'post',
        data
    });
}

export function updateNorma(data) {
    return request({
        url: '/norma',
        method: 'put',
        data: data
    });
}

export function deleteNorma(data) {
    return request({
        url: '/norma',
        method: 'delete',
        data
    });
}