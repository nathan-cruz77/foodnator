<template>
  <v-dialog v-model="visible" max-width="500px">
    <v-card>
        <v-card-title>Sign up</v-card-title>
        <v-card-text>
          <v-container fluid>
            <v-text-field label="Username" required v-model="username"/>
            <v-text-field label="Email" required v-model="email"/>
            <v-text-field label="Password" type="password" required v-model="password" @keyup.enter="createUser()"/>
            <small style="color: red" v-if="error">Username already in use</small>
          </v-container>
        </v-card-text>
        <v-btn class="blue--text darken-1" flat @click="close()">Cancel</v-btn>
        <v-btn class="blue--text darken-1" flat @click="createUser()" :loading="loading" :disabled="loading">Sign up</v-btn>
    </v-card>
  </v-dialog>
</template>

<script>
import AppApi from '~apijs'
import { mapActions, mapGetters } from 'vuex'

export default {
  data: () => ({
    visible: false,
    loading: false,
    error: false,
    username: '',
    email: '',
    password: '',
  }),

  computed: {
    ...mapGetters('user', ['loggedUser']),
  },

  methods: {
    ...mapActions('user', ['login']),
    open(){
      this.visible = true
    },
    close(){
      this.visible = false
    },
    async createUser(){
      this.loading = true
      this.error = false

      const { data } = await AppApi.newUser({
        username: this.username,
        email: this.email,
        password: this.password,
      })

      console.log(`New User data: ${JSON.stringify(data)}`)

      if (data.created) {
        await this.login({ username: this.username, password: this.password })
        this.visible = false
      } else {
        this.error = true
      }

      this.loading = false
    },
  },
}
</script>
