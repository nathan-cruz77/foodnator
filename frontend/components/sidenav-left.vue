<template>
  <v-navigation-drawer v-if="showFilters" fixed app>
    <v-list dense>
      <v-list-tile @click="toggleFilters()">
        <v-list-tile-action>
          <v-icon>keyboard_backspace</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>Preferences</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile/>

      <v-list-tile>
        <multi-select v-model="preferences.selectedCuisines" :options="cuisines" label="Prefered cuisines"/>
      </v-list-tile>
      <v-list-tile/>

      <v-list-tile>
        <multi-select v-model="preferences.rejectedCuisines" :options="cuisines" label="Rejected cuisines"/>
      </v-list-tile>
      <v-list-tile/>

      <v-list-tile>
        <v-list-tile-title>
          Price:
          <template v-for="i in preferences.price">
            <span style="display: none">{{ i }}</span>
            <v-icon color="green accent-4" small>attach_money</v-icon>
          </template>
        </v-list-tile-title>

        <v-slider v-model="preferences.price" type="number" :min="1" :max="5"/>
      </v-list-tile>
      <v-list-tile/>

      <v-list-tile>
        <v-list-tile-title>Free delivery: </v-list-tile-title>
        <v-switch color="green accent-4" v-model="preferences.freeDelivery"/>
      </v-list-tile>
      <v-list-tile/>

      <v-list-tile>
        <v-list-tile-title>Rating at least {{ preferences.rating }}</v-list-tile-title>
        <v-slider v-model="preferences.rating" min="0" max="5"/>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'
import MultiSelect from '~/components/multi-select'

export default {
  data: () => ({
    preferences: {},
  }),

  components: {
    MultiSelect,
  },

  mounted() {
    this.preferences = { ...this.getPreferences() }
    this.fetchCuisines()
  },

  watch: {
    preferences() {
      this.updatePreferences(this.preferences)
    },
  },

  computed: {
    ...mapState(['showFilters', 'cuisines']),
  },
  methods: {
    ...mapActions(['toggleFilters', 'fetchCuisines', 'updatePreferences']),
    ...mapGetters(['getPreferences']),
  },
}
</script>
