<template>
  <v-dialog v-model="visible" max-width="500px">
    <v-card>
        <v-card-title>Log in</v-card-title>
        <v-card-text>
          <v-container fluid>
            <v-text-field label="Username" required v-model="username"/>
            <v-text-field label="Password" type="password" required v-model="password" @keyup.enter="login()"/>
            <small style="color: red" v-if="error">Wrong user or password</small>
          </v-container>
        </v-card-text>
        <v-btn class="blue--text darken-1" flat @click="close()">Cancel</v-btn>
        <v-btn class="blue--text darken-1" flat @click="login()" :loading="loading" :disabled="loading">Login</v-btn>
    </v-card>
  </v-dialog>
</template>

<script>
import AppApi from '~apijs'
import { mapMutations } from 'vuex'

export default {
  data: () => ({
    visible: false,
    loading: false,
    username: '',
    password: '',
    error: false,
  }),

  methods: {
    ...mapMutations('user', ['setLoggedUser']),
    open(){
      this.visible = true
    },
    close(){
      this.visible = false
    },
    async login(){
      this.loading = true
      this.error = false

      const { data } = await AppApi.login(this.username, this.password)
      const user = data

      if(user) {
        this.setLoggedUser(user)
        this.visible = false
      } else {
        this.error = true
      }

      this.loading = false
    },
  },
}
</script>
