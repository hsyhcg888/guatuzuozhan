<script setup>
import { onMounted, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { departments, register } from '@/api/auth'
import { getApiError } from '@/api/http'
const positions = [['general_manager', '总经理'], ['deputy_general_manager', '副总经理'], ['section_chief', '科长'], ['deputy_section_chief', '副科长'], ['team_leader', '组长'], ['member', '组员']]
const form = reactive({ name: '', password: '', confirm_password: '', position: 'member', department_id: '', job_title: '', responsibility: '' })
const list = ref([]); const error = ref(''); const success = ref(''); const loading = ref(false); const router = useRouter()
onMounted(async () => { try { list.value = (await departments()).data } catch (e) { error.value = getApiError(e, '部门加载失败') } })
async function submit() { error.value = ''; success.value = ''; if (!form.name || !form.password || !form.confirm_password || !form.department_id) { error.value = '请填写完整注册信息'; return } if (form.password !== form.confirm_password) { error.value = '两次输入的密码不一致'; return } loading.value = true; try { await register(form); success.value = '注册申请已提交，请等待系统管理员审核'; setTimeout(() => router.push('/login'), 1500) } catch (e) { error.value = getApiError(e) } finally { loading.value = false } }
</script>
<template><section class="panel"><p class="eyebrow">APPLICATION / 02</p><h1>注册申请</h1><form class="form-grid" @submit.prevent="submit"><label>姓名<input v-model.trim="form.name" required /></label><label>密码<input v-model="form.password" type="password" required minlength="6" /></label><label>确认密码<input v-model="form.confirm_password" type="password" required /></label><label>职位<select v-model="form.position"><option v-for="p in positions" :key="p[0]" :value="p[0]">{{ p[1] }}</option></select></label><label>部门<select v-model="form.department_id" required><option value="" disabled>请选择部门</option><option v-for="d in list" :key="d.id" :value="d.id">{{ d.name }}</option></select></label><label>用户岗位<input v-model="form.job_title" placeholder="可填写无" /></label><label>职责描述<textarea v-model="form.responsibility" rows="4" /></label><p v-if="error" class="error">{{ error }}</p><p v-if="success" class="success">{{ success }}</p><button :disabled="loading">{{ loading ? '提交中…' : '提交申请' }}</button><RouterLink to="/login">返回登录</RouterLink></form></section></template>
