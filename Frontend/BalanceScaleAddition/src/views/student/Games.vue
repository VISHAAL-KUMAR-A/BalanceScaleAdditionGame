<template>
  <div class="games-page">
    <h1>🎮 Available Games</h1>
    <p class="subtitle">Choose a difficulty level to start playing!</p>

    <div v-if="loading" class="loading">Loading games...</div>
    
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else class="games-grid">
      <div v-for="game in games" :key="game.id" class="game-card">
        <div class="game-icon">⚖️</div>
        <h3>{{ game.name }}</h3>
        <p class="difficulty" :class="`difficulty-${game.difficulty}`">
          {{ game.difficulty.toUpperCase() }}
        </p>
        <button class="btn-play">Play Now</button>
      </div>
    </div>

    <router-link to="/dashboard" class="btn-back">← Back to Dashboard</router-link>
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

onMounted(() => {
  fetchGames()
})
</script>

<style scoped>
.games-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

h1 {
  color: #2c3e50;
  text-align: center;
  margin-bottom: 0.5rem;
}

.subtitle {
  text-align: center;
  color: #7f8c8d;
  margin-bottom: 2rem;
}

.loading, .error {
  text-align: center;
  padding: 2rem;
  font-size: 1.1rem;
}

.error {
  color: #e74c3c;
}

.games-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.game-card {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  border: 2px solid #e0e0e0;
  text-align: center;
  transition: all 0.3s;
}

.game-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}

.game-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
}

.game-card h3 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.difficulty {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-weight: 600;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.difficulty-easy {
  background: #d4edda;
  color: #155724;
}

.difficulty-medium {
  background: #fff3cd;
  color: #856404;
}

.difficulty-hard {
  background: #f8d7da;
  color: #721c24;
}

.btn-play {
  width: 100%;
  padding: 0.75rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.3s;
}

.btn-play:hover {
  background: #5568d3;
}

.btn-back {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background: #95a5a6;
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  transition: background 0.3s;
}

.btn-back:hover {
  background: #7f8c8d;
}
</style>

