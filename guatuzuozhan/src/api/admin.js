import http from './http'
export const listUsers = (params) => http.get('/admin/users/', { params })
export const createUser = (data) => http.post('/admin/users/', data)
export const updateUser = (id, data) => http.patch(`/admin/users/${id}/`, data)
export const actionUser = (id, action, data = {}) => http.post(`/admin/users/${id}/${action}/`, data)
export const deleteUser = (id) => http.delete(`/admin/users/${id}/`)
export const downloadTemplate = () => http.get('/admin/users/template/', { responseType: 'blob' })
export const importUsers = (file) => { const data = new FormData(); data.append('file', file); return http.post('/admin/users/import/', data) }
