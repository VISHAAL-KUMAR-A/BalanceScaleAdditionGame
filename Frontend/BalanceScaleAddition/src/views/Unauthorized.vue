<template>
  <div class="unauthorized">
    <div class="content">
      <span class="icon">🚫</span>
      <h1>Access Denied</h1>
      <p>You don't have permission to access this page.</p>
      <p class="details">Required role: {{ requiredRole }}</p>
      <p class="details">Your role: {{ userRole }}</p>
      <router-link to="/dashboard" class="btn">Go to Dashboard</router-link>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()
const route = useRoute()

const userRole = computed(() => authStore.userRole)
const requiredRole = computed(() => route.meta.requiresRole || 'Unknown')
</script>

<style scoped>
.unauthorized {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 2rem;
}

.content {
  background: white;
  padding: 3rem;
  border-radius: 20px;
  text-align: center;
  max-width: 500px;
}

.icon {
  font-size: 5rem;
  display: block;
  margin-bottom: 1rem;
}

h1 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

p {
  color: #7f8c8d;
  margin-bottom: 0.5rem;
}

.details {
  font-size: 0.9rem;
  color: #95a5a6;
}

.btn {
  display: inline-block;
  margin-top: 2rem;
  padding: 0.75rem 2rem;
  background: #667eea;
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  transition: transform 0.2s;
}

.btn:hover {
  transform: translateY(-2px);
}
</style>

