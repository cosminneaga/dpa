<template>
    <header class="elevation-6 rounded">

        <v-btn
          icon
          variant="text"
        >
          <v-icon>mdi-menu</v-icon>
        </v-btn>

        <h1 class="title">Blogger</h1>

        <v-spacer></v-spacer>

        <ul class="nav-links">
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="/about">About</router-link></li>
            <li><router-link to="/login">Login</router-link></li>
            <li><router-link to="/register">Register</router-link></li>
        </ul>

    </header>
</template>

<style lang="scss" scoped>
header {
    display: flex;
    align-items: center;
    gap:20px;
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