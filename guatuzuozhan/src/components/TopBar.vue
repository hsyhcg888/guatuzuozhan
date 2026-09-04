<script setup>
import { useRoute } from 'vue-router';import { useAuthStore } from '@/stores/auth';import { getPositionLabel } from '@/utils/labels'
defineEmits(['logout']);const route=useRoute();const auth=useAuthStore();const titles={'/home':'数字化工作台','/system/users':'用户管理','/system/users/pending':'注册申请审核'}
</script>
<template><header class="topbar"><div><small>数字化指挥中心</small><h2>{{titles[route.path]||'挂图作战系统'}}</h2></div><div class="user"><div class="user-copy"><strong>{{auth.user?.name}}</strong><span>{{getPositionLabel(auth.user?.position)}} · {{auth.user?.department?.name||'未分配'}}</span></div><button @click="$emit('logout')">退出登录</button></div></header></template>
<style scoped>.topbar{height:88px;padding:0 34px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #20415d;background:#081625bb;backdrop-filter:blur(14px)}small{color:#55bde9;letter-spacing:.15em;font-size:10px}h2{margin:7px 0 0;font-size:21px}.user{display:flex;gap:18px;align-items:center}.user-copy{text-align:right}.user-copy strong,.user-copy span{display:block}.user-copy span{font-size:12px;color:#8da6bc;margin-top:5px}.user button{padding:8px 12px}@media(max-width:700px){.topbar{height:auto;min-height:88px;padding:16px}.user-copy{display:none}}
</style>
