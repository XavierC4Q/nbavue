<template>
  <v-alert type="error" prominent dark>
    <span class="title">{{ message }}</span>
  </v-alert>
</template>

<script>
export default {
  name: "ErrorMessage",
  props: ["message"]
};
</script>