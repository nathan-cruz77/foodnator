<template>
  <v-navigation-drawer v-if="showGroups" fixed app>
    <v-list dense>
      <v-list-tile @click="toggleGroups()">
        <v-list-tile-action>
          <!-- This is here because material icons do not include a left version of arrow_right_alt -->
          <v-icon style="transform: rotate(180deg)">arrow_right_alt</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>Groups</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile/>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters('toolbar', ['showGroups']),
  },
  methods: {
    ...mapActions('toolbar', ['toggleGroups']),
  },
}
</script>
