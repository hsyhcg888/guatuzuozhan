<script setup>
import { useAuthStore } from '@/stores/auth'
const auth = useAuthStore()
</script>
<template>
  <div class="app-shell">
    <header v-if="auth.user"><strong>GUATU · 作战平台</strong><nav><RouterLink to="/home">首页</RouterLink><RouterLink v-if="auth.isAdmin" to="/system/users">系统管理中心</RouterLink><RouterLink v-if="auth.isAdmin" to="/system/users/pending">注册审核</RouterLink><button @click="auth.logout(); $router.push('/login')">退出</button></nav></header>
    <main><RouterView /></main>
  </div>
</template>
<style>
:root{font-family:Inter,system-ui,sans-serif;color:#e8f1ff;background:#07111f}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 80% 0%,#123968 0,#07111f 45%);min-height:100vh}.app-shell{min-height:100vh}header{height:68px;padding:0 5%;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #23405d;background:#091827dd;backdrop-filter:blur(12px)}nav{display:flex;gap:20px;align-items:center}a{color:#8fc9ff;text-decoration:none}button,.button{border:1px solid #3a91db;background:#0d3154;color:#fff;border-radius:8px;padding:10px 16px;cursor:pointer}button:disabled{opacity:.55;cursor:not-allowed}main{max-width:1200px;margin:auto;padding:48px 24px}.panel{background:#0b1c30dd;border:1px solid #244664;border-radius:18px;padding:28px;box-shadow:0 20px 60px #0005}.form-grid{display:grid;gap:15px;max-width:520px}input,select,textarea{width:100%;padding:12px;border:1px solid #31516d;border-radius:8px;background:#081522;color:#fff}label{display:grid;gap:6px;color:#a9c6df}.error{color:#ff8f9d}.success{color:#6ef0b0}.muted{color:#8da6bc}.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px}.card{padding:22px;border:1px solid #244664;border-radius:14px;background:#10263d}.table-wrap{overflow:auto}table{width:100%;border-collapse:collapse}th,td{padding:12px;text-align:left;border-bottom:1px solid #23405d;white-space:nowrap}.actions{display:flex;gap:8px;flex-wrap:wrap}.danger{border-color:#c35363;background:#522331}.eyebrow{color:#62c8ff;letter-spacing:.18em}@media(max-width:700px){header{height:auto;padding:18px;gap:12px;align-items:flex-start}nav{flex-wrap:wrap;justify-content:flex-end}main{padding:24px 14px}}
</style>
