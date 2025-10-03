<script setup>
import { onMounted } from 'vue'
import { useAuthStore } from './stores/auth'

const authStore = useAuthStore()

onMounted(() => {
  authStore.initAuth()
})
</script>

<template>
  <div id="app" class="min-h-screen bg-gray-900 text-gray-100">
    <router-view v-if="!authStore.loading" />
    <div v-else class="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-purple-600 via-purple-700 to-purple-900">
      <div class="w-12 h-12 border-4 border-purple-300/30 border-t-white rounded-full animate-spin"></div>
      <p class="mt-4 text-white text-xl font-medium">Loading...</p>
    </div>
  </div>
</template>
