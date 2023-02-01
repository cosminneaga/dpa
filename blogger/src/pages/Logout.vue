<template>
    <default-layout>
        <section>
            <v-img
                src="/img/bye.jpg"
                height="500"
                class="bg-grey-lighten-2"
                aspect-ratio="4/3"
                width="500"
            ></v-img>

            <div class="my-10"></div>

            <v-progress-circular
                color="primary"
                indeterminate
                :size="128"
                :width="12"
            ></v-progress-circular>

            <h1>Logging you out</h1>
        </section>
    </default-layout>
</template>

<script lang="ts">
export default {
    mounted() {
        setTimeout(() => {
            // this.$cookies.set("X-Access-Token", "");
            // this.$cookies.remove("X-Access-Token");
            this.eraseCookieFromAllPaths("X-Access-Token");
            localStorage.clear();
            this.$router.push("/");
        }, 2100);
    },

    methods: {
        eraseCookieFromAllPaths(name: string) {
            // This function will attempt to remove a cookie from all paths.
            var pathBits = location.pathname.split("/");
            var pathCurrent = " path=";

            // do a simple pathless delete first.
            document.cookie = name + "=; expires=Thu, 01-Jan-1970 00:00:01 GMT;";

            for (var i = 0; i < pathBits.length; i++) {
                pathCurrent += (pathCurrent.substr(-1) != "/" ? "/" : "") + pathBits[i];
                document.cookie = name + "=; expires=Thu, 01-Jan-1970 00:00:01 GMT;" + pathCurrent + ";";
            }
        },
    },
};
</script>

<style lang="scss" scoped>
section {
    display: flex;
    flex-flow: column nowrap;
    justify-content: center;
    align-items: center;
}
</style>