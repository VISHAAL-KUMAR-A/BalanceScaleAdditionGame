import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
    meta: { requiresAuth: false }
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue'),
    meta: { requiresAuth: false, redirectIfAuth: true }
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue'),
    meta: { requiresAuth: false, redirectIfAuth: true }
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('../views/Dashboard.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/student/games',
    name: 'StudentGames',
    component: () => import('../views/student/Games.vue'),
    meta: { requiresAuth: true, requiresRole: 'student' }
  },
  {
    path: '/student/progress',
    name: 'StudentProgress',
    component: () => import('../views/student/Progress.vue'),
    meta: { requiresAuth: true, requiresRole: 'student' }
  },
  {
    path: '/teacher/students',
    name: 'TeacherStudents',
    component: () => import('../views/teacher/Students.vue'),
    meta: { requiresAuth: true, requiresRole: 'teacher' }
  },
  {
    path: '/teacher/assignments',
    name: 'TeacherAssignments',
    component: () => import('../views/teacher/Assignments.vue'),
    meta: { requiresAuth: true, requiresRole: 'teacher' }
  },
  {
    path: '/admin/users',
    name: 'AdminUsers',
    component: () => import('../views/admin/Users.vue'),
    meta: { requiresAuth: true, requiresRole: 'admin' }
  },
  {
    path: '/admin/stats',
    name: 'AdminStats',
    component: () => import('../views/admin/Stats.vue'),
    meta: { requiresAuth: true, requiresRole: 'admin' }
  },
  {
    path: '/unauthorized',
    name: 'Unauthorized',
    component: () => import('../views/Unauthorized.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/NotFound.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Role hierarchy for checking permissions
const roleHierarchy = {
  admin: 3,
  teacher: 2,
  student: 1,
  user: 0
}

// Navigation guards
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()

  // Wait for auth to initialize if still loading
  if (authStore.loading) {
    await authStore.initAuth()
  }

  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  const redirectIfAuth = to.matched.some(record => record.meta.redirectIfAuth)
  const requiresRole = to.meta.requiresRole

  // Redirect if already authenticated and trying to access login/register
  if (redirectIfAuth && authStore.isAuthenticated) {
    next({ name: 'Dashboard' })
    return
  }

  // Check if route requires authentication
  if (requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'Login', query: { redirect: to.fullPath } })
    return
  }

  // Check role-based access
  if (requiresRole && authStore.isAuthenticated) {
    const userLevel = roleHierarchy[authStore.userRole] || 0
    const requiredLevel = roleHierarchy[requiresRole] || 0

    if (userLevel < requiredLevel) {
      next({ name: 'Unauthorized' })
      return
    }
  }

  next()
})

export default router

