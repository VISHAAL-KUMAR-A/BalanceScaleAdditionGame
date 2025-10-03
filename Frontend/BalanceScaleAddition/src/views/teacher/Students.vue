<template>
  <div class="students-page">
    <h1>👨‍🎓 My Students</h1>
    <p class="subtitle">Manage and track your students' progress</p>

    <div v-if="loading" class="loading">Loading students...</div>
    
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else class="students-list">
      <div v-for="student in students" :key="student.id" class="student-card">
        <div class="student-avatar">{{ student.name.charAt(0) }}</div>
        <div class="student-info">
          <h3>{{ student.name }}</h3>
          <p class="student-id">ID: {{ student.id }}</p>
        </div>
        <div class="student-progress">
          <div class="progress-circle" :style="{ background: getProgressColor(student.progress) }">
            {{ student.progress }}%
          </div>
          <p>Progress</p>
        </div>
      </div>
    </div>

    <router-link to="/dashboard" class="btn-back">← Back to Dashboard</router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import apiClient from '../../api/axios'

const students = ref([])
const loading = ref(true)
const error = ref(null)

const fetchStudents = async () => {
  try {
    const response = await apiClient.get('/api/teacher/students')
    students.value = response.data.students
  } catch (err) {
    error.value = 'Failed to load students. Please try again.'
    console.error(err)
  } finally {
    loading.value = false
  }
}

const getProgressColor = (progress) => {
  if (progress >= 80) return '#4caf50'
  if (progress >= 60) return '#ff9800'
  return '#f44336'
}

onMounted(() => {
  fetchStudents()
})
</script>

<style scoped>
.students-page {
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

.students-list {
  display: grid;
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.student-card {
  background: white;
  padding: 1.5rem;
  border-radius: 15px;
  border: 2px solid #e0e0e0;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  transition: all 0.3s;
}

.student-card:hover {
  transform: translateX(5px);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
}

.student-avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: bold;
}

.student-info {
  flex: 1;
}

.student-info h3 {
  color: #2c3e50;
  margin-bottom: 0.25rem;
}

.student-id {
  color: #95a5a6;
  font-size: 0.9rem;
  margin: 0;
}

.student-progress {
  text-align: center;
}

.progress-circle {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  font-weight: bold;
  color: white;
  margin-bottom: 0.5rem;
}

.student-progress p {
  color: #7f8c8d;
  font-size: 0.9rem;
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

