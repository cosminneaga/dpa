<template>
    <header class="elevation-6 rounded">

        <!-- <v-btn icon variant="text" @click="drawer = true">
            <v-icon>mdi-menu</v-icon>
        </v-btn> -->

        <h1 class="title">Blogger</h1>

        <v-spacer></v-spacer>

        <ul class="nav-links">
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="/about">About</router-link></li>
            <li><router-link to="/login">Login</router-link></li>
            <li><router-link to="/register">Register</router-link></li>
        </ul>


        <v-navigation-drawer v-model="drawer" temporary>
            <v-list-item prepend-avatar="https://randomuser.me/api/portraits/men/78.jpg"
                title="John Leider"></v-list-item>

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

    </header>
</template>

<script lang="ts">
export default {
    data: () => ({
        drawer: false
    }),
}
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