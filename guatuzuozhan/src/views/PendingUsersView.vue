<script setup>
import { onMounted, ref } from 'vue'
import { actionUser, listUsers } from '@/api/admin'
import { getApiError } from '@/api/http'
import { getPositionLabel } from '@/utils/labels'
import ConfirmModal from '@/components/ConfirmModal.vue'
const users=ref([]),loading=ref(false),error=ref('');const modal=ref({open:false,title:'',message:'',confirmText:'',run:null})
async function load(){loading.value=true;try{users.value=(await listUsers({register_status:'pending'})).data.results||[]}catch(e){error.value=getApiError(e,'注册申请加载失败')}finally{loading.value=false}}
function ask(u,a){let remark='';if(a==='reject'){remark=window.prompt('请输入驳回原因')||'';if(!remark)return}modal.value={open:true,title:a==='approve'?'确认审核通过':'确认驳回申请',message:`确定要${a==='approve'?'通过':'驳回'}用户“${u.name}”的注册申请吗？`,confirmText:a==='approve'?'审核通过':'驳回申请',run:()=>actionUser(u.id,a,{remark})}}
async function confirmModal(){const fn=modal.value.run;modal.value.open=false;try{await fn();await load()}catch(e){error.value=getApiError(e,'审核操作失败')}}onMounted(load)
</script>
<template><section class="panel"><h1>注册申请审核</h1><p v-if="loading" class="muted">加载中…</p><p v-if="error" class="error">{{error}}</p><p v-if="!loading&&!users.length" class="muted">暂无待审核申请</p><div v-else class="table-wrap"><table><thead><tr><th>姓名</th><th>职位</th><th>部门</th><th>岗位</th><th>操作</th></tr></thead><tbody><tr v-for="u in users" :key="u.id"><td>{{u.name}}</td><td>{{getPositionLabel(u.position)}}</td><td>{{u.department?.name||'—'}}</td><td>{{u.job_title||'无'}}</td><td class="actions"><button @click="ask(u,'approve')">审核通过</button><button class="danger" @click="ask(u,'reject')">驳回申请</button></td></tr></tbody></table></div><ConfirmModal :open="modal.open" :title="modal.title" :message="modal.message" :confirm-text="modal.confirmText" @confirm="confirmModal" @cancel="modal.open=false" /></section></template>
