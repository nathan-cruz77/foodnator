<template>
  <v-footer color="blue-grey" class="white--text" app>
    <v-spacer></v-spacer>
    <span>&copy; {{ year }}</span>
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
