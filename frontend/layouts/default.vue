<template>
  <v-app id="inspire">
    <sidenav-left/>
    <toolbar/>
    <v-content>
      <v-container>
        <nuxt></nuxt>
      </v-container>
    </v-content>
    <le-footer/>
  </v-app>
</template>

<script>
import toolbar from '~/components/toolbar'
import footer from '~/components/footer'
import SidenavLeft from '~/components/sidenav-left'

export default {
  components: {
    SidenavLeft,
    toolbar,
    leFooter: footer
  },
}
</script>
