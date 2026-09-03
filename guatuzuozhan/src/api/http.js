import axios from 'axios'
const http = axios.create({ baseURL: 'http://127.0.0.1:8000/api', timeout: 10000 })
http.interceptors.request.use((config) => { const token = localStorage.getItem('access_token'); if (token) config.headers.Authorization = `Bearer ${token}`; return config })
http.interceptors.response.use((r) => r, (e) => { if (e.response?.status === 401) { localStorage.clear(); if (location.pathname !== '/login') location.href = '/login' } return Promise.reject(e) })
export default http
