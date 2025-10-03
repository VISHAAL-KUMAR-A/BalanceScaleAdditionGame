<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-600 via-purple-700 to-purple-900 p-4">
    <div class="bg-gray-800 p-10 rounded-3xl shadow-2xl w-full max-w-md border border-gray-700">
      <h2 class="text-center text-gray-100 mb-2 text-4xl font-bold">📝 Register</h2>
      <p class="text-center text-gray-400 mb-8">Join Balance Scale Addition!</p>

      <form @submit.prevent="handleRegister" class="mb-6">
        <div class="mb-6">
          <label for="displayName" class="block mb-2 text-gray-200 font-semibold">Display Name</label>
          <input
            type="text"
            id="displayName"
            v-model="displayName"
            required
            placeholder="Enter your name"
            :disabled="loading"
            class="w-full px-4 py-3 bg-gray-900 border-2 border-gray-700 rounded-xl text-gray-100 placeholder-gray-500 focus:outline-none focus:border-purple-500 transition-colors disabled:bg-gray-800 disabled:cursor-not-allowed"
          />
        </div>

        <div class="mb-6">
          <label for="email" class="block mb-2 text-gray-200 font-semibold">Email</label>
          <input
            type="email"
            id="email"
            v-model="email"
            required
            placeholder="Enter your email"
            :disabled="loading"
            class="w-full px-4 py-3 bg-gray-900 border-2 border-gray-700 rounded-xl text-gray-100 placeholder-gray-500 focus:outline-none focus:border-purple-500 transition-colors disabled:bg-gray-800 disabled:cursor-not-allowed"
          />
        </div>

        <div class="mb-6">
          <label for="password" class="block mb-2 text-gray-200 font-semibold">Password</label>
          <input
            type="password"
            id="password"
            v-model="password"
            required
            placeholder="Enter your password (min 6 characters)"
            :disabled="loading"
            minlength="6"
            class="w-full px-4 py-3 bg-gray-900 border-2 border-gray-700 rounded-xl text-gray-100 placeholder-gray-500 focus:outline-none focus:border-purple-500 transition-colors disabled:bg-gray-800 disabled:cursor-not-allowed"
          />
        </div>

        <div class="mb-6">
          <label for="confirmPassword" class="block mb-2 text-gray-200 font-semibold">Confirm Password</label>
          <input
            type="password"
            id="confirmPassword"
            v-model="confirmPassword"
            required
            placeholder="Confirm your password"
            :disabled="loading"
            class="w-full px-4 py-3 bg-gray-900 border-2 border-gray-700 rounded-xl text-gray-100 placeholder-gray-500 focus:outline-none focus:border-purple-500 transition-colors disabled:bg-gray-800 disabled:cursor-not-allowed"
          />
        </div>

        <div v-if="error" class="bg-red-900/30 border border-red-500 text-red-300 px-4 py-3 rounded-xl mb-4 text-sm">
          {{ error }}
        </div>

        <button type="submit" :disabled="loading" class="w-full px-4 py-3 bg-purple-600 hover:bg-purple-700 text-white font-semibold rounded-xl transition-all duration-200 hover:-translate-y-1 hover:shadow-lg disabled:opacity-60 disabled:cursor-not-allowed disabled:transform-none">
          {{ loading ? 'Creating account...' : 'Register' }}
        </button>
      </form>

      <div class="relative text-center my-6">
        <div class="absolute inset-0 flex items-center">
          <div class="w-full border-t border-gray-700"></div>
        </div>
        <span class="relative bg-gray-800 px-4 text-gray-400 text-sm">OR</span>
      </div>

      <button @click="handleGoogleRegister" :disabled="loading" class="w-full px-4 py-3 bg-gray-900 hover:bg-gray-700 text-gray-100 border-2 border-gray-700 font-semibold rounded-xl flex items-center justify-center gap-2 transition-all duration-200 hover:-translate-y-1 hover:shadow-lg disabled:opacity-60 disabled:cursor-not-allowed disabled:transform-none">
        <span class="text-xl">🔍</span>
        Sign up with Google
      </button>

      <p class="text-center mt-6 text-gray-400">
        Already have an account? 
        <router-link to="/login" class="text-purple-400 hover:text-purple-300 font-semibold hover:underline">Login here</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()
const router = useRouter()

const displayName = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const loading = ref(false)
const error = ref(null)

const handleRegister = async () => {
  try {
    loading.value = true
    error.value = null

    // Validate passwords match
    if (password.value !== confirmPassword.value) {
      error.value = 'Passwords do not match.'
      return
    }

    // Validate password length
    if (password.value.length < 6) {
      error.value = 'Password must be at least 6 characters.'
      return
    }

    await authStore.register(email.value, password.value, displayName.value)
    router.push('/dashboard')
  } catch (err) {
    error.value = getErrorMessage(err)
  } finally {
    loading.value = false
  }
}

const handleGoogleRegister = async () => {
  try {
    loading.value = true
    error.value = null
    
    await authStore.loginWithGoogle()
    router.push('/dashboard')
  } catch (err) {
    error.value = getErrorMessage(err)
  } finally {
    loading.value = false
  }
}

const getErrorMessage = (err) => {
  // Handle API errors from backend
  if (err.response?.data?.detail) {
    return err.response.data.detail
  }
  
  // Handle Firebase errors  
  const errorMessages = {
    'auth/email-already-in-use': 'This email is already registered.',
    'auth/invalid-email': 'Invalid email address.',
    'auth/operation-not-allowed': 'Email/password accounts are not enabled.',
    'auth/weak-password': 'Password is too weak.',
  }
  
  return errorMessages[err.code] || err.message || 'Registration failed. Please try again.'
}
</script>
