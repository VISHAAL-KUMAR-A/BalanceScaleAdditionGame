<template>
  <div class="max-w-4xl mx-auto px-6 py-12 text-center">
    <h1 class="text-5xl font-bold text-gray-100 mb-3">🎯 Balance Scale Addition Game</h1>
    <p class="text-xl text-gray-400 mb-8">Learn addition through visual intuition!</p>
    
    <div class="bg-gradient-to-br from-purple-600 via-purple-700 to-purple-900 text-white p-12 rounded-3xl my-8 shadow-2xl">
      <div class="text-7xl mb-4">⚖️</div>
      <p class="text-lg leading-relaxed">
        Master addition by balancing the scale! When you're close but not quite right, 
        the scale tilts to show if your sum is too large or too small.
      </p>
    </div>

    <div class="flex gap-4 justify-center mt-8" v-if="!isAuthenticated">
      <router-link to="/login" class="px-8 py-3 bg-purple-600 hover:bg-purple-700 text-white font-semibold rounded-xl transition-all duration-200 hover:-translate-y-1 hover:shadow-lg">
        Login
      </router-link>
      <router-link to="/register" class="px-8 py-3 bg-gray-800 hover:bg-gray-700 text-white font-semibold rounded-xl border-2 border-purple-600 transition-all duration-200 hover:-translate-y-1 hover:shadow-lg">
        Register
      </router-link>
    </div>

    <div class="flex gap-4 justify-center mt-8" v-else>
      <router-link to="/dashboard" class="px-8 py-3 bg-purple-600 hover:bg-purple-700 text-white font-semibold rounded-xl transition-all duration-200 hover:-translate-y-1 hover:shadow-lg">
        Go to Dashboard
      </router-link>
      <button @click="handleLogout" class="px-8 py-3 bg-gray-800 hover:bg-gray-700 text-white font-semibold rounded-xl border-2 border-purple-600 transition-all duration-200 hover:-translate-y-1 hover:shadow-lg">
        Logout
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()
const router = useRouter()

const isAuthenticated = computed(() => authStore.isAuthenticated)

const handleLogout = async () => {
  await authStore.logout()
  router.push('/')
}
</script>

