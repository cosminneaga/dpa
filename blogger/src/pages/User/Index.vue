<template>
    <user-layout>

        <v-container
            fluid
            class="d-flex flex-row flex-wrap justify-center"
            style="gap:20px;"
        >
            <router-link
                v-for="(item, i) in blogs"
                :key="i"
                :to="`/user/blog/view/${item._id}`"
                style="text-decoration: none;"
            >
                <v-card
                    width="400"
                    :title="item.title"
                    :subtitle="item.description"
                    ripple
                    variant="outlined"
                    link
                    color="blue"
                >
                    <template v-slot:text>
                        <div
                            class="card-content"
                            v-html="item.content"
                        ></div>
                    </template>
                </v-card>
            </router-link>
        </v-container>
    </user-layout>
</template>

<script lang="ts">
export default {
    data: () => ({
        blogs: [],
    }),

    async mounted() {
        const req = await this.axios.get("/blogs", {
            headers: {
                "x-access-token": this.$cookies.get("X-Access-Token"),
            },
        });

        this.blogs = req.data.data;
    },
};
</script>

<style lang="scss" scoped>
.card-content {
    display: inline-block;
    width: 100%;
    height: 100px;
    white-space: nowrap;
    overflow: hidden !important;
    text-overflow: ellipsis;
}
</style>