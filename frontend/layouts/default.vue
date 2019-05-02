<template>
  <v-app id="inspire">
    <toolbar/>
    <v-content>
      <v-container>
        <nuxt></nuxt>
      </v-container>
    </v-content>
    <preferences/>
    <le-footer/>
  </v-app>
</template>

<script>
import toolbar from '~/components/toolbar'
import footer from '~/components/footer'
import Preferences from '~/components/preferences'

export default {
  components: {
    Preferences,
    toolbar,
    leFooter: footer
  },
}
</script>
