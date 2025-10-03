<template>
  <div class="progress-page">
    <h1>📊 My Progress</h1>
    <p class="subtitle">Track your learning journey!</p>

    <div v-if="loading" class="loading">Loading progress...</div>
    
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else class="progress-content">
      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-icon">🎮</div>
          <div class="stat-value">{{ progress.games_played }}</div>
          <div class="stat-label">Games Played</div>
        </div>

        <div class="stat-card">
          <div class="stat-icon">🎯</div>
          <div class="stat-value">{{ progress.accuracy }}%</div>
          <div class="stat-label">Accuracy</div>
        </div>

        <div class="stat-card">
          <div class="stat-icon">⭐</div>
          <div class="stat-value">{{ progress.level }}</div>
          <div class="stat-label">Current Level</div>
        </div>
      </div>

      <div class="progress-bar-container">
        <h3>Level Progress</h3>
        <div class="progress-bar">
          <div class="progress-fill" :style="{ width: `${(progress.level / 10) * 100}%` }"></div>
        </div>
        <p class="progress-text">Level {{ progress.level }} of 10</p>
      </div>
    </div>

    <router-link to="/dashboard" class="btn-back">← Back to Dashboard</router-link>
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

<style scoped>
.progress-page {
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

.progress-content {
  margin-bottom: 2rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  border: 2px solid #e0e0e0;
  text-align: center;
}

.stat-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.stat-value {
  font-size: 2.5rem;
  font-weight: bold;
  color: #667eea;
  margin-bottom: 0.5rem;
}

.stat-label {
  color: #7f8c8d;
  font-size: 0.9rem;
}

.progress-bar-container {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  border: 2px solid #e0e0e0;
}

.progress-bar-container h3 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.progress-bar {
  width: 100%;
  height: 30px;
  background: #e0e0e0;
  border-radius: 15px;
  overflow: hidden;
  margin-bottom: 0.5rem;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
  transition: width 0.5s ease;
}

.progress-text {
  text-align: center;
  color: #7f8c8d;
  margin: 0;
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

