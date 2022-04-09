/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

export function getListCausal() {
    return request({
        url: '/causal',
        method: 'get'
    });
}

export function getCausalProceso(id) {
    return request({
        url: '/causal_proceso',
        method: 'get',
        params: { 'idProceso': id }
    });
}

export function getCantidadCausalProceso(id) {
    return request({
        url: '/cantidad_causal_proceso',
        method: 'get',
        params: { 'idproceso': id }
    });
}

export function createCausal(data) {
    return request({
        url: '/causal',
        method: 'post',
        data
    });
}

export function updateCausal(data) {
    return request({
        url: '/causal',
        method: 'put',
        data: data
    });
}

export function deleteCausal(data) {
    return request({
        url: '/causal',
        method: 'delete',
        data
    });
}