<template>
  <v-app-bar app class="blue darken-3">
    <v-toolbar-title class="headline text-uppercase white--text pointer">
      <span class="blue darken-3 display-2" @click="navHome">NBAVue</span>
    </v-toolbar-title>

    <div class="flex-grow-1"></div>

    <v-list class="blue darken-3 white--text d-flex justify-space-evenly" height="100%">
      <v-list-item href to="/teams" height="100%">
        <v-list-item-content>
          <v-list-item-title class="title white--text">Teams</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item href to="/players" height="100%">
        <v-list-item-content>
          <v-list-item-title class="title white--text">Players</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-app-bar>
</template>

<script>
export default {
  name: "Header"
};
</script>