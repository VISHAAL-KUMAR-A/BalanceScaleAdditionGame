<template>
  <div class="max-w-6xl mx-auto px-6 py-12">
    <h1 class="text-4xl font-bold text-gray-100 text-center mb-2">👨‍🎓 My Students</h1>
    <p class="text-center text-gray-400 mb-12">Manage and track your students' progress</p>

    <div v-if="loading" class="text-center py-12 text-xl text-gray-400">Loading students...</div>
    
    <div v-else-if="error" class="text-center py-12 text-xl text-red-400">{{ error }}</div>

    <div v-else class="grid gap-6 mb-8">
      <div v-for="student in students" :key="student.id" class="bg-gray-800 p-6 rounded-2xl border border-gray-700 flex items-center gap-6 hover:border-purple-500 hover:translate-x-2 transition-all duration-300">
        <div class="w-16 h-16 rounded-full bg-gradient-to-br from-purple-600 to-purple-800 text-white flex items-center justify-center text-2xl font-bold flex-shrink-0">
          {{ student.name.charAt(0) }}
        </div>
        <div class="flex-1">
          <h3 class="text-xl font-bold text-gray-100 mb-1">{{ student.name }}</h3>
          <p class="text-gray-400 text-sm">ID: {{ student.id }}</p>
        </div>
        <div class="text-center">
          <div class="w-20 h-20 rounded-full flex items-center justify-center text-xl font-bold text-white mb-2" :style="{ background: getProgressColor(student.progress) }">
            {{ student.progress }}%
          </div>
          <p class="text-gray-400 text-sm">Progress</p>
        </div>
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
  if (progress >= 80) return '#10b981'  // green-500
  if (progress >= 60) return '#f59e0b'  // amber-500
  return '#ef4444'  // red-500
}

onMounted(() => {
  fetchStudents()
})
</script>
