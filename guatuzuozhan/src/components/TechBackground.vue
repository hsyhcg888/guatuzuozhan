<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'

const cursor = ref({ x: -200, y: -200 })
const glowVisible = ref(false)
const effects = ref([])
let frame = 0
let targetX = -200
let targetY = -200
let currentX = -200
let currentY = -200
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)')

function animateCursor() {
  currentX += (targetX - currentX) * 0.12
  currentY += (targetY - currentY) * 0.12
  cursor.value = { x: currentX, y: currentY }
  frame = requestAnimationFrame(animateCursor)
}

function move(event) {
  if (reducedMotion.matches) return
  const target = event.target instanceof Element ? event.target : null
  glowVisible.value = !target?.closest('[data-no-cursor-glow], input, textarea, select, button, a, label, form, .panel, .card, .sidebar, .topbar, table, .modal-backdrop')
  if (glowVisible.value) { targetX = event.clientX; targetY = event.clientY }
}

function isBackgroundClick(event) {
  const target = event.target
  if (!(target instanceof Element)) return false
  return !target.closest('[data-no-cursor-glow], input, textarea, select, button, a, label, form, .panel, .card, .sidebar, .topbar, table, .modal-backdrop')
}

function click(event) {
  if (reducedMotion.matches || !isBackgroundClick(event)) return
  const id = `${Date.now()}-${Math.random()}`
  effects.value = [...effects.value.slice(-4), { id, x: event.clientX, y: event.clientY }]
  window.setTimeout(() => { effects.value = effects.value.filter((item) => item.id !== id) }, 1100)
}

function leave() { glowVisible.value = false }

onMounted(() => { document.addEventListener('pointermove', move, { passive: true }); document.addEventListener('click', click, { passive: true }); window.addEventListener('mouseleave', leave); frame = requestAnimationFrame(animateCursor) })
onBeforeUnmount(() => { document.removeEventListener('pointermove', move); document.removeEventListener('click', click); window.removeEventListener('mouseleave', leave); cancelAnimationFrame(frame) })
</script>

<template>
  <div class="tech-bg" aria-hidden="true">
    <div v-if="!reducedMotion.matches" class="cursor-glow" :class="{ 'is-visible': glowVisible }" :style="{ transform: `translate3d(${cursor.x}px, ${cursor.y}px, 0)` }" />
    <i v-for="n in 8" :key="n" class="ambient-dot" :style="{ left: `${(n * 13) % 100}%`, top: `${(n * 29) % 100}%`, animationDelay: `-${n * 1.7}s` }" />
    <div v-for="effect in effects" :key="effect.id" class="click-effect" :style="{ left: `${effect.x}px`, top: `${effect.y}px` }"><span class="ring" /><b v-for="n in 6" :key="n" :style="{ '--angle': `${n * 60}deg` }" /></div>
  </div>
</template>

<style scoped>
.tech-bg{position:fixed;inset:0;z-index:0;overflow:hidden;pointer-events:none;background-image:linear-gradient(#42b9e018 1px,transparent 1px),linear-gradient(90deg,#42b9e018 1px,transparent 1px);background-size:42px 42px;mask-image:linear-gradient(to bottom,#000,transparent 92%)}.tech-bg:before,.tech-bg:after{content:"";position:absolute;width:42vw;height:42vw;border-radius:50%;filter:blur(80px);opacity:.22;animation:drift 18s ease-in-out infinite alternate}.tech-bg:before{background:#147ee8;top:-20vw;right:-10vw}.tech-bg:after{background:#08c9d8;bottom:-25vw;left:-12vw;animation-delay:-8s}.cursor-glow{position:absolute;left:-70px;top:-70px;width:140px;height:140px;border-radius:50%;opacity:0;background:radial-gradient(circle,#31cfff44 0,#1a8fff18 35%,transparent 72%);will-change:transform;pointer-events:none;transition:opacity 180ms ease}.cursor-glow.is-visible{opacity:.2}.ambient-dot{position:absolute;width:4px;height:4px;border-radius:50%;background:#67dcff;box-shadow:0 0 12px #67dcff;animation:float 7s ease-in-out infinite}.click-effect{position:absolute;width:1px;height:1px;transform:translate(-50%,-50%);pointer-events:none}.ring{position:absolute;width:22px;height:22px;transform:translate(-50%,-50%);border:1px solid #66dcff;border-radius:50%;box-shadow:0 0 12px #28bfff;animation:ripple 900ms ease-out forwards}.click-effect b{position:absolute;left:0;top:0;width:4px;height:4px;border-radius:50%;background:#70e5ff;box-shadow:0 0 8px #39cfff;transform:rotate(var(--angle)) translateY(-8px);animation:particle 900ms ease-out forwards}@keyframes drift{to{transform:translate(8vw,10vh) scale(1.2)}}@keyframes float{50%{opacity:.25;transform:translate(12px,-18px)}}@keyframes ripple{to{width:130px;height:130px;opacity:0}}@keyframes particle{to{opacity:0;transform:rotate(var(--angle)) translateY(-58px) scale(.3)}}@media(prefers-reduced-motion:reduce){.tech-bg:before,.tech-bg:after,.ambient-dot{animation:none}.cursor-glow,.click-effect{display:none}}
</style>
