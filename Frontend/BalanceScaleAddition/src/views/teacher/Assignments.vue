<template>
  <div class="max-w-6xl mx-auto px-6 py-12">
    <h1 class="text-4xl font-bold text-gray-100 text-center mb-2">📝 Assignments</h1>
    <p class="text-center text-gray-400 mb-12">Create and manage student assignments</p>

    <div v-if="loading" class="text-center py-12 text-xl text-gray-400">Loading assignments...</div>
    
    <div v-else-if="error" class="text-center py-12 text-xl text-red-400">{{ error }}</div>

    <div v-else>
      <div class="grid gap-6 mb-8">
        <div v-for="assignment in assignments" :key="assignment.id" class="bg-gray-800 p-6 rounded-2xl border border-gray-700 hover:border-purple-500 transition-all duration-300">
          <div class="flex justify-between items-start mb-4">
            <h3 class="text-2xl font-bold text-gray-100">{{ assignment.title }}</h3>
            <span class="text-gray-400 text-sm">Due: {{ assignment.due_date }}</span>
          </div>
          <div class="flex gap-4">
            <button class="px-6 py-2 bg-purple-600 hover:bg-purple-700 text-white font-semibold rounded-lg transition-colors">
              Edit
            </button>
            <button class="px-6 py-2 bg-gray-700 hover:bg-gray-600 text-gray-100 font-semibold rounded-lg transition-colors">
              View Details
            </button>
          </div>
        </div>
      </div>

      <button class="w-full px-6 py-4 bg-green-600 hover:bg-green-700 text-white font-bold text-lg rounded-xl transition-colors mb-8">
        + Create New Assignment
      </button>
    </div>

    <router-link to="/dashboard" class="inline-block px-6 py-3 bg-gray-700 hover:bg-gray-600 text-white font-semibold rounded-xl transition-colors">
      ← Back to Dashboard
    </router-link>
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
