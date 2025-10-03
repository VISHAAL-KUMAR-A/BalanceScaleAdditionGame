<template>
  <div class="max-w-6xl mx-auto px-6 py-12">
    <div class="text-center mb-12">
      <h1 class="text-4xl font-bold text-gray-100 mb-4">👋 Welcome, {{ displayName }}!</h1>
      <p class="inline-block px-6 py-2 rounded-full font-semibold uppercase text-sm" :class="roleClass">
        {{ userRole }}
      </p>
    </div>

    <div class="bg-gray-800 p-6 rounded-2xl mb-12 border border-gray-700">
      <p class="mb-3 text-gray-300"><strong class="text-gray-100">Email:</strong> {{ user?.email }}</p>
      <p class="text-gray-300"><strong class="text-gray-100">User ID:</strong> {{ user?.uid }}</p>
    </div>

    <div class="mb-12">
      <h2 class="text-3xl font-bold text-gray-100 mb-6">Quick Links</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Student Links -->
        <router-link v-if="isStudent" to="/student/games" class="bg-gray-800 p-8 rounded-2xl border-2 border-gray-700 hover:border-purple-500 transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl text-center group">
          <span class="text-5xl block mb-4">🎮</span>
          <h3 class="text-xl font-bold text-gray-100 mb-2 group-hover:text-purple-400">Play Games</h3>
          <p class="text-gray-400">Practice addition with balance scales</p>
        </router-link>

        <router-link v-if="isStudent" to="/student/progress" class="bg-gray-800 p-8 rounded-2xl border-2 border-gray-700 hover:border-purple-500 transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl text-center group">
          <span class="text-5xl block mb-4">📊</span>
          <h3 class="text-xl font-bold text-gray-100 mb-2 group-hover:text-purple-400">My Progress</h3>
          <p class="text-gray-400">View your learning progress</p>
        </router-link>

        <!-- Teacher Links -->
        <router-link v-if="isTeacher" to="/teacher/students" class="bg-gray-800 p-8 rounded-2xl border-2 border-gray-700 hover:border-purple-500 transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl text-center group">
          <span class="text-5xl block mb-4">👨‍🎓</span>
          <h3 class="text-xl font-bold text-gray-100 mb-2 group-hover:text-purple-400">My Students</h3>
          <p class="text-gray-400">Manage and track students</p>
        </router-link>

        <router-link v-if="isTeacher" to="/teacher/assignments" class="bg-gray-800 p-8 rounded-2xl border-2 border-gray-700 hover:border-purple-500 transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl text-center group">
          <span class="text-5xl block mb-4">📝</span>
          <h3 class="text-xl font-bold text-gray-100 mb-2 group-hover:text-purple-400">Assignments</h3>
          <p class="text-gray-400">Create and manage assignments</p>
        </router-link>

        <!-- Admin Links -->
        <router-link v-if="isAdmin" to="/admin/users" class="bg-gray-800 p-8 rounded-2xl border-2 border-gray-700 hover:border-purple-500 transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl text-center group">
          <span class="text-5xl block mb-4">👥</span>
          <h3 class="text-xl font-bold text-gray-100 mb-2 group-hover:text-purple-400">User Management</h3>
          <p class="text-gray-400">Manage all users and roles</p>
        </router-link>

        <router-link v-if="isAdmin" to="/admin/stats" class="bg-gray-800 p-8 rounded-2xl border-2 border-gray-700 hover:border-purple-500 transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl text-center group">
          <span class="text-5xl block mb-4">📈</span>
          <h3 class="text-xl font-bold text-gray-100 mb-2 group-hover:text-purple-400">Statistics</h3>
          <p class="text-gray-400">View system statistics</p>
        </router-link>
      </div>
    </div>

    <button @click="handleLogout" class="block mx-auto px-8 py-3 bg-red-600 hover:bg-red-700 text-white font-semibold rounded-xl transition-colors">
      Logout
    </button>
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
  const roleMap = {
    'user': 'bg-gray-700 text-gray-300',
    'student': 'bg-blue-900/50 text-blue-300 border border-blue-500',
    'teacher': 'bg-purple-900/50 text-purple-300 border border-purple-500',
    'admin': 'bg-red-900/50 text-red-300 border border-red-500'
  }
  return roleMap[userRole.value] || roleMap['user']
})

const handleLogout = async () => {
  await authStore.logout()
  router.push('/')
}
</script>
