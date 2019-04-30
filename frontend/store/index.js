import Vuex from 'vuex'
import AppApi from '~apijs'

const store = () => new Vuex.Store({
  state: {
    logged_user: undefined,
    showFilters: false,
    cuisines: [],
    preferences: {
      price: 1,
      freeDelivery: false,
      selectedCuisines: [],
      rejectedCuisines: [],
      rating: 0,
    },
  },

  actions: {
    toggleFilters({ commit, state }) {
      commit('setShowFilters', !state.showFilters)
    },

    async fetchCuisines({ commit }) {
      const { data } = await AppApi.cuisines()
      commit('setCuisines', data)
    },

    updatePreferences({ commit, state }, preferences) {
      commit('setPreferences', preferences)

      if (state.logged_user) {
        AppApi.update_preferences(preferences)
      }
    }
  },

  mutations: {
    SET_LOGGED_USER(state, logged_user) {
      console.log(`set logged user: ${JSON.stringify(logged_user)}`)
      state.logged_user = logged_user
    },

    setShowFilters(state, value) {
      state.showFilters = value
    },

    setCuisines(state, cuisines) {
      state.cuisines = cuisines
    },

    setPreferences(state, preferences) {
      state.preferences = preferences
    },
  },

  getters: {
    logged_user: ({ logged_user }) => logged_user,
    getPreferences: ({ preferences }) => preferences,
  },
})

export default store
