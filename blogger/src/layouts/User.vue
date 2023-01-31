<template>
    <div>
        <v-app-bar
            :elevation="1"
            rounded
            absolute
            density="compact"
            style="width: 1000px; left: 50%; transform: translate(-50%, 0);"
        >

            <v-app-bar-title>
                <span>Blogger</span>
            </v-app-bar-title>

            <template #append>
                <router-link
                    v-for="(item, i) in links"
                    :key="i"
                    :to="item.to"
                    style="text-decoration: none;"
                    class="ml-2"
                >
                    <v-btn
                        variant="text"
                        :color="item.color ? item.color : 'primary'"
                    >{{item.text}}</v-btn>
                </router-link>
            </template>
        </v-app-bar>

        <v-container
            style="margin-top: 80px;"
            fluid
        >
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