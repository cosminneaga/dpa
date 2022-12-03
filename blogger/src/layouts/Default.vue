<script lang="ts" setup>
import Header from "@/components/Navigation/Header.vue";
import Footer from "@/components/Navigation/Footer.vue";
</script>

<template>
    <v-container class="elevation-1 pa-0" style="max-width: 1400px; min-width: 600px;">
        <Header></Header>
        
        <div class="my-10"></div>

        <v-container>
            <slot></slot>
        </v-container>

        <div class="my-10"></div>

        <Footer></Footer>
    </v-container>
</template>