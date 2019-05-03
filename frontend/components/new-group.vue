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
        <v-text-field label="Name" v-model="name"/>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  data: () => ({
    name: '',
  }),

  computed: {
    ...mapGetters('toolbar', ['showNewGroup']),
  },

  methods: {
    ...mapActions('toolbar', ['backToGroups']),
  },
}
</script>
