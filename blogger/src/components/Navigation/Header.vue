<template>
    <v-toolbar elevation="12" style="position: relative !important; max-width: 1200px" class="mx-auto" theme="dark">
        <!-- <v-btn icon variant="text" @click="drawer = true">
            <v-icon>mdi-menu</v-icon>
        </v-btn> -->

        <v-app-bar-title>
            <v-tooltip :text="serverString" location="bottom">
                <template v-slot:activator="{ props }">
                    <span class="title" v-bind="props">Bloggerr</span>
                </template>
            </v-tooltip>
        </v-app-bar-title>

        <v-spacer></v-spacer>

        <ul class="nav-links">
            <li>
                <v-btn variant="text" color="primary" to="/">Home</v-btn>
            </li>
            <li>
                <v-btn variant="text" color="primary" to="/about">About</v-btn>
            </li>
            <li>
                <v-btn variant="text" color="primary" to="/login">Login</v-btn>
            </li>
            <!-- <li>
                <v-btn
                    variant="text"
                    color="primary"
                    to="/register"
                >Register</v-btn>
            </li> -->
        </ul>

        <v-navigation-drawer v-model="drawer" temporary>
            <v-list-item
                prepend-avatar="https://randomuser.me/api/portraits/men/78.jpg"
                title="John Leider"
            ></v-list-item>

            <v-divider></v-divider>

            <v-list density="compact" nav>
                <router-link to="/">
                    <v-list-item prepend-icon="mdi-view-dashboard" title="Home" value="home"></v-list-item>
                </router-link>
                <router-link to="/about">
                    <v-list-item prepend-icon="mdi-forum" title="About" value="about"></v-list-item>
                </router-link>
            </v-list>
        </v-navigation-drawer>
    </v-toolbar>
</template>

<script lang="ts">
export default {
    props: ["serverString"],

    data: () => ({
        drawer: false,
    }),
};
</script>

<style lang="scss" scoped>
header {
    display: flex;
    align-items: center;
    gap: 20px;
    padding: 12px 21px;

    ul.nav-links {
        list-style-type: none;
        padding: 0;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 5px;

        li {
            a {
                padding: 7px 8px;
            }
        }
    }
}
</style>
