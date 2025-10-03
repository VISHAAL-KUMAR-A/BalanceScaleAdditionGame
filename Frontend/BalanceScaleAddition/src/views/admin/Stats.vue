<template>
  <div class="max-w-6xl mx-auto px-6 py-12">
    <h1 class="text-4xl font-bold text-gray-100 text-center mb-2">📈 System Statistics</h1>
    <p class="text-center text-gray-400 mb-12">Overview of platform usage and activity</p>

    <div v-if="loading" class="text-center py-12 text-xl text-gray-400">Loading statistics...</div>
    
    <div v-else-if="error" class="text-center py-12 text-xl text-red-400">{{ error }}</div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <div class="bg-gray-800 p-8 rounded-2xl border border-gray-700 text-center hover:-translate-y-2 transition-transform duration-300">
        <div class="text-5xl mb-4">👥</div>
        <div class="text-4xl font-bold text-purple-400 mb-2">{{ stats.total_users }}</div>
        <div class="text-gray-400">Total Users</div>
      </div>

      <div class="bg-gray-800 p-8 rounded-2xl border border-gray-700 text-center hover:-translate-y-2 transition-transform duration-300">
        <div class="text-5xl mb-4">🎓</div>
        <div class="text-4xl font-bold text-blue-400 mb-2">{{ stats.total_students }}</div>
        <div class="text-gray-400">Students</div>
      </div>

      <div class="bg-gray-800 p-8 rounded-2xl border border-gray-700 text-center hover:-translate-y-2 transition-transform duration-300">
        <div class="text-5xl mb-4">👨‍🏫</div>
        <div class="text-4xl font-bold text-green-400 mb-2">{{ stats.total_teachers }}</div>
        <div class="text-gray-400">Teachers</div>
      </div>

      <div class="bg-gray-800 p-8 rounded-2xl border border-gray-700 text-center hover:-translate-y-2 transition-transform duration-300">
        <div class="text-5xl mb-4">🔑</div>
        <div class="text-4xl font-bold text-red-400 mb-2">{{ stats.total_admins }}</div>
        <div class="text-gray-400">Admins</div>
      </div>

      <div class="col-span-full bg-gradient-to-br from-purple-600 via-purple-700 to-purple-900 p-8 rounded-2xl text-center text-white hover:-translate-y-2 transition-transform duration-300 shadow-2xl">
        <div class="text-6xl mb-4">🎮</div>
        <div class="text-5xl font-bold mb-2">{{ stats.games_played_today }}</div>
        <div class="text-purple-100 text-lg">Games Played Today</div>
      </div>
    </div>

    <router-link to="/dashboard" class="inline-block px-6 py-3 bg-gray-700 hover:bg-gray-600 text-white font-semibold rounded-xl transition-colors">
      ← Back to Dashboard
    </router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import apiClient from '../../api/axios'

const stats = ref({})
const loading = ref(true)
const error = ref(null)

const fetchStats = async () => {
  try {
    const response = await apiClient.get('/api/admin/stats')
    stats.value = response.data.stats
  } catch (err) {
    error.value = 'Failed to load statistics. Please try again.'
    console.error(err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchStats()
})
</script>
