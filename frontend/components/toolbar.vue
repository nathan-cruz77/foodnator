<template>
  <v-toolbar color="white red--text" light fixed app>
    <v-btn icon v-if="loggedUser" @click="toggleGroups()">
      <v-icon>group</v-icon>
    </v-btn>
    <v-toolbar-title>
      <v-card flat :to="{ name: 'index' }" color="red--text">Foodnator</v-card>
    </v-toolbar-title>
    <v-spacer/>

    <v-menu v-if="loggedUser" offset-y>
      <v-btn icon slot="activator" class="ma-0 ml-5">
        <v-avatar size="36px">
          <img src="https://www.w3schools.com/w3css/img_avatar3.png">
        </v-avatar>
      </v-btn>
      <v-card class="no-padding">
        <v-list two-line>
          <v-list-tile avatar>
            <v-list-tile-avatar>
              <v-avatar>
                <img src="https://www.w3schools.com/w3css/img_avatar3.png">
              </v-avatar>
            </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title>{{loggedUser.first_name}} {{loggedUser.last_name}}</v-list-tile-title>
              <v-list-tile-sub-title>{{loggedUser.email}}</v-list-tile-sub-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
        <v-divider></v-divider>
        <v-list>
          <v-list-tile @click="logout()">
            <v-list-tile-content>
              <v-list-tile-title>Log out</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-card>
    </v-menu>
    <v-btn v-else flat ripple class="ma-0 ml-5" @click.stop="openLoginDialog($event)">Login</v-btn>

    <login-dialog ref="login_dialog"/>
    <v-btn v-if="loggedUser" @click.stop="toggleShowPreferences()" icon>
      <v-icon>settings</v-icon>
    </v-btn>
  </v-toolbar>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from 'vuex'
import loginDialog from '~/components/login-dialog'
import AppApi from '~apijs'

export default {
  components: {
    loginDialog,
  },
  computed: {
    ...mapGetters('user', ['loggedUser']),
  },
  methods: {
    ...mapActions('toolbar', ['toggleShowPreferences', 'toggleGroups', 'closeTabs']),
    ...mapMutations('user', ['setLoggedUser']),
    openLoginDialog (evt) {
      this.$refs.login_dialog.open();
      evt.stopPropagation();
    },
    async logout(){
      await AppApi.logout()
      this.closeTabs()
      this.setLoggedUser(null)
    }
  },
}
</script>
