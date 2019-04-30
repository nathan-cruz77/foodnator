<template>
  <v-autocomplete
    v-model="valueCopy"
    :items="options"
    :label="label"
    :allow-overflow="false"
    hide-selected
    hide-no-data
    clearable
    chips
    multiple
    color="blue-grey lighten-2"
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
    value: {
      type: Array,
      required: true,
    }
  },

  // This copy is here to prevent Vue from complaining about v-autocomplete
  // mutating a prop value.
  data: () => ({
    valueCopy: [],
  }),

  mounted() {
    this.valueCopy = [...this.value]
  },

  watch: {
    valueCopy() {
      this.$emit('input', this.valueCopy)
    },
  },
}
</script>
