<template>
  <div class="max-w-6xl mx-auto px-6 py-12">
    <h1 class="text-4xl font-bold text-gray-100 text-center mb-2">📊 My Progress</h1>
    <p class="text-center text-gray-400 mb-12">Track your learning journey!</p>

    <div v-if="loading" class="text-center py-12 text-xl text-gray-400">Loading progress...</div>
    
    <div v-else-if="error" class="text-center py-12 text-xl text-red-400">{{ error }}</div>

    <div v-else class="mb-8">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div class="bg-gray-800 p-8 rounded-2xl border border-gray-700 text-center">
          <div class="text-5xl mb-4">🎮</div>
          <div class="text-4xl font-bold text-purple-400 mb-2">{{ progress.games_played }}</div>
          <div class="text-gray-400">Games Played</div>
        </div>

        <div class="bg-gray-800 p-8 rounded-2xl border border-gray-700 text-center">
          <div class="text-5xl mb-4">🎯</div>
          <div class="text-4xl font-bold text-blue-400 mb-2">{{ progress.accuracy }}%</div>
          <div class="text-gray-400">Accuracy</div>
        </div>

        <div class="bg-gray-800 p-8 rounded-2xl border border-gray-700 text-center">
          <div class="text-5xl mb-4">⭐</div>
          <div class="text-4xl font-bold text-yellow-400 mb-2">{{ progress.level }}</div>
          <div class="text-gray-400">Current Level</div>
        </div>
      </div>

      <div class="bg-gray-800 p-8 rounded-2xl border border-gray-700">
        <h3 class="text-2xl font-bold text-gray-100 mb-6">Level Progress</h3>
        <div class="w-full h-8 bg-gray-700 rounded-full overflow-hidden mb-2">
          <div 
            class="h-full bg-gradient-to-r from-purple-600 to-purple-800 transition-all duration-500 ease-out flex items-center justify-end pr-3"
            :style="{ width: `${(progress.level / 10) * 100}%` }"
          >
            <span class="text-white text-sm font-semibold" v-if="progress.level > 0">{{ progress.level }}</span>
          </div>
        </div>
        <p class="text-center text-gray-400 mt-4">Level {{ progress.level }} of 10</p>
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

const progress = ref({})
const loading = ref(true)
const error = ref(null)

const fetchProgress = async () => {
  try {
    const response = await apiClient.get('/api/student/progress')
    progress.value = response.data.progress
  } catch (err) {
    error.value = 'Failed to load progress. Please try again.'
    console.error(err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchProgress()
})
</script>
