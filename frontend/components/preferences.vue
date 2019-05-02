<template>
  <v-navigation-drawer v-if="showPreferences" fixed right app>
    <v-list dense>
      <v-list-tile @click="toggleShowPreferences()">
        <v-list-tile-content>
          <v-list-tile-title>Preferences</v-list-tile-title>
        </v-list-tile-content>
        <v-list-tile-action>
          <v-icon>arrow_right_alt</v-icon>
        </v-list-tile-action>
      </v-list-tile>
      <v-list-tile/>

      <v-list-tile>
        <multi-select v-model="preferences.selectedCuisines" :options.sync="cuisines" label="Prefered cuisines"/>
      </v-list-tile>
      <v-list-tile/>

      <v-list-tile>
        <multi-select v-model="preferences.rejectedCuisines" :options.sync="cuisines" label="Rejected cuisines"/>
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
    preferences: {
      price: 1,
      freeDelivery: false,
      selectedCuisines: [],
      rejectedCuisines: [],
      rating: 0,
    },
    cuisines: [],
  }),

  components: {
    MultiSelect,
  },

  async mounted() {
    await this.fetchCuisines()
    this.cuisines = [...this.availableCuisines]
  },

  watch: {
    preferences: {
      handler() {
        this.updatePreferences({ ...this.preferences })
      },
      deep: true,
    },
  },

  computed: {
    ...mapState('user', { availableCuisines: 'cuisines' }),
    ...mapState('toolbar', ['showPreferences']),
  },
  methods: {
    ...mapActions('toolbar', ['toggleShowPreferences']),
    ...mapActions('user', ['fetchCuisines', 'updatePreferences']),
  },
}
</script>
