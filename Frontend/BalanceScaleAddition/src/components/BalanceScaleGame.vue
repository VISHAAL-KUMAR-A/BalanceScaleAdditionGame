<template>
  <div class="balance-game-container min-h-screen px-4 py-8 md:px-6 md:py-12">
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <div class="text-center mb-8 md:mb-12">
        <h1 class="text-3xl md:text-5xl font-bold text-gray-100 mb-4">⚖️ Balance Scale Addition</h1>
        <p class="text-base md:text-lg text-gray-300 mb-6">Find numbers that add up to balance the scale!</p>
        
        <!-- Difficulty Selector -->
        <div class="flex justify-center gap-2 md:gap-4 mb-6">
          <button
            v-for="level in ['easy', 'medium', 'hard']"
            :key="level"
            @click="selectDifficulty(level)"
            :class="[
              'px-4 md:px-6 py-2 md:py-3 rounded-xl font-semibold text-sm md:text-base transition-all duration-300',
              difficulty === level 
                ? 'bg-purple-600 text-white scale-110 shadow-lg' 
                : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
            ]"
          >
            {{ level.charAt(0).toUpperCase() + level.slice(1) }}
          </button>
        </div>

        <!-- Score Display -->
        <div class="flex justify-center gap-4 md:gap-8 text-gray-300">
          <div class="bg-gray-800 px-4 md:px-6 py-2 rounded-xl border border-gray-700">
            <span class="text-xs md:text-sm">Score: </span>
            <span class="text-lg md:text-xl font-bold text-purple-400">{{ totalScore }}</span>
          </div>
          <div class="bg-gray-800 px-4 md:px-6 py-2 rounded-xl border border-gray-700">
            <span class="text-xs md:text-sm">Time: </span>
            <span class="text-lg md:text-xl font-bold text-blue-400">{{ formatTime(elapsedTime) }}</span>
          </div>
        </div>
      </div>

      <!-- Balance Scale Visualization -->
      <div class="balance-scale-wrapper mb-8 md:mb-12">
        <div class="scale-container relative" :class="scaleClass">
          <!-- Center Pole -->
          <div class="center-pole absolute left-1/2 transform -translate-x-1/2 bg-gray-600 w-3 md:w-4 h-32 md:h-48 rounded-t-lg" style="top: 20%"></div>
          
          <!-- Balance Beam -->
          <div class="balance-beam absolute left-1/2 transform -translate-x-1/2 bg-gradient-to-r from-gray-500 via-gray-400 to-gray-500 h-3 md:h-4 rounded-full shadow-2xl transition-all duration-700 ease-in-out"
               :style="beamStyle"
               style="width: 80%; max-width: 600px; top: 20%">
            <div class="absolute -top-1 left-1/2 transform -translate-x-1/2 w-4 md:w-6 h-4 md:h-6 bg-yellow-500 rounded-full shadow-lg"></div>
          </div>

          <!-- Left Pan (Target) -->
          <div class="scale-pan left-pan absolute transition-all duration-700 ease-in-out"
               :style="leftPanStyle">
            <div class="pan-content bg-gradient-to-br from-purple-600 to-purple-800 rounded-2xl md:rounded-3xl p-4 md:p-8 shadow-2xl border-4 border-purple-500 transform hover:scale-105 transition-transform">
              <div class="text-center">
                <div class="text-xs md:text-sm text-purple-200 mb-2">Target</div>
                <div class="text-4xl md:text-6xl font-bold text-white">{{ targetNumber }}</div>
                <div class="text-xs md:text-sm text-purple-200 mt-2">🎯</div>
              </div>
            </div>
            <div class="chain absolute w-1 bg-gray-600 h-12 md:h-20 left-1/2 transform -translate-x-1/2 -top-12 md:-top-20"></div>
          </div>

          <!-- Right Pan (User Input) -->
          <div class="scale-pan right-pan absolute transition-all duration-700 ease-in-out"
               :style="rightPanStyle">
            <div class="pan-content bg-gradient-to-br from-blue-600 to-blue-800 rounded-2xl md:rounded-3xl p-4 md:p-8 shadow-2xl border-4 border-blue-500 transform hover:scale-105 transition-transform">
              <div class="text-center">
                <div class="text-xs md:text-sm text-blue-200 mb-2">Your Sum</div>
                <div class="text-4xl md:text-6xl font-bold text-white">{{ currentSum }}</div>
                <div class="text-xs md:text-sm text-blue-200 mt-2">
                  {{ currentSum > targetNumber ? '⬆️ Too Heavy' : currentSum < targetNumber ? '⬇️ Too Light' : '✅ Perfect!' }}
                </div>
              </div>
            </div>
            <div class="chain absolute w-1 bg-gray-600 h-12 md:h-20 left-1/2 transform -translate-x-1/2 -top-12 md:-top-20"></div>
          </div>
        </div>
      </div>

      <!-- Input Section -->
      <div class="input-section max-w-2xl mx-auto mb-8">
        <div class="bg-gray-800 rounded-2xl p-4 md:p-8 border-2 border-gray-700 shadow-xl">
          <h3 class="text-lg md:text-xl font-bold text-gray-100 mb-4 text-center">Enter Your Numbers</h3>
          
          <div class="flex flex-wrap gap-2 md:gap-3 mb-4 justify-center">
            <div v-for="(num, index) in userNumbers" :key="index" class="flex items-center gap-2">
              <input
                v-model.number="userNumbers[index]"
                type="number"
                min="1"
                :max="maxValue"
                @input="updateSum"
                class="w-16 md:w-20 px-3 py-2 md:py-3 bg-gray-700 text-white text-center text-lg md:text-xl font-bold rounded-xl border-2 border-gray-600 focus:border-purple-500 focus:outline-none transition-colors"
                placeholder="?"
              />
              <button
                v-if="userNumbers.length > 1"
                @click="removeNumber(index)"
                class="text-red-400 hover:text-red-300 transition-colors p-1"
                title="Remove"
              >
                ✕
              </button>
            </div>
          </div>

          <div class="flex flex-col sm:flex-row gap-3 justify-center">
            <button
              @click="addNumber"
              :disabled="userNumbers.length >= maxAddends"
              class="px-4 md:px-6 py-2 md:py-3 bg-green-600 hover:bg-green-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-semibold rounded-xl transition-colors text-sm md:text-base"
            >
              ➕ Add Number
            </button>
            
            <button
              @click="submitAnswer"
              :disabled="!canSubmit"
              class="px-4 md:px-6 py-2 md:py-3 bg-purple-600 hover:bg-purple-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-semibold rounded-xl transition-colors text-sm md:text-base"
            >
              ✓ Check Answer
            </button>

            <button
              @click="newGame"
              class="px-4 md:px-6 py-2 md:py-3 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-xl transition-colors text-sm md:text-base"
            >
              🔄 New Game
            </button>
          </div>

          <!-- Hints -->
          <div v-if="hintsEnabled && hint" class="mt-4 p-3 md:p-4 bg-yellow-900/30 border border-yellow-600 rounded-xl text-yellow-200 text-center text-sm md:text-base">
            💡 {{ hint }}
          </div>
        </div>
      </div>

      <!-- Feedback Section -->
      <div v-if="feedback" class="feedback-section max-w-2xl mx-auto">
        <div :class="[
          'p-4 md:p-6 rounded-2xl text-center font-semibold text-base md:text-lg animate-bounce-in border-2',
          feedbackClass
        ]">
          {{ feedback }}
        </div>
      </div>

      <!-- Progress Stats -->
      <div v-if="progress" class="progress-section max-w-4xl mx-auto mt-8 md:mt-12">
        <h3 class="text-xl md:text-2xl font-bold text-gray-100 mb-4 md:mb-6 text-center">Your Progress</h3>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 md:gap-4">
          <div class="bg-gray-800 p-4 md:p-6 rounded-xl border border-gray-700 text-center">
            <div class="text-2xl md:text-3xl font-bold text-purple-400">{{ progress.total_games }}</div>
            <div class="text-xs md:text-sm text-gray-400 mt-1">Games Played</div>
          </div>
          <div class="bg-gray-800 p-4 md:p-6 rounded-xl border border-gray-700 text-center">
            <div class="text-2xl md:text-3xl font-bold text-green-400">{{ progress.correct_games }}</div>
            <div class="text-xs md:text-sm text-gray-400 mt-1">Correct</div>
          </div>
          <div class="bg-gray-800 p-4 md:p-6 rounded-xl border border-gray-700 text-center">
            <div class="text-2xl md:text-3xl font-bold text-blue-400">{{ progress.accuracy_percentage.toFixed(1) }}%</div>
            <div class="text-xs md:text-sm text-gray-400 mt-1">Accuracy</div>
          </div>
          <div class="bg-gray-800 p-4 md:p-6 rounded-xl border border-gray-700 text-center">
            <div class="text-2xl md:text-3xl font-bold text-yellow-400">{{ progress.total_score }}</div>
            <div class="text-xs md:text-sm text-gray-400 mt-1">Total Score</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import apiClient from '../api/axios'
import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()

// Game State
const difficulty = ref('easy')
const targetNumber = ref(10)
const userNumbers = ref([])
const currentSum = ref(0)
const feedback = ref('')
const totalScore = ref(0)
const maxAddends = ref(3)
const maxValue = ref(10)
const minValue = ref(1)
const hintsEnabled = ref(true)
const hint = ref('')
const elapsedTime = ref(0)
const timerInterval = ref(null)
const gameStartTime = ref(null)
const progress = ref(null)

// Computed Properties
const canSubmit = computed(() => {
  return userNumbers.value.length > 0 && 
         userNumbers.value.every(num => num > 0 && num <= maxValue.value)
})

const difference = computed(() => currentSum.value - targetNumber.value)

const tiltAngle = computed(() => {
  const maxTilt = 15 // Maximum tilt angle in degrees
  const diff = difference.value
  if (diff === 0) return 0
  
  // Calculate tilt proportional to difference, capped at maxTilt
  const tilt = Math.min(Math.abs(diff) * 2, maxTilt)
  return diff > 0 ? tilt : -tilt
})

const scaleClass = computed(() => {
  if (currentSum.value === targetNumber.value && currentSum.value > 0) {
    return 'balanced'
  } else if (currentSum.value > targetNumber.value) {
    return 'tilt-right'
  } else if (currentSum.value < targetNumber.value && currentSum.value > 0) {
    return 'tilt-left'
  }
  return ''
})

const beamStyle = computed(() => {
  return {
    transform: `translateX(-50%) rotate(${tiltAngle.value}deg)`
  }
})

const leftPanStyle = computed(() => {
  const basePosTop = 20 // percentage
  const basePosLeft = 10 // percentage
  const verticalShift = Math.sin((tiltAngle.value * Math.PI) / 180) * 15
  
  return {
    left: `${basePosLeft}%`,
    top: `${basePosTop + verticalShift}%`
  }
})

const rightPanStyle = computed(() => {
  const basePosTop = 20
  const basePosRight = 10
  const verticalShift = -Math.sin((tiltAngle.value * Math.PI) / 180) * 15
  
  return {
    right: `${basePosRight}%`,
    top: `${basePosTop + verticalShift}%`
  }
})

const feedbackClass = computed(() => {
  if (feedback.value.includes('Perfect') || feedback.value.includes('Correct')) {
    return 'bg-green-900/50 text-green-200 border-green-500'
  } else if (feedback.value.includes('close') || feedback.value.includes('Almost')) {
    return 'bg-yellow-900/50 text-yellow-200 border-yellow-500'
  } else {
    return 'bg-red-900/50 text-red-200 border-red-500'
  }
})

// Methods
const selectDifficulty = async (level) => {
  difficulty.value = level
  await loadGameConfig()
}

const loadGameConfig = async () => {
  try {
    const response = await apiClient.post('/api/game/config', {
      difficulty: difficulty.value
    })
    
    targetNumber.value = response.data.target_number
    maxAddends.value = response.data.max_addends
    maxValue.value = response.data.max_value
    minValue.value = response.data.min_value
    hintsEnabled.value = response.data.hints_enabled
    
    // Reset game state
    userNumbers.value = []
    currentSum.value = 0
    feedback.value = ''
    hint.value = ''
    
    // Start timer
    startTimer()
  } catch (error) {
    console.error('Failed to load game config:', error)
    feedback.value = 'Failed to load game. Please try again.'
  }
}

const updateSum = () => {
  currentSum.value = userNumbers.value.reduce((sum, num) => sum + (num || 0), 0)
  
  // Update hint
  if (hintsEnabled.value) {
    const diff = difference.value
    if (diff > 0) {
      hint.value = `Your sum is ${Math.abs(diff)} more than the target. Try smaller numbers or remove some.`
    } else if (diff < 0) {
      hint.value = `Your sum is ${Math.abs(diff)} less than the target. Try larger numbers or add more.`
    } else if (currentSum.value > 0) {
      hint.value = 'Perfect! Your sum matches the target! Submit your answer!'
    } else {
      hint.value = `Try to make ${targetNumber.value} using numbers between ${minValue.value} and ${maxValue.value}.`
    }
  }
}

const addNumber = () => {
  if (userNumbers.value.length < maxAddends.value) {
    userNumbers.value.push(0)
  }
}

const removeNumber = (index) => {
  userNumbers.value.splice(index, 1)
  updateSum()
}

const submitAnswer = async () => {
  if (!canSubmit.value) return
  
  const timeSpent = Math.floor((Date.now() - gameStartTime.value) / 1000)
  
  try {
    const response = await apiClient.post('/api/game/submit', {
      target_number: targetNumber.value,
      user_answer: userNumbers.value.filter(n => n > 0),
      difficulty: difficulty.value,
      time_spent_seconds: timeSpent
    })
    
    feedback.value = response.data.feedback
    totalScore.value += response.data.score
    
    // Stop timer
    stopTimer()
    
    // Load updated progress
    await loadProgress()
    
    // Auto-start new game after correct answer
    if (response.data.is_correct) {
      setTimeout(() => {
        newGame()
      }, 3000)
    }
  } catch (error) {
    console.error('Failed to submit answer:', error)
    feedback.value = 'Failed to submit answer. Please try again.'
  }
}

const newGame = async () => {
  await loadGameConfig()
}

const loadProgress = async () => {
  try {
    const response = await apiClient.get('/api/game/progress')
    progress.value = response.data
  } catch (error) {
    console.error('Failed to load progress:', error)
  }
}

const startTimer = () => {
  stopTimer()
  gameStartTime.value = Date.now()
  elapsedTime.value = 0
  timerInterval.value = setInterval(() => {
    elapsedTime.value = Math.floor((Date.now() - gameStartTime.value) / 1000)
  }, 1000)
}

const stopTimer = () => {
  if (timerInterval.value) {
    clearInterval(timerInterval.value)
    timerInterval.value = null
  }
}

const formatTime = (seconds) => {
  const mins = Math.floor(seconds / 60)
  const secs = seconds % 60
  return `${mins}:${secs.toString().padStart(2, '0')}`
}

// Lifecycle
onMounted(async () => {
  await loadGameConfig()
  await loadProgress()
})

onUnmounted(() => {
  stopTimer()
})

// Watch for changes
watch(userNumbers, () => {
  updateSum()
}, { deep: true })
</script>

<style scoped>
.balance-game-container {
  background: linear-gradient(to bottom, #1a1a2e, #0f0f1e);
  min-height: 100vh;
}

.scale-container {
  height: 400px;
  position: relative;
  margin: 0 auto;
}

@media (max-width: 768px) {
  .scale-container {
    height: 350px;
  }
}

.scale-pan {
  width: 140px;
}

@media (min-width: 768px) {
  .scale-pan {
    width: 180px;
  }
}

.balanced {
  animation: balance-success 1s ease-in-out;
}

@keyframes balance-success {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.02); }
}

.tilt-left .balance-beam {
  animation: wobble 0.5s ease-in-out;
}

.tilt-right .balance-beam {
  animation: wobble 0.5s ease-in-out;
}

@keyframes wobble {
  0%, 100% { transform: translateX(-50%) rotate(var(--angle, 0deg)); }
  25% { transform: translateX(-50%) rotate(calc(var(--angle, 0deg) * 1.1)); }
  75% { transform: translateX(-50%) rotate(calc(var(--angle, 0deg) * 0.9)); }
}

@keyframes animate-bounce-in {
  0% {
    opacity: 0;
    transform: scale(0.5);
  }
  50% {
    opacity: 1;
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}

.animate-bounce-in {
  animation: animate-bounce-in 0.5s ease-out;
}

/* Remove spinner from number input */
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type="number"] {
  -moz-appearance: textfield;
}
</style>

