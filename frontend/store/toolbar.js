export const state = () => ({
    showPreferences: false,
    leftTab: null,
})

export const actions = {
  toggleShowPreferences({ commit, state }) {
    commit('setShowPreferences', !state.showPreferences)
  },

  toggleGroups({ commit, state }) {
    const { leftTab } = state

    if (leftTab === null) {
      commit('setLeftTab', 'groups')
    } else {
      commit('setLeftTab', null)
    }
  },

  newGroup({ commit }) {
    commit('setLeftTab', 'newGroup')
  },

  backToGroups({ commit }) {
    commit('setLeftTab', 'groups')
  },

  closeTabs({ commit }) {
    commit('setLeftTab', null)
    commit('setShowPreferences', false)
  },
}

export const mutations = {
  setShowPreferences(state, value) {
    state.showPreferences = value
  },
  setLeftTab(state, value) {
    state.leftTab = value
  }
}

export const getters = {
  showGroups: ({ leftTab }) => leftTab === 'groups',
  showNewGroup: ({ leftTab }) => leftTab === 'newGroup',
}
