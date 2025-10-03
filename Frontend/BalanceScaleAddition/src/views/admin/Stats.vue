<template>
  <div class="stats-page">
    <h1>📈 System Statistics</h1>
    <p class="subtitle">Overview of platform usage and activity</p>

    <div v-if="loading" class="loading">Loading statistics...</div>
    
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon">👥</div>
        <div class="stat-value">{{ stats.total_users }}</div>
        <div class="stat-label">Total Users</div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">🎓</div>
        <div class="stat-value">{{ stats.total_students }}</div>
        <div class="stat-label">Students</div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">👨‍🏫</div>
        <div class="stat-value">{{ stats.total_teachers }}</div>
        <div class="stat-label">Teachers</div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">🔑</div>
        <div class="stat-value">{{ stats.total_admins }}</div>
        <div class="stat-label">Admins</div>
      </div>

      <div class="stat-card large">
        <div class="stat-icon">🎮</div>
        <div class="stat-value">{{ stats.games_played_today }}</div>
        <div class="stat-label">Games Played Today</div>
      </div>
    </div>

    <router-link to="/dashboard" class="btn-back">← Back to Dashboard</router-link>
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

<style scoped>
.stats-page {
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
  transition: all 0.3s;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}

.stat-card.large {
  grid-column: span 2;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.stat-card.large .stat-value,
.stat-card.large .stat-label {
  color: white;
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

