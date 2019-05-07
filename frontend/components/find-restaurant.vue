<template>
  <v-btn :loading="loading" :disabled="loading" @click="findRestaurant()" large color="red darken-1 white--text">
    {{ label }}
  </v-btn>
</template>

<script>
import { mapState } from 'vuex'
import AppApi from '~apijs'

export default {
  props: {
    label: {
      type: String,
      required: false,
      default: 'Find Restaurant',
    },
  },

  data: () => ({
    loading: false,
  }),

  computed: {
    ...mapState('user', ['selectedGroup']),
  },

  methods: {
    async findRestaurant() {
      this.loading = true
      const { data } = await AppApi.findRestaurant(this.selectedGroup)
      this.loading = false
      this.$router.push({ path: `/restaurant/${data}` })
    },
  },
}
</script>
