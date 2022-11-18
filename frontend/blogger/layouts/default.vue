<template>

    <v-app :theme="theme">

        <v-container style="max-width: 1200px;">
            <div class="mt-2 pa-5 rounded-shaped elevation-3">
                <v-row class="align-center">

                    <v-img
                        src="img/logo_main.png"
                        max-height="100"
                    ></v-img>

                    <v-spacer></v-spacer>

                    <v-btn variant="plain">
                        <nuxt-link to="/">Home</nuxt-link>
                    </v-btn>

                    <v-btn variant="plain">
                        <nuxt-link to="/login">Login</nuxt-link>
                    </v-btn>

                    <v-btn variant="plain">
                        <nuxt-link to="/register">Register</nuxt-link>
                    </v-btn>

                    <v-btn variant="plain">
                        <nuxt-link to="/user/home">UserHome</nuxt-link>
                    </v-btn>

                </v-row>
            </div>

            <v-container>
                <slot />
            </v-container>

            <div class="mt-5 pa-10 rounded-shaped elevation-3">
                <p>Created in 2022</p>
            </div>
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
    data() {
        return {
            drawer: false,
        };
    },
};
</script>