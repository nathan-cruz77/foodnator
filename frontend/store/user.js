import AppApi from '~apijs'

export const state = () => ({
  loggedUser: undefined,
  cuisines: [],
  preferences: {},
  groups: [],
  selectedGroup: null,
})

export const actions = {
  async fetchCuisines({ commit }) {
    const { data } = await AppApi.cuisines()
    commit('setCuisines', data)
  },

  async fetchGroups({ commit, state }) {
    if (!state.loggedUser) return

    const { data } = await AppApi.groups(state.loggedUser.username)
    commit('setGroups', data)
  },

  selectGroup({ commit }, group) {
    commit('setSelectedGRoup', group)
  },

  updatePreferences({ commit, state }, preferences) {
    commit('setPreferences', preferences)

    if (state.loggedUser) {
      AppApi.updatePreferences(preferences)
    }
  },

  async login({ dispatch, commit }, { username, password }) {
    const { data } = await AppApi.login(username, password)
    const user = data

    if (user) {
      commit('setLoggedUser', user)
      dispatch('fetchGroups')
    }
  },
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

  setGroups(state, groups) {
    state.groups = groups
  },

  setSelectedGRoup(state, group) {
    state.selectedGroup = group
  }
}

export const getters = {
  loggedUser: ({ loggedUser }) => loggedUser,
  getPreferences: ({ preferences }) => preferences,
  groups: ({ groups }) => groups,
}
