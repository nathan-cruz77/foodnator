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
        <multi-select :options="cuisines" label="Cuisines"/>
      </v-list-tile>

      <v-list-tile>
        <v-list-tile-title v-if="price >= 200">
          Price: more than ${{ price }}
        </v-list-tile-title>
        <v-list-tile-title v-else>
          Price: up to ${{ price }}
        </v-list-tile-title>

        <v-slider v-model="price" type="number" :min="10" :max="200"/>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import MultiSelect from '~/components/multi-select'

export default {
  data: () => ({
    price: 10,
  }),

  components: {
    MultiSelect,
  },

  mounted() {
    this.fetchCuisines()
  },

  computed: {
    ...mapState(['showFilters', 'cuisines']),
  },
  methods: {
    ...mapActions(['toggleFilters', 'fetchCuisines']),
  },
}
</script>
