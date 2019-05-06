<template>
  <div class="container--centralized full-width">
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
        <div class="item text-vertical-centralized restaurant-rating">
          <v-icon color="rgba(230, 166, 76, 1)">star</v-icon>
          {{ restaurant.rating }}
        </div>
      </div>
    </v-card>
  </div>
</template>

<style>
.image {
  padding: 16px;
  border-radius: 50%;
}

.image-container {
  height: 200px;
  width: 200px;
}

.full-width {
  width: 100vw;
}

.container--column {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.container--centralized {
  display: flex;
  justify-content: center;
  align-items: center;
}

.text-vertical-centralized {
  display: flex;
  align-items: center;
}

.item {
  width: 250px;
  min-height: 45px;
  /* border: 1px solid black; */
}

.restaurant-name {
  font-weight: 700;
  font-size: 1.5rem;
  flex-grow: 2
}

.restaurant-cuisine {
  font-size: 1.3125rem;
  font-weight: 300;
  flex-grow: 1;
}

.restaurant-delivery {
  font-size: 1.125rem;
  font-weight: 500;
  padding: 2px 4px;
  border: 1px solid #d8d8d8;
}

.restaurant-delivery--free {
  color: #55a977;
}

.restaurant-rating {
  color: #e6a64c;
  flex-grow: 1;
}
</style>

<script>
import AppApi from '~apijs'

export default {
  async asyncData({ params }) {
    const { slug } = params
    const { data } = await AppApi.fetchRestaurant(slug)

    return { restaurant: data }
  },
}
</script>
