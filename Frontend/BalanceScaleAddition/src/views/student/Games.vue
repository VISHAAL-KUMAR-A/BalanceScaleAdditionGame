<template>
  <div class="max-w-6xl mx-auto px-6 py-12">
    <h1 class="text-4xl font-bold text-gray-100 text-center mb-2">🎮 Available Games</h1>
    <p class="text-center text-gray-400 mb-12">Choose a difficulty level to start playing!</p>

    <div v-if="loading" class="text-center py-12 text-xl text-gray-400">Loading games...</div>
    
    <div v-else-if="error" class="text-center py-12 text-xl text-red-400">{{ error }}</div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-8">
      <div v-for="game in games" :key="game.id" class="bg-gray-800 p-8 rounded-2xl border border-gray-700 text-center hover:-translate-y-2 hover:border-purple-500 transition-all duration-300 group">
        <div class="text-6xl mb-4">⚖️</div>
        <h3 class="text-2xl font-bold text-gray-100 mb-4 group-hover:text-purple-400">{{ game.name }}</h3>
        <p class="inline-block px-4 py-2 rounded-full text-sm font-semibold uppercase mb-6" :class="getDifficultyClass(game.difficulty)">
          {{ game.difficulty.toUpperCase() }}
        </p>
        <button class="w-full px-6 py-3 bg-purple-600 hover:bg-purple-700 text-white font-semibold rounded-xl transition-colors">
          Play Now
        </button>
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

const games = ref([])
const loading = ref(true)
const error = ref(null)

const fetchGames = async () => {
  try {
    const response = await apiClient.get('/api/student/games')
    games.value = response.data.games
  } catch (err) {
    error.value = 'Failed to load games. Please try again.'
    console.error(err)
  } finally {
    loading.value = false
  }
}

const getDifficultyClass = (difficulty) => {
  const difficultyMap = {
    'easy': 'bg-green-900/50 text-green-300 border border-green-500',
    'medium': 'bg-yellow-900/50 text-yellow-300 border border-yellow-500',
    'hard': 'bg-red-900/50 text-red-300 border border-red-500'
  }
  return difficultyMap[difficulty] || difficultyMap['easy']
}

onMounted(() => {
  fetchGames()
})
</script>
