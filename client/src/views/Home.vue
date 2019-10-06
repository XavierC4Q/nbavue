<template>
  <v-container fluid>
    <h1 class="title">Welcome to NBAVue</h1>
    <div class="p-2 m-2 text-justify text-wrap body-1">
      <p>
        This a just a small project meant to copy the NBA stats page using Flask and VueJS.
        If you know me, you know I love basketball and I love code, especially chances to try new things.
        Shoutout to nba_py for being so easy and free.
      </p>
      <p>
          For now, I will have an page for all static team info, all static player info and
          a stats page with all the advanced stats and stuff. I have to see how often the api
          updates before I can think about a live tracker.
      </p>
    </div>
  </v-container>
</template>

<script>
export default {
  name: "Home"
};
</script>