<template>
  <v-navigation-drawer v-if="showNewGroup" fixed app>
    <v-list dense>
      <v-list-tile @click="backToGroups()">
        <v-list-tile-action>
          <!-- This is here because material icons do not include a left version of arrow_right_alt -->
          <v-icon style="transform: rotate(180deg)">arrow_right_alt</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>New Group</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile/>

      <v-list-tile>
        <v-text-field label="Name" v-model="name" required/>
      </v-list-tile>
      <v-list-tile/>

      <v-list-tile>
        <v-autocomplete
          v-model="selectedUsers"
          :loading="loading"
          :items="users"
          :search-input.sync="userSearch"
          item-text="username"
          multiple
          cache-items
          chips
          hide-no-data
          hide-selected/>
      </v-list-tile>
      <v-list-tile/>

      <v-list-tile>
        <v-list-tile-content style="align-items: center">
          <v-btn :disabled="createDisabled" :class="btnClass" color="red">Create group</v-btn>
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'
import AppApi from '~apijs'

export default {
  data: () => ({
    name: '',
    selectedUsers: [],
    loading: false,
    users: [],
    userSearch: null,
  }),

  watch: {
    userSearch: _.debounce(async function(val) {
      if (!val) this.users = []

      this.loading = true
      const { data } = await AppApi.searchUsers(this.userSearch)
      this.users = data
      this.loading = false
    }, 300),
  },

  computed: {
    ...mapGetters('toolbar', ['showNewGroup']),
    createDisabled() {
      return !this.name || this.selectedUsers.length <= 0
    },
    btnClass() {
      if (this.createDisabled) {
        return ''
      }

      return 'white--text'
    },
  },

  methods: {
    ...mapActions('toolbar', ['backToGroups']),
  },
}
</script>
