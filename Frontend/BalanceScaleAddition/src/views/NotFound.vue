<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-600 via-purple-700 to-purple-900 p-8">
    <div class="bg-gray-800 p-12 rounded-3xl text-center max-w-lg border border-gray-700">
      <span class="text-8xl block mb-6">❓</span>
      <h1 class="text-4xl font-bold text-gray-100 mb-4">404 - Page Not Found</h1>
      <p class="text-gray-400 mb-8 text-lg">The page you're looking for doesn't exist.</p>
      <router-link to="/" class="inline-block px-8 py-3 bg-purple-600 hover:bg-purple-700 text-white font-semibold rounded-xl transition-all duration-200 hover:-translate-y-1">
        Go Home
      </router-link>
    </div>
  </div>
</template>
