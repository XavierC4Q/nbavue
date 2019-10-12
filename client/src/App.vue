<template>
  <v-app>
    <Header />

    <v-content>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-content>

    <Footer />
  </v-app>
</template>

<script>
import Footer from "./components/Footer";
import Header from "./components/Header";

export default {
  name: "App",
  components: {
    Footer,
    Header
  },
  data: () => ({
    //
  }),
  methods: {
    navHome() {
      window.history.length > 1 ? this.$router.go(-1) : this.$router.push("/");
    }
  }
};
</script>

<style scoped lang="scss">
.pointer {
  &:hover {
    cursor: pointer;
  }
}
</style>
