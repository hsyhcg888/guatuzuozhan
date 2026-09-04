<script setup>
import { onBeforeUnmount, onMounted } from 'vue'
defineProps({ open: Boolean, title: String, message: String, confirmText: { type: String, default: '&#x786e;&#x5b9a;' } })
const emit = defineEmits(['confirm', 'cancel'])
function keydown(e) { if (e.key === 'Escape') emit('cancel') }
onMounted(() => window.addEventListener('keydown', keydown)); onBeforeUnmount(() => window.removeEventListener('keydown', keydown))
</script>
<template><Teleport to="body"><div v-if="open" class="modal-backdrop" @click.self="emit('cancel')"><div class="modal-card" role="dialog" aria-modal="true"><h2>{{ title }}</h2><p>{{ message }}</p><div class="modal-actions"><button @click="emit('cancel')">&#x53d6;&#x6d88;</button><button class="danger" @click="emit('confirm')">{{ confirmText }}</button></div></div></div></Teleport></template>
<style scoped>.modal-backdrop{position:fixed;inset:0;z-index:20;display:grid;place-items:center;background:#020914bb;backdrop-filter:blur(5px)}.modal-card{width:min(420px,calc(100vw - 32px));padding:28px;border:1px solid #3976a8;border-radius:16px;background:#0b1d31;box-shadow:0 24px 90px #000b}.modal-card h2{margin-top:0;color:#dff2ff}.modal-card p{color:#aac1d5;line-height:1.7}.modal-actions{display:flex;justify-content:flex-end;gap:10px;margin-top:24px}</style>
