<template>
    <div style="min-width: 740px">
        <v-app-bar :elevation="4" rounded absolute density="comfortable" style="min-width: 740px; margin: auto">
            <v-app-bar-title>
                <span class="text-primary text-uppercase">Blogger</span>
            </v-app-bar-title>

            <template #append>
                <router-link
                    v-for="(item, i) in links"
                    :key="i"
                    :to="item.to"
                    style="text-decoration: none"
                    class="ml-2"
                >
                    <v-btn variant="text" :color="item.color ? item.color : 'primary'">{{ item.text }}</v-btn>
                </router-link>
            </template>
        </v-app-bar>

        <v-container style="margin-top: 80px" fluid>
            <slot></slot>
        </v-container>

        <!-- USER LAYOUT BOTTOM -->
    </div>
</template>

<script lang="ts">
export default {
    data: () => ({
        links: [
            { text: "Home", to: "/user/home" },
            { text: "Create new Blog", to: "/user/blog/create" },
            { text: "Settings", to: "/user/settings" },
            { text: "Logout", to: "/logout", color: "error" },
        ],
    }),
};
</script>
