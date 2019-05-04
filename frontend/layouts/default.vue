<template>
  <v-app id="inspire">
    <groups/>
    <new-group/>
    <toolbar/>
    <v-content>
      <v-container fill-height>
        <nuxt></nuxt>
      </v-container>
    </v-content>
    <preferences/>
    <le-footer/>
  </v-app>
</template>

<script>
import Toolbar from '~/components/toolbar'
import Footer from '~/components/footer'
import Preferences from '~/components/preferences'
import Groups from '~/components/groups'
import NewGroup from '~/components/new-group'

export default {
  components: {
    NewGroup,
    Groups,
    Preferences,
    Toolbar,
    leFooter: Footer
  },
}
</script>
