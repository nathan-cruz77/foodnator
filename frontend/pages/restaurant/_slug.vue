<template>
  <div class="container--centralized flex-column full-width">
    <v-card class="container--centralized" v-if="restaurant !== 'not-found'">
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

    <v-card v-else class="container--centralized">
      No restaurant found, try other preferences.
    </v-card>

    <div class="restaurant-actions">
      <v-btn v-if="restaurant !== 'not-found'" @click="openOnIfood()" color="rgba(85, 169, 119, 1) white--text">
        Check on Ifood
      </v-btn>

      <find-restaurant label="Try Again" v-if="loggedUser"/>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import AppApi from '~apijs'
import FindRestaurant from '~/components/find-restaurant'

export default {
  async asyncData({ params }) {
    const { slug } = params

    try {
      const { data } = await AppApi.fetchRestaurant(slug)
      return { restaurant: data }
    } catch(error) {
      if (error.response.status === 404) return { restaurant: 'not-found' }
      throw error
    }
  },

  components: {
    FindRestaurant,
  },

  computed: {
    ...mapState('user', ['loggedUser']),
  },

  methods: {
    openOnIfood() {
      if (this.restaurant.ifood_url) {
        window.open(this.restaurant.ifood_url)
      }
    },
  },
}
</script>
