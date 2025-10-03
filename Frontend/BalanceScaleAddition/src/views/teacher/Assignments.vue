<template>
  <div class="assignments-page">
    <h1>📝 Assignments</h1>
    <p class="subtitle">Create and manage student assignments</p>

    <div v-if="loading" class="loading">Loading assignments...</div>
    
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else>
      <div class="assignments-list">
        <div v-for="assignment in assignments" :key="assignment.id" class="assignment-card">
          <div class="assignment-header">
            <h3>{{ assignment.title }}</h3>
            <span class="due-date">Due: {{ assignment.due_date }}</span>
          </div>
          <div class="assignment-actions">
            <button class="btn-edit">Edit</button>
            <button class="btn-view">View Details</button>
          </div>
        </div>
      </div>

      <button class="btn-create">+ Create New Assignment</button>
    </div>

    <router-link to="/dashboard" class="btn-back">← Back to Dashboard</router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import apiClient from '../../api/axios'

const assignments = ref([])
const loading = ref(true)
const error = ref(null)

const fetchAssignments = async () => {
  try {
    const response = await apiClient.get('/api/teacher/assignments')
    assignments.value = response.data.assignments
  } catch (err) {
    error.value = 'Failed to load assignments. Please try again.'
    console.error(err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchAssignments()
})
</script>

<style scoped>
.assignments-page {
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

.assignments-list {
  display: grid;
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.assignment-card {
  background: white;
  padding: 1.5rem;
  border-radius: 15px;
  border: 2px solid #e0e0e0;
  transition: all 0.3s;
}

.assignment-card:hover {
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
}

.assignment-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.assignment-header h3 {
  color: #2c3e50;
  margin: 0;
}

.due-date {
  color: #7f8c8d;
  font-size: 0.9rem;
}

.assignment-actions {
  display: flex;
  gap: 1rem;
}

.btn-edit, .btn-view {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.3s;
}

.btn-edit {
  background: #667eea;
  color: white;
}

.btn-edit:hover {
  background: #5568d3;
}

.btn-view {
  background: #e0e0e0;
  color: #2c3e50;
}

.btn-view:hover {
  background: #d0d0d0;
}

.btn-create {
  width: 100%;
  padding: 1rem;
  background: #4caf50;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s;
  margin-bottom: 2rem;
}

.btn-create:hover {
  background: #45a049;
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

