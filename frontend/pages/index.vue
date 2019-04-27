<template>
  <v-layout column justify-center align-center>
    <div class="display-2">Can't choose where to eat?</div>
    <div class="display-2">We got you covered!</div>
    <v-btn color="red darken-1" large @click="findRestaurant()">Find restaurant</v-btn>
  </v-layout>
</template>

<script>
export default {
  methods: {
    findRestaurant() {
      console.log('Pede no to de boa')
    },
  },
}
</script>
