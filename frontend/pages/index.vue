<template>
  <v-layout column justify-center align-center>
    <div class="display-2">Can't choose where to eat?</div>
    <div class="display-2">We got you covered!</div>
    <v-btn
      :loading="loading"
      :disabled="loading"
      @click="findRestaurant()"
      color="red darken-1 white--text"
      class="find-restaurant-button"
      large>
      Find restaurant
    </v-btn>
  </v-layout>
</template>

<script>
import { mapState } from 'vuex'
import AppApi from '~apijs'

export default {
  data: () => ({
    loading: false,
  }),

  computed: {
    ...mapState('user', ['selectedGroup']),
  },

  methods: {
    async findRestaurant() {
      this.loading = true
      const { data } = await AppApi.findRestaurant(this.selectedGroup)
      this.loading = false
      this.$router.push({ path: `/restaurant/${data}` })
    },
  },
}
</script>
