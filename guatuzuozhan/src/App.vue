<script setup>
import { useAuthStore } from '@/stores/auth'
import AppLayout from '@/components/AppLayout.vue'
import TechBackground from '@/components/TechBackground.vue'
const auth = useAuthStore()
</script>
<template><TechBackground /><AppLayout v-if="auth.user"><RouterView /></AppLayout><main v-else class="public-shell"><RouterView /></main></template>
<style>
:root{font-family:Inter,system-ui,sans-serif;color:#e8f1ff;background:#050d18}*{box-sizing:border-box}body{margin:0;min-width:320px;background:linear-gradient(135deg,#050d18,#091b2d 55%,#10152f);min-height:100vh}.public-shell{min-height:100vh;display:grid;place-items:center;padding:24px}.panel{background:#0b1c30dd;border:1px solid #315879;border-radius:18px;padding:28px;box-shadow:0 20px 60px #0006;animation:rise .45s ease both}.form-grid{display:grid;gap:15px;max-width:520px}input,select,textarea{width:100%;padding:12px;border:1px solid #31516d;border-radius:8px;background:#081522;color:#fff}label{display:grid;gap:6px;color:#a9c6df}.error{color:#ff8f9d}.success{color:#6ef0b0}.muted{color:#8da6bc}.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px}.card{padding:22px;border:1px solid #244664;border-radius:14px;background:#10263d}.table-wrap{overflow:auto}table{width:100%;border-collapse:collapse}th,td{padding:12px;text-align:left;border-bottom:1px solid #23405d;white-space:nowrap}.actions{display:flex;gap:8px;flex-wrap:wrap}button{border:1px solid #3a91db;background:#0d3154;color:#fff;border-radius:8px;padding:10px 16px;cursor:pointer}button:hover{box-shadow:0 0 18px #2ea9ff66}button:disabled{opacity:.55;cursor:not-allowed}.danger{border-color:#c35363;background:#522331}.eyebrow{color:#62c8ff;letter-spacing:.18em}@keyframes rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}@media(max-width:700px){.public-shell{padding:14px}}
</style>
