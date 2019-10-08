<template>
  <div>
    <div v-if="teams && teams.length">
      <h1 class="display-1 text-center">NBA Teams</h1>
      <v-autocomplete
        label="Select a Team"
        :items="teams.map((t) => t.full_name)"
        @change="selectTeam"
      ></v-autocomplete>
      <v-card v-if="currentTeam">
        <v-card-title class="text-center">{{ currentTeam.full_name }}</v-card-title>
        <p class="body-1 px-4">City: {{ currentTeam.city }}</p>
        <p class="body-1 px-4">State: {{ currentTeam.state }}</p>
        <p class="body-1 px-4">Established: {{ currentTeam.year_founded }}</p>
      </v-card>
    </div>
    <ErrorMessage v-else message="Error fetching NBA teams! Check backend!" />
  </div>
</template>

<script>
import ErrorMessage from "@/components/ErrorMessage.vue";

export default {
  name: "Teams",
  components: {
    ErrorMessage
  },
  data() {
    return {
      teams: null,
      url: "http://127.0.0.1:5000/teams/all_teams",
      currentTeam: null
    };
  },
  async created() {
    try {
      const res = await fetch(this.url);
      const data = await res.json();

      this.teams = data;
    } catch (e) {
      console.log("TEAMS ERROR", e);
    }
  },
  computed: {

  },
  methods: {
    selectTeam(teamName) {
      this.currentTeam = this.teams.find(t => t.full_name === teamName);
    }
  }
};
</script>


<style scoped lang="scss">
.team-item {
  max-width: fit-content !important;
}
</style>