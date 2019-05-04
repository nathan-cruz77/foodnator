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
    color="blue-grey lighten-2">

    <template slot="selection" slot-scope="{ selected, item, index }">
      <v-chip @input="remove(index)" :selected="selected" close class="chip--select-multi">
        {{ getText(item) }}
      </v-chip>
    </template>
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
    },
    itemText: {
      type: String,
      required: false,
      default: '',
    },
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

  methods: {
    getText(item) {
      if (this.itemText) {
        return item[this.itemText]
      }

      return item
    },

    remove(index) {
      if (index >= 0) this.valueCopy.splice(index, 1)
    },
  },
}
</script>
