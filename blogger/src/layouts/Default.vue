<script lang="ts" setup>
import Header from "@/components/Navigation/Header.vue";
import Footer from "@/components/Navigation/Footer.vue";
</script>

<template>
    <v-container style="max-width: 1400px; min-width: 600px;">
        <Header></Header>
        
        <div class="my-10"></div>

        <v-container>
            <slot></slot>
        </v-container>

        <div class="my-10"></div>

        <Footer></Footer>
    </v-container>
</template>

<script lang="ts">
export default {
    async mounted() {
        const res = await this.axios.get('/api/hello');

        console.log(res);     
                
    }
}
</script>

<style lang="scss" scoped>
.v-container {
    margin-top: 50px;
    margin-bottom: 50px;
}
</style>