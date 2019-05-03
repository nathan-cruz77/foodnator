<template>
  <v-navigation-drawer v-if="showGroups" fixed app>
    <v-list dense>
      <v-list-tile @click="toggleGroups()">
        <v-list-tile-action>
          <!-- This is here because material icons do not include a left version of arrow_right_alt -->
          <v-icon style="transform: rotate(180deg)">arrow_right_alt</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>Groups</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile/>

      <v-item-group>
        <v-container grid-list-md>
          <v-layout wrap column>
            <v-flex v-for="group in groups" :key="group.name" xs12 md4>
              <v-item>
                <v-card slot-scope="{ active, toggle }"
                  @click="selectAndToggle(group, toggle)"
                  :color="active ? 'red' : ''"
                  hover
                  class="d-flex align-center"
                  height="60"
                  width="100%">
                  <div class="display-6 text-xs-center">
                    {{ group.name }}
                  </div>
                </v-card>
              </v-item>
            </v-flex>
          </v-layout>
        </v-container>
      </v-item-group>
      <v-list-tile/>

      <v-container grid-list-md>
        <v-layout wrap column>
          <v-btn color="red" @click="newGroup()" xs12 md4>
            <v-icon>group_add</v-icon>
            <v-spacer/>
            <div>New Group</div>
          </v-btn>
        </v-layout>
      </v-container>

    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  mounted() {
    this.fetchGroups()
  },
  computed: {
    ...mapGetters('toolbar', ['showGroups']),
    ...mapGetters('user', ['groups']),
  },
  methods: {
    ...mapActions('toolbar', ['toggleGroups', 'newGroup']),
    ...mapActions('user', ['fetchGroups', 'selectGroup']),
    selectAndToggle(group, toggle) {
      toggle()
      this.selectGroup(group)
    },
  },
}
</script>
