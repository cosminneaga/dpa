<template>
    <div>
        <v-app-bar
            :elevation="0"
            rounded
        >

            <v-app-bar-title>
                <span>Blogger</span>
                <br>
                <span
                    class="text-caption"
                    v-if="user"
                >Hello {{user.first_name}} {{user.last_name}}</span>
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
                        variant="outlined"
                        color="primary"
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
            { text: "Logout", to: "/logout" },
        ],
        user: null,
    }),

    async mounted() {
        const req = await this.axios.get("/api/user/me", {
            headers: {
                "x-access-token": this.$cookies.get("X-Access-Token"),
            },
        });
        this.user = req.data.data;
    },
};
</script>