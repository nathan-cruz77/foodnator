<template>
  <v-toolbar color="white red--text" light fixed app>
    <v-toolbar-side-icon></v-toolbar-side-icon>
    <v-toolbar-title>Foodnator</v-toolbar-title>
    <v-spacer/>

    <v-btn v-if="!logged_user" flat ripple class="ma-0 ml-5" @click.stop="openLoginDialog($event)">Login</v-btn>
    <v-menu v-if="logged_user" offset-y>
      <v-btn icon slot="activator" class="ma-0 ml-5">
        <v-avatar size="36px">
          <img src="https://graph.facebook.com/4/picture?width=300&height=300">
        </v-avatar>
      </v-btn>
      <v-card class="no-padding">
        <v-list two-line>
          <v-list-tile avatar>
            <v-list-tile-avatar>
              <v-avatar>
                <img src="https://graph.facebook.com/4/picture?width=300&height=300">
              </v-avatar>
            </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title>{{logged_user.first_name}} {{logged_user.last_name}}</v-list-tile-title>
              <v-list-tile-sub-title>{{logged_user.email}}</v-list-tile-sub-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
        <v-divider></v-divider>
        <v-list>
          <v-list-tile @click="switchMode()">
            <v-list-tile-content>
              <v-list-tile-title>Staff mode</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile @click="logout()">
            <v-list-tile-content>
              <v-list-tile-title>Log out</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-card>
    </v-menu>
    <v-btn @click.stop="toggleFilters()" icon>
      <v-icon>settings</v-icon>
    </v-btn>
    <login-dialog ref="login_dialog"/>
  </v-toolbar>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import loginDialog from '~/components/login-dialog'
import AppApi from '~apijs'

export default {
  components: {
    loginDialog,
  },
  computed: {
    ...mapGetters(['logged_user']),
  },
  methods: {
    ...mapActions(['toggleFilters']),
    openLoginDialog (evt) {
      this.$refs.login_dialog.open();
      evt.stopPropagation();
    },
    logout(){
      AppApi.logout().then(() => this.$store.commit('SET_LOGGED_USER', null));
    }
  }
}
</script>
