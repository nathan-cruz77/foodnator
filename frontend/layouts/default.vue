<template>
  <v-app id="inspire">
    <groups/>
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
import Groups from '~/components/groups'

export default {
  components: {
    Groups,
    Preferences,
    toolbar,
    leFooter: footer
  },
}
</script>
