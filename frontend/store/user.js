import AppApi from '~apijs'

export const state = () => ({
  loggedUser: undefined,
  cuisines: [],
  preferences: {},
})

export const actions = {
  async fetchCuisines({ commit }) {
    const { data } = await AppApi.cuisines()
    commit('setCuisines', data)
  },
  updatePreferences({ commit, state }, preferences) {
    commit('setPreferences', preferences)

    if (state.loggedUser) {
      AppApi.update_preferences(preferences)
    }
  }
}

export const mutations = {
  setLoggedUser(state, loggedUser) {
    console.log(`set logged user: ${JSON.stringify(loggedUser)}`)
    state.loggedUser = loggedUser
  },

  setCuisines(state, cuisines) {
    state.cuisines = cuisines
  },

  setPreferences(state, preferences) {
    state.preferences = preferences
  },
}

export const getters = {
  loggedUser: ({ loggedUser }) => loggedUser,
  getPreferences: ({ preferences }) => preferences,
}
