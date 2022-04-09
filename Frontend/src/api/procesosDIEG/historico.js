/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request';

// -------------------------------------------------------
// ----------- OPERACIONES HISTORICO GENERAL -------------
// -------------------------------------------------------

export function getAniosHistorico() {
    return request({
        url: '/historico/anios',
        method: 'get'
    });
}

export function getHistoricoGeneral(data) {
    return request({
        url: '/historico_general',
        method: 'post',
        data
    });
}

export function createHistoricoGeneral(data) {
    return request({
        url: '/historico_general_guardar',
        method: 'post',
        data
    });
}

// -------------------------------------------------------
// ----------- OPERACIONES HISTORICO ESPECIFICO ----------
// -------------------------------------------------------

export function getHistoricoEspecifico(data) {
    return request({
        url: '/historico_especifico',
        method: 'post',
        data
    });
}

export function createHistoricoEspecifico(data) {
    return request({
        url: '/historico_especifico_guardar',
        method: 'post',
        data
    });
}