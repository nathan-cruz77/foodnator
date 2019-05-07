<template>
  <v-layout v-if="loggedUser" column justify-center align-center>
    <div class="display-2">Can't choose where to eat?</div>
    <div class="display-2">We got you covered!</div>
    <find-restaurant class="find-restaurant-button"/>
  </v-layout>
  <v-layout v-else column justify-center align-center >
    <div class="display-2">Find the best restaurants for your group or you!</div>
    <div class="display-2">Login to get started</div>
  </v-layout>
</template>

<script>
import { mapState } from 'vuex'
import FindRestaurant from '~/components/find-restaurant'

export default {
  components: {
    FindRestaurant,
  },

  computed: {
    ...mapState('user', ['loggedUser']),
  },
}
</script>
