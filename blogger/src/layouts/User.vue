<template>
    <div>
        <v-app-bar :elevation="2">

            <v-app-bar-title>
                <span>Blogger</span>
                <br>
                <span
                    class="text-caption"
                    v-if="user"
                >Hello {{user.first_name}} {{user.last_name}}</span>
            </v-app-bar-title>

            <template #append>
                <v-menu open-on-click>
                    <template #activator="{props}">
                        <v-btn
                            icon="mdi-dots-vertical"
                            v-bind="props"
                        ></v-btn>
                    </template>

                    <v-list>
                        <v-list-item
                            v-for="(item, index) in items"
                            :key="index"
                        >
                            <v-list-item-title>
                                <router-link :to="item.to">{{ item.title }}</router-link>
                            </v-list-item-title>
                        </v-list-item>
                    </v-list>
                </v-menu>
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
        items: [
            { title: "Home", to: "/user/home" },
            { title: "Create new Blog", to: "/user/blog/create" },
            { title: "Logout", to: "/logout" },
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