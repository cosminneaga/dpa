<template>
    <v-container style="max-width: 1400px; min-width: 540px">
        <Header :serverString="serverString"></Header>

        <div class="my-10"></div>

        <v-container>
            <slot></slot>
        </v-container>

        <div class="my-10"></div>

        <Footer></Footer>
    </v-container>
</template>

<script lang="ts">
import Header from "../components/Navigation/Header.vue";
import Footer from "../components/Navigation/Footer.vue";

export default {
    components: { Header, Footer },

    data: () => ({
        serverString: "",
    }),

    async mounted() {
        try {
            const res = await new this.Api().get("/hello");
            console.log(res);
            this.serverString = res.data.message;
        } catch (e: any) {
            console.warn(e.message);
        }
    },
};
</script>

<style lang="scss" scoped>
.v-container {
    margin-top: 50px;
    margin-bottom: 50px;
}
</style>
