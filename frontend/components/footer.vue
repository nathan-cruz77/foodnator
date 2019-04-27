<template>
  <v-footer color="red lighten-2" class="white--text" app>
    <v-layout justify-center row wrap>
      <span>&copy; {{ year }} - Foodnator</span>
    </v-layout>
  </v-footer>
</template>

<script>
  export default {
    props: ['state'],
    computed: {
      year: () => (new Date()).getFullYear(),
    }
  }
</script>
