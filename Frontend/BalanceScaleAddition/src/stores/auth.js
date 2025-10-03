import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { 
  signInWithPopup,
  signOut,
  onAuthStateChanged
} from 'firebase/auth'
import { auth, googleProvider } from '../config/firebase'
import apiClient from '../api/axios'

export const useAuthStore = defineStore('auth', () => {
  // State
  const user = ref(null)
  const token = ref(localStorage.getItem('auth_token') || null)
  const loading = ref(true)
  const error = ref(null)

  // Getters
  const isAuthenticated = computed(() => !!user.value && !!token.value)
  const userRole = computed(() => user.value?.role || 'user')
  const isStudent = computed(() => ['student', 'teacher', 'admin'].includes(userRole.value))
  const isTeacher = computed(() => ['teacher', 'admin'].includes(userRole.value))
  const isAdmin = computed(() => userRole.value === 'admin')

  // Set token in localStorage and axios headers
  const setToken = (newToken) => {
    token.value = newToken
    localStorage.setItem('auth_token', newToken)
    apiClient.defaults.headers.common['Authorization'] = `Bearer ${newToken}`
  }

  // Clear token
  const clearToken = () => {
    token.value = null
    localStorage.removeItem('auth_token')
    delete apiClient.defaults.headers.common['Authorization']
  }

  // Actions
  const initAuth = () => {
    return new Promise((resolve) => {
      // Check if we have a stored token
      const storedToken = localStorage.getItem('auth_token')
      if (storedToken) {
        setToken(storedToken)
        fetchUserProfile().then(() => {
          loading.value = false
          resolve(user.value)
        }).catch(() => {
          // Token invalid, clear it
          clearToken()
          user.value = null
          loading.value = false
          resolve(null)
        })
      } else {
        user.value = null
        loading.value = false
        resolve(null)
      }
    })
  }

  const fetchUserProfile = async () => {
    try {
      const response = await apiClient.get('/api/auth/me')
      user.value = response.data
      return response.data
    } catch (err) {
      console.error('Failed to fetch user profile:', err)
      throw err
    }
  }

  const register = async (email, password, displayName) => {
    try {
      error.value = null
      loading.value = true
      
      const response = await apiClient.post('/api/auth/register', {
        email,
        password,
        display_name: displayName
      })
      
      // Set token and user from response
      setToken(response.data.access_token)
      user.value = response.data.user
      
      return user.value
    } catch (err) {
      error.value = err.response?.data?.detail || err.message
      throw err
    } finally {
      loading.value = false
    }
  }

  const login = async (email, password) => {
    try {
      error.value = null
      loading.value = true
      
      const response = await apiClient.post('/api/auth/login', {
        email,
        password
      })
      
      // Set token and user from response
      setToken(response.data.access_token)
      user.value = response.data.user
      
      return user.value
    } catch (err) {
      error.value = err.response?.data?.detail || err.message
      throw err
    } finally {
      loading.value = false
    }
  }

  const loginWithGoogle = async () => {
    try {
      error.value = null
      loading.value = true
      
      // Sign in with Firebase Google
      const result = await signInWithPopup(auth, googleProvider)
      const firebaseToken = await result.user.getIdToken()
      
      // Send Firebase token to our backend
      const response = await apiClient.post('/api/auth/google', {
        firebase_token: firebaseToken
      })
      
      // Set our backend token and user
      setToken(response.data.access_token)
      user.value = response.data.user
      
      return user.value
    } catch (err) {
      error.value = err.response?.data?.detail || err.message
      throw err
    } finally {
      loading.value = false
    }
  }

  const logout = async () => {
    try {
      // Sign out from Firebase if user is signed in
      if (auth.currentUser) {
        await signOut(auth)
      }
      
      // Clear local state
      clearToken()
      user.value = null
    } catch (err) {
      error.value = err.message
      throw err
    }
  }

  return {
    // State
    user,
    token,
    loading,
    error,
    // Getters
    isAuthenticated,
    userRole,
    isStudent,
    isTeacher,
    isAdmin,
    // Actions
    initAuth,
    fetchUserProfile,
    register,
    login,
    loginWithGoogle,
    logout
  }
})
