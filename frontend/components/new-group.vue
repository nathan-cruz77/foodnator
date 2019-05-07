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
          clearable
          multiple
          cache-items
          chips
          hide-no-data
          hide-selected>

          <template slot="selection" slot-scope="{ selected, item, index }">
            <v-chip @input="remove(index)" :selected="selected" close class="chip--select-multi">
              {{ item }}
            </v-chip>
          </template>

        </v-autocomplete>
      </v-list-tile>
      <v-list-tile/>

      <v-list-tile>
        <v-list-tile-content style="align-items: center">
          <v-btn
            @click="createGroup()"
            :disabled="createDisabled"
            :class="btnClass"
            :loading="creatingGroup"
            color="red">
            Create group
          </v-btn>
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
    creatingGroup: false,
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
    ...mapActions('user', ['newGroup']),
    async createGroup() {
      this.creatingGroup = true
      await this.newGroup({ name: this.name, users: this.selectedUsers })
      this.clearData()
      this.backToGroups()
    },
    remove(index) {
      if (index >= 0) this.selectedUsers.splice(index, 1)
    },
    clearData() {
      this.name = ''
      this.selectedUsers = []
      this.loading = false
      this.users = []
      this.userSearch = null
      this.creatingGroup = false
    }
  },
}
</script>
