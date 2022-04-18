/* jshint esversion: 6 */
import request from '../utils/request'

export function getUserList() {
  return request({
    url: 'users',
    method: 'get'
  })
}

export function getUser(query) {
  return request({
    url: `users/${query}`,
    method: 'get',
    params: { 'nombre': query }
  })
}

export function postUser(query) {
  return request({
    url: `users/${query}`,
    method: 'post'
  })
}

export function putUser(query) {
  return request({
    url: `users/${query}`,
    method: 'put'
  })
}

export function deleteUser(query) {
  return request({
    url: `users/${query}`,
    method: 'delete'
  })
}
