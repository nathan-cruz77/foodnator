<template>
  <v-app id="inspire">
    <toolbar :state="layout"/>
    <v-content>
      <v-container>
        <nuxt></nuxt>
      </v-container>
    </v-content>
    <le-footer/>
  </v-app>
</template>

<script>
import toolbar from '~/components/toolbar.vue'
import footer from '~/components/footer.vue'

export default {
  components: {
    toolbar,
    leFooter: footer
  },
  data: () => ({
    layout: {
      drawer: true,
    },
  }),
  computed: {
    snack () {
      return this.$store.getters.snack
    }
  }
}
</script>
