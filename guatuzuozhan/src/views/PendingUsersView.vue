<script setup>
import { onMounted, ref } from 'vue'
import { actionUser, listUsers } from '@/api/admin'
import { getApiError } from '@/api/http'
const users=ref([]);const loading=ref(false);const error=ref('')
async function load(){loading.value=true;try{users.value=(await listUsers({register_status:'pending'})).data.results||[]}catch(e){error.value=getApiError(e,'注册申请加载失败')}finally{loading.value=false}}
async function act(u,a){let remark='';if(a==='reject'){remark=prompt('请输入驳回原因')||'';if(!remark)return}if(!confirm(a==='approve'?'确认通过？':'确认驳回？'))return;try{await actionUser(u.id,a,{remark});load()}catch(e){error.value=getApiError(e,'审核操作失败')}}onMounted(load)
</script>
<template><section class="panel"><p class="eyebrow">REVIEW QUEUE</p><h1>注册申请审核</h1><p v-if="loading" class="muted">加载中…</p><p v-if="error" class="error">{{error}}</p><p v-if="!loading&&!users.length" class="muted">暂无待审核申请</p><div v-else class="table-wrap"><table><thead><tr><th>姓名</th><th>职位</th><th>部门</th><th>岗位</th><th>职责</th><th>操作</th></tr></thead><tbody><tr v-for="u in users" :key="u.id"><td>{{u.name}}</td><td>{{u.position}}</td><td>{{u.department?.name||'—'}}</td><td>{{u.job_title||'无'}}</td><td>{{u.responsibility||'—'}}</td><td class="actions"><button @click="act(u,'approve')">通过</button><button class="danger" @click="act(u,'reject')">驳回</button></td></tr></tbody></table></div></section></template>
