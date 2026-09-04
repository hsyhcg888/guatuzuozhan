import axios from 'axios'

export function getApiError(error, fallback = '请求失败，请稍后重试') {
  const status = error.response?.status
  const data = error.response?.data
  if (import.meta.env.DEV) console.error('[API]', status || 'NETWORK', data || error.message)
  if (!error.response) return '无法连接后端服务，请确认 Django 已启动'
  if (status === 400) {
    const text = Object.values(data || {}).flat().filter((v) => typeof v === 'string').join('；')
    if (text.includes('已存在')) return '该姓名已存在，无法注册'
    if (text.includes('两次') || text.includes('confirm')) return '两次输入的密码不一致'
    return text.replace(/<[^>]*>/g, '').slice(0, 120) || '提交信息不符合要求，请检查表单'
  }
  if (status === 401) return '登录信息错误'
  if (status === 403) return '当前账号没有权限'
  if (status === 404) return '接口不存在，请检查后端服务'
  if (status >= 500) return '服务器出现异常，请查看后端日志'
  return fallback
}
const http = axios.create({ baseURL: 'http://127.0.0.1:8000/api', timeout: 10000 })
http.interceptors.request.use((config) => { const token = localStorage.getItem('access_token'); if (token) config.headers.Authorization = `Bearer ${token}`; return config })
http.interceptors.response.use((response) => response, (error) => { if (error.response?.status === 401) { localStorage.removeItem('access_token'); localStorage.removeItem('refresh_token'); localStorage.removeItem('auth_user'); if (location.pathname !== '/login') location.href = '/login' } return Promise.reject(error) })
export default http
