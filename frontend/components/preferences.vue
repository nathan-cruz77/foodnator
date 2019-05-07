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
        <multi-select
          v-model="preferences.selectedCuisines"
          :options="availableSelectionCuisines"
          label="Prefered cuisines"/>
      </v-list-tile>
      <v-list-tile/>

      <v-list-tile>
        <multi-select
          v-model="preferences.rejectedCuisines"
          :options="availableRejectionCuisines"
          label="Rejected cuisines"/>
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
import _ from 'lodash'
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
    availableSelectionCuisines: [],
    availableRejectionCuisines: [],
  }),

  components: {
    MultiSelect,
  },

  async mounted() {
    await this.fetchCuisines()
    await this.loadPreferences()

    this.availableSelectionCuisines = _.cloneDeep(this.cuisines)
    this.availableRejectionCuisines = _.cloneDeep(this.cuisines)

    this.preferences = _.cloneDeep(this.storePreferences)
  },

  watch: {
    preferences: {
      handler() {
        this.updatePreferences(_.cloneDeep(this.preferences))
      },
      deep: true,
    },

    'preferences.selectedCuisines'() {
      this.availableRejectionCuisines = _.difference(this.cuisines, this.preferences.selectedCuisines)
    },

    'preferences.rejectedCuisines'() {
      this.availableSelectionCuisines = _.difference(this.cuisines, this.preferences.rejectedCuisines)
    },
  },

  computed: {
    ...mapState('user', ['cuisines']),
    ...mapState('user', { storePreferences: 'preferences' }),
    ...mapState('toolbar', ['showPreferences']),
  },
  methods: {
    ...mapActions('toolbar', ['toggleShowPreferences']),
    ...mapActions('user', ['fetchCuisines', 'updatePreferences', 'loadPreferences']),
  },
}
</script>
