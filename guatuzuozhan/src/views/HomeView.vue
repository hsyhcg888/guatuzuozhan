<script setup>
import { useAuthStore } from '@/stores/auth'
import { getPositionLabel } from '@/utils/labels'
const auth = useAuthStore()
</script>
<template><section class="panel"><p class="eyebrow">COMMAND HUB</p><h1>&#x6b22;&#x8fce;&#x56de;&#x6765;&#xff0c;{{ auth.user?.name }}</h1><p class="muted">&#x804c;&#x4f4d;&#xff1a;{{ getPositionLabel(auth.user?.position) }}　&#x90e8;&#x95e8;&#xff1a;{{ auth.user?.department?.name || '&#x672a;&#x5206;&#x914d;' }}</p><div class="cards"><div class="card"><small>&#x8eab;&#x4efd;&#x72b6;&#x6001;</small><h2>&#x5df2;&#x8ba4;&#x8bc1;</h2></div><div class="card"><small>&#x6743;&#x9650;&#x7b49;&#x7ea7;</small><h2>{{ auth.isAdmin ? '&#x7cfb;&#x7edf;&#x7ba1;&#x7406;&#x5458;' : '&#x666e;&#x901a;&#x7528;&#x6237;' }}</h2></div></div></section></template>
