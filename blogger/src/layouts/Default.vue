<script lang="ts" setup>
import Header from "@/components/Navigation/Header.vue";
import Footer from "@/components/Navigation/Footer.vue";
</script>

<template>
    <v-container class="elevation-1">
        <Header></Header>
        
        <div class="my-10"></div>

        <slot></slot>

        <div class="my-10"></div>

        <Footer></Footer>
    </v-container>
</template>