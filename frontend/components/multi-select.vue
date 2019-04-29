<template>
  <v-autocomplete
    v-model="selected"
    :disabled="isUpdating"
    :items="options"
    :label="label"
    :allow-overflow="false"
    hide-selected
    hide-no-data
    clearable
    chips
    color="blue-grey lighten-2"
    multiple
    no-data-text="Carregando">
  </v-autocomplete>
</template>

<script>
export default {
  props: {
    options: {
      type: Array,
      required: true
    },
    label: {
      type: String,
      required: true,
    },
  },

  data: () => ({
    selected: [],
    autoUpdate: true,
    isUpdating: false,
  }),

  watch: {
    isUpdating (val) {
      if (val) {
        setTimeout(() => (this.isUpdating = false), 3000)
      }
    }
  },
}
</script>
