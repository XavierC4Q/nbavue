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
        <h1 class="display-1 px-4 py-4 mb-2 text-center">{{ currentTeam.full_name }}</h1>
        <p class="body-1 px-4">City: {{ currentTeam.city }}</p>
        <p class="body-1 px-4">State: {{ currentTeam.state }}</p>
        <p class="body-1 px-4">Established: {{ currentTeam.year_founded }}</p>
        <p class="headline px-4 text-center">Roster</p>
        <v-container fluid v-if="roster.length" class="d-flex flex-wrap justify-space-around">
          <v-card v-for="r in roster" :key="r.PLAYER_ID" width="30%" class="my-2 mx-2" flat>
            <v-card-title class="text-center">{{ r.PLAYER }}</v-card-title>
            <p class="body-1 px-4">Postion: {{ r.POSITION }}</p>
            <p class="body-1 px-4">Number {{ r.NUM }}</p>
          </v-card>
        </v-container>
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
      currentTeam: null,
      roster: []
    };
  },
  async created() {
    try {
      const res = await fetch(this.teamsUrl);
      const data = await res.json();

      this.teams = data;
    } catch (e) {
      throw Error("Failed to fetch team");
    }
  },
  computed: {
    teamsUrl: () => "http://127.0.0.1:5000/teams/all_teams"
  },
  methods: {
    async selectTeam(teamName) {
      this.currentTeam = this.teams.find(t => t.full_name === teamName);

      const rosterUrl = `http://127.0.0.1:5000/players/roster/${this.currentTeam.id}`;

      const res = await fetch(rosterUrl);
      const data = await res.json();

      this.roster = data;
    }
  }
};
</script>


<style scoped lang="scss">
.team-item {
  max-width: fit-content !important;
}
</style>