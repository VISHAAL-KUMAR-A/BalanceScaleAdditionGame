<template>
  <div>
    <!-- User Info Header -->
    <div class="bg-gray-800/50 border-b border-gray-700 px-4 py-3">
      <div class="max-w-7xl mx-auto flex justify-between items-center">
        <div class="flex items-center gap-4">
          <div>
            <span class="text-gray-300 text-sm">Welcome, </span>
            <span class="text-white font-semibold">{{ displayName }}</span>
          </div>
          <span class="px-3 py-1 rounded-full text-xs font-semibold uppercase" :class="roleClass">
            {{ userRole }}
          </span>
        </div>
        <button @click="handleLogout" class="px-4 py-2 bg-red-600 hover:bg-red-700 text-white text-sm font-semibold rounded-lg transition-colors">
          Logout
        </button>
      </div>
    </div>

    <!-- Balance Scale Game -->
    <BalanceScaleGame />

    <!-- Quick Links Section -->
    <div class="max-w-7xl mx-auto px-4 py-8">
      <div class="bg-gray-800/50 rounded-2xl p-6 border border-gray-700">
        <h3 class="text-xl font-bold text-gray-100 mb-4">Quick Links</h3>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
          <!-- Student Links -->
          <router-link v-if="isStudent" to="/student/progress" class="bg-gray-700/50 p-4 rounded-xl hover:bg-gray-700 transition-colors text-center group">
            <span class="text-3xl block mb-2">📊</span>
            <span class="text-sm text-gray-300 group-hover:text-purple-300">Progress</span>
          </router-link>

          <!-- Teacher Links -->
          <router-link v-if="isTeacher" to="/teacher/students" class="bg-gray-700/50 p-4 rounded-xl hover:bg-gray-700 transition-colors text-center group">
            <span class="text-3xl block mb-2">👨‍🎓</span>
            <span class="text-sm text-gray-300 group-hover:text-purple-300">Students</span>
          </router-link>

          <router-link v-if="isTeacher" to="/teacher/assignments" class="bg-gray-700/50 p-4 rounded-xl hover:bg-gray-700 transition-colors text-center group">
            <span class="text-3xl block mb-2">📝</span>
            <span class="text-sm text-gray-300 group-hover:text-purple-300">Assignments</span>
          </router-link>

          <!-- Admin Links -->
          <router-link v-if="isAdmin" to="/admin/users" class="bg-gray-700/50 p-4 rounded-xl hover:bg-gray-700 transition-colors text-center group">
            <span class="text-3xl block mb-2">👥</span>
            <span class="text-sm text-gray-300 group-hover:text-purple-300">Users</span>
          </router-link>

          <router-link v-if="isAdmin" to="/admin/stats" class="bg-gray-700/50 p-4 rounded-xl hover:bg-gray-700 transition-colors text-center group">
            <span class="text-3xl block mb-2">📈</span>
            <span class="text-sm text-gray-300 group-hover:text-purple-300">Stats</span>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import BalanceScaleGame from '../components/BalanceScaleGame.vue'

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
