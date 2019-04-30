<template>
  <v-app id="inspire">
    <toolbar/>
    <v-content>
      <v-container>
        <nuxt></nuxt>
      </v-container>
    </v-content>
    <filters/>
    <le-footer/>
  </v-app>
</template>

<script>
import toolbar from '~/components/toolbar'
import footer from '~/components/footer'
import Filters from '~/components/filters'

export default {
  components: {
    Filters,
    toolbar,
    leFooter: footer
  },
}
</script>
