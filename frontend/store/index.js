import Vuex from 'vuex'
import AppApi from '~apijs'

const store = () => new Vuex.Store({
  state: {
    logged_user: undefined,
    showFilters: false,
    cuisines: []
  },

  actions: {
    toggleFilters({ commit, state }) {
      commit('setShowFilters', !state.showFilters)
    },

    async fetchCuisines({ commit }) {
      const { data } = await AppApi.cuisines()
      commit('setCuisines', data)
    },
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
  },

  getters: {
    logged_user(state) {
      return state.logged_user
    },
  },
})

export default store
