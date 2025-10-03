<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-600 via-purple-700 to-purple-900 p-8">
    <div class="bg-gray-800 p-12 rounded-3xl text-center max-w-lg border border-gray-700">
      <span class="text-8xl block mb-6">🚫</span>
      <h1 class="text-4xl font-bold text-gray-100 mb-4">Access Denied</h1>
      <p class="text-gray-300 mb-3 text-lg">You don't have permission to access this page.</p>
      <p class="text-gray-500 text-sm mb-2">Required role: <span class="text-purple-400 font-semibold">{{ requiredRole }}</span></p>
      <p class="text-gray-500 text-sm mb-8">Your role: <span class="text-blue-400 font-semibold">{{ userRole }}</span></p>
      <router-link to="/dashboard" class="inline-block px-8 py-3 bg-purple-600 hover:bg-purple-700 text-white font-semibold rounded-xl transition-all duration-200 hover:-translate-y-1">
        Go to Dashboard
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()
const route = useRoute()

const userRole = computed(() => authStore.userRole)
const requiredRole = computed(() => route.meta.requiresRole || 'Unknown')
</script>
