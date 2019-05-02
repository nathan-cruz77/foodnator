export const state = () => ({
    showPreferences: false,
})

export const actions = {
  toggleShowPreferences({ commit, state }) {
    commit('setShowPreferences', !state.showPreferences)
  },
}

export const mutations = {
  setShowPreferences(state, value) {
    state.showPreferences = value
  },
}
