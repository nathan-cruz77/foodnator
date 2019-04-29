<template>
  <v-footer color="red--text" app>
    <v-layout justify-center row wrap>
      <span>&copy; {{ year }} - Foodnator</span>
    </v-layout>
  </v-footer>
</template>

<script>
  export default {
    computed: {
      year: () => (new Date()).getFullYear(),
    }
  }
</script>
