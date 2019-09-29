<template>
  <div>
    <h3>Teams</h3>
    <section v-if="teams && teams.length">
        <div v-for="t in teams" :key="t.id">
            <h2>{{t.full_name}}</h2>
        </div>
    </section>
    <section v-else>
        <h2>No teams here</h2>
    </section>
  </div>
</template>

<script>
export default {
  name: "Teams",
  data() {
    return { teams: null, url: "http://127.0.0.1:5000/teams/all_teams" };
  },
  async created() {
    try {
      const res = await fetch(this.url);
      const data = await res.json();

      this.teams = data;
    } catch (e) {
      console.log("TEAMS ERROR", e);
    }
  }
};
</script>