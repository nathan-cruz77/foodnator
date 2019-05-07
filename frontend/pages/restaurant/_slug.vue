<template>
  <div class="container--centralized flex-column full-width">
    <v-card class="container--centralized">
      <div class="image-container container--centralized">
        <img class="image" :src="restaurant.avatar">
      </div>
      <div class="container--column">
        <div class="item text-vertical-centralized restaurant-name">{{ restaurant.name }}</div>
        <div class="item text-vertical-centralized restaurant-cuisine">{{ restaurant.cuisine }}</div>
        <div class="item text-vertical-centralized">
          <span v-if="parseFloat(restaurant.delivery_fee) == 0" class="restaurant-delivery restaurant-delivery--free">
            FREE DELIVERY
          </span>
          <span v-else class="restaurant-delivery">
            DELIVERY ${{ restaurant.delivery_fee }}
          </span>
        </div>
        <div class="item text-vertical-centralized">
          <div class="restaurant-rating">
            <v-icon color="rgba(230, 166, 76, 1)">star</v-icon>
            {{ restaurant.rating }}
          </div>
          <div class="restaurant-price">
            <template v-for="i in restaurant.price_range">
              <span color="green accent-4">$</span>
              <span style="display: none">{{ i }}</span>
            </template>
          </div>
        </div>
      </div>
    </v-card>

    <v-btn :loading="loading" :disabled="loading" @click="findRestaurant()" large color="red darken-1 white--text" class="retry-button">
      Try Again
    </v-btn>
  </div>
</template>

<script>
import AppApi from '~apijs'

export default {
  async asyncData({ params }) {
    const { slug } = params
    const { data } = await AppApi.fetchRestaurant(slug)

    return { restaurant: data }
  },

  data: () => ({
    loading: false,
  }),

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
