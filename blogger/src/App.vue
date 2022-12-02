<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <!-- <component :is="layout">
    <router-view :layout.sync="layout" />
  </component> -->
  <v-app>
    <RouterView />
  </v-app>
</template>
