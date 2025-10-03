<template>
  <div class="dashboard">
    <div class="dashboard-header">
      <h1>👋 Welcome, {{ displayName }}!</h1>
      <p class="role-badge" :class="roleClass">{{ userRole }}</p>
    </div>

    <div class="user-info">
      <p><strong>Email:</strong> {{ user?.email }}</p>
      <p><strong>User ID:</strong> {{ user?.uid }}</p>
    </div>

    <div class="quick-links">
      <h2>Quick Links</h2>
      <div class="links-grid">
        <!-- Student Links -->
        <router-link v-if="isStudent" to="/student/games" class="link-card">
          <span class="icon">🎮</span>
          <h3>Play Games</h3>
          <p>Practice addition with balance scales</p>
        </router-link>

        <router-link v-if="isStudent" to="/student/progress" class="link-card">
          <span class="icon">📊</span>
          <h3>My Progress</h3>
          <p>View your learning progress</p>
        </router-link>

        <!-- Teacher Links -->
        <router-link v-if="isTeacher" to="/teacher/students" class="link-card">
          <span class="icon">👨‍🎓</span>
          <h3>My Students</h3>
          <p>Manage and track students</p>
        </router-link>

        <router-link v-if="isTeacher" to="/teacher/assignments" class="link-card">
          <span class="icon">📝</span>
          <h3>Assignments</h3>
          <p>Create and manage assignments</p>
        </router-link>

        <!-- Admin Links -->
        <router-link v-if="isAdmin" to="/admin/users" class="link-card">
          <span class="icon">👥</span>
          <h3>User Management</h3>
          <p>Manage all users and roles</p>
        </router-link>

        <router-link v-if="isAdmin" to="/admin/stats" class="link-card">
          <span class="icon">📈</span>
          <h3>Statistics</h3>
          <p>View system statistics</p>
        </router-link>
      </div>
    </div>

    <button @click="handleLogout" class="btn-logout">Logout</button>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()
const router = useRouter()

const user = computed(() => authStore.user)
const userRole = computed(() => authStore.userRole)
const isStudent = computed(() => authStore.isStudent)
const isTeacher = computed(() => authStore.isTeacher)
const isAdmin = computed(() => authStore.isAdmin)

const displayName = computed(() => user.value?.displayName || user.value?.email?.split('@')[0] || 'User')

const roleClass = computed(() => {
  return `role-${userRole.value}`
})

const handleLogout = async () => {
  await authStore.logout()
  router.push('/')
}
</script>

<style scoped>
.dashboard {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.dashboard-header {
  text-align: center;
  margin-bottom: 2rem;
}

.dashboard-header h1 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.role-badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.9rem;
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

.user-info {
  background: #f5f5f5;
  padding: 1.5rem;
  border-radius: 10px;
  margin-bottom: 2rem;
}

.user-info p {
  margin: 0.5rem 0;
  color: #555;
}

.quick-links h2 {
  color: #2c3e50;
  margin-bottom: 1.5rem;
}

.links-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.link-card {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  text-decoration: none;
  border: 2px solid #e0e0e0;
  transition: all 0.3s;
  text-align: center;
}

.link-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  border-color: #667eea;
}

.link-card .icon {
  font-size: 3rem;
  display: block;
  margin-bottom: 1rem;
}

.link-card h3 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.link-card p {
  color: #7f8c8d;
  font-size: 0.9rem;
  margin: 0;
}

.btn-logout {
  display: block;
  margin: 2rem auto 0;
  padding: 0.75rem 2rem;
  background: #e74c3c;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.3s;
}

.btn-logout:hover {
  background: #c0392b;
}
</style>

