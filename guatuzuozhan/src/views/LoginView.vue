<script setup>
import { reactive, ref } from 'vue'; import { useRouter } from 'vue-router'; import { useAuthStore } from '@/stores/auth'
const form=reactive({name:'',password:''}); const error=ref(''); const loading=ref(false); const router=useRouter(); const auth=useAuthStore()
async function submit(){error.value='';loading.value=true;try{await auth.login(form);router.push('/home')}catch(e){error.value=e.response?.data?.detail||'登录失败，请检查网络'}finally{loading.value=false}}
</script>
<template><section class="panel auth-panel"><p class="eyebrow">SECURE ACCESS / 01</p><h1>作战平台</h1><p class="muted">统一身份认证中心</p><form class="form-grid" @submit.prevent="submit"><label>姓名<input v-model.trim="form.name" required autocomplete="username" /></label><label>密码<input v-model="form.password" type="password" required autocomplete="current-password" /></label><p v-if="error" class="error">{{ error }}</p><button :disabled="loading">{{ loading?'验证中…':'登录系统' }}</button><RouterLink to="/register">提交注册申请 →</RouterLink></form></section></template>
