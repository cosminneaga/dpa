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
            this.$cookies.set("X-Access-Token", "");
            this.$router.push("/");
        }, 3000);
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