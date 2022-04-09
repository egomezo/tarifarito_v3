/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getListSubCausal(param) {
    return request({
        url: '/subcausal',
        method: 'get',
        params: { 'idcausal': param }
    });
}

export function createSubCausal(data) {
    return request({
        url: '/subcausal',
        method: 'post',
        data
    });
}

export function updateSubCausal(data) {
    return request({
        url: '/subcausal',
        method: 'put',
        data: data
    });
}

export function deleteSubCausal(data) {
    return request({
        url: '/subcausal',
        method: 'delete',
        data
    });
}