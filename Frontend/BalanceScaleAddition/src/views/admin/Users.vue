<template>
  <div class="max-w-7xl mx-auto px-6 py-12">
    <h1 class="text-4xl font-bold text-gray-100 text-center mb-2">👥 User Management</h1>
    <p class="text-center text-gray-400 mb-12">Manage all users and their roles</p>

    <div v-if="loading" class="text-center py-12 text-xl text-gray-400">Loading users...</div>
    
    <div v-else-if="error" class="text-center py-12 text-xl text-red-400">{{ error }}</div>

    <div v-else class="bg-gray-800 rounded-2xl border border-gray-700 overflow-hidden mb-8">
      <table class="w-full">
        <thead class="bg-gray-700/50">
          <tr>
            <th class="px-6 py-4 text-left text-gray-200 font-semibold">User ID</th>
            <th class="px-6 py-4 text-left text-gray-200 font-semibold">Email</th>
            <th class="px-6 py-4 text-left text-gray-200 font-semibold">Role</th>
            <th class="px-6 py-4 text-left text-gray-200 font-semibold">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.uid" class="border-t border-gray-700 hover:bg-gray-700/30 transition-colors">
            <td class="px-6 py-4 text-gray-300">{{ user.uid }}</td>
            <td class="px-6 py-4 text-gray-300">{{ user.email }}</td>
            <td class="px-6 py-4">
              <span class="inline-block px-4 py-1 rounded-full text-sm font-semibold uppercase" :class="getRoleClass(user.role)">
                {{ user.role }}
              </span>
            </td>
            <td class="px-6 py-4">
              <button class="px-4 py-2 bg-purple-600 hover:bg-purple-700 text-white font-semibold rounded-lg transition-colors">
                Manage Role
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <router-link to="/dashboard" class="inline-block px-6 py-3 bg-gray-700 hover:bg-gray-600 text-white font-semibold rounded-xl transition-colors">
      ← Back to Dashboard
    </router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import apiClient from '../../api/axios'

const users = ref([])
const loading = ref(true)
const error = ref(null)

const fetchUsers = async () => {
  try {
    const response = await apiClient.get('/api/admin/users')
    users.value = response.data.users
  } catch (err) {
    error.value = 'Failed to load users. Please try again.'
    console.error(err)
  } finally {
    loading.value = false
  }
}

const getRoleClass = (role) => {
  const roleMap = {
    'user': 'bg-gray-700 text-gray-300',
    'student': 'bg-blue-900/50 text-blue-300 border border-blue-500',
    'teacher': 'bg-purple-900/50 text-purple-300 border border-purple-500',
    'admin': 'bg-red-900/50 text-red-300 border border-red-500'
  }
  return roleMap[role] || roleMap['user']
}

onMounted(() => {
  fetchUsers()
})
</script>
