<template>

    <v-app :theme="theme">
        <v-app-bar
            :elevation="2"
            style="min-width: 100%;"
        >

            <template #prepend>
                <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            </template>

            <v-app-bar-title>Blogger</v-app-bar-title>

            <template #append>
                <v-btn icon="mdi-dots-vertical"></v-btn>
            </template>

        </v-app-bar>

        <v-navigation-drawer
            v-model="drawer"
            temporary
            class="pa-3"
        >
            <v-list-item :title="user.first_name + ' ' + user.last_name"></v-list-item>

            <v-divider></v-divider>

            <v-list
                density="compact"
                nav
            >
                <nuxt-link to="/user/home">
                    <v-list-item
                        prepend-icon="mdi-view-dashboard"
                        title="Home"
                        value="home"
                    >

                    </v-list-item>
                </nuxt-link>
                <v-list-item
                    prepend-icon="mdi-forum"
                    title="About"
                    value="about"
                ></v-list-item>
            </v-list>
        </v-navigation-drawer>

        <v-container class="mt-15">
            <slot></slot>
        </v-container>
    </v-app>

</template>

<script setup>
import { ref } from "vue";

const theme = ref("light");

function onClick() {
    theme.value = theme.value === "light" ? "dark" : "light";
}
</script>

<script>
export default {
    data: () => ({
        drawer: false,
        user: "default",
    }),

    async mounted() {
        const res = await $fetch(this.$config.public.apiBase + "user/me", {
            headers: {
                "X-Access-Token": JSON.parse(localStorage.getItem("blogger"))
                    .token,
            },
        });

        console.log(res);
        this.user = res.data;
    },
};
</script>