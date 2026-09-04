<script setup>
import { ref } from 'vue'; import { useAuthStore } from '@/stores/auth'; import Sidebar from './Sidebar.vue'; import TopBar from './TopBar.vue'; import ConfirmModal from './ConfirmModal.vue'
const auth=useAuthStore();const collapsed=ref(false);const logoutOpen=ref(false);function logout(){auth.logout();logoutOpen.value=false}
</script>
<template><div class="layout"><Sidebar :collapsed="collapsed" @toggle="collapsed=!collapsed"/><div class="workspace"><TopBar @logout="logoutOpen=true"/><main class="content"><slot /></main></div><ConfirmModal :open="logoutOpen" title="确认退出登录" message="确定要退出当前账号吗？" confirm-text="确定退出" @confirm="logout" @cancel="logoutOpen=false"/></div></template>
<style scoped>.layout{display:flex;min-height:100vh}.workspace{min-width:0;flex:1}.content{max-width:1440px;margin:auto;padding:32px;animation:content-in .4s ease}@keyframes content-in{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}@media(max-width:700px){.content{padding:18px}}</style>
