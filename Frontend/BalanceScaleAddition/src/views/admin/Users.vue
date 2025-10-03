<template>
  <div class="users-page">
    <h1>👥 User Management</h1>
    <p class="subtitle">Manage all users and their roles</p>

    <div v-if="loading" class="loading">Loading users...</div>
    
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else class="users-table">
      <table>
        <thead>
          <tr>
            <th>User ID</th>
            <th>Email</th>
            <th>Role</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.uid">
            <td>{{ user.uid }}</td>
            <td>{{ user.email }}</td>
            <td>
              <span class="role-badge" :class="`role-${user.role}`">
                {{ user.role }}
              </span>
            </td>
            <td>
              <button class="btn-manage">Manage Role</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <router-link to="/dashboard" class="btn-back">← Back to Dashboard</router-link>
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

onMounted(() => {
  fetchUsers()
})
</script>

<style scoped>
.users-page {
  max-width: 1400px;
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

.users-table {
  background: white;
  border-radius: 15px;
  border: 2px solid #e0e0e0;
  overflow: hidden;
  margin-bottom: 2rem;
}

table {
  width: 100%;
  border-collapse: collapse;
}

thead {
  background: #f8f9fa;
}

th, td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #e0e0e0;
}

th {
  color: #2c3e50;
  font-weight: 600;
}

td {
  color: #555;
}

.role-badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 600;
  text-transform: uppercase;
}

.role-user {
  background: #e0e0e0;
  color: #666;
}

.role-student {
  background: #e3f2fd;
  color: #1976d2;
}

.role-teacher {
  background: #f3e5f5;
  color: #7b1fa2;
}

.role-admin {
  background: #ffebee;
  color: #c62828;
}

.btn-manage {
  padding: 0.5rem 1rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.3s;
}

.btn-manage:hover {
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

