<template>
  <v-layout column justify-center align-center>
    <div class="display-2">Can't choose where to eat?</div>
    <div class="display-2">We got you covered!</div>
    <find-restaurant class="find-restaurant-button"/>
  </v-layout>
</template>

<script>
import { mapState } from 'vuex'
import AppApi from '~apijs'
import FindRestaurant from '~/components/find-restaurant'

export default {
  components: {
    FindRestaurant,
  },
}
</script>
