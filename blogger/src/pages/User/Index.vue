<template>
    <user-layout>

        <v-list lines="one">
            <v-list-item
                v-for="(item, i) in blogs"
                :key="i"
            >
                <div v-html="item.content"></div>
            </v-list-item>
        </v-list>
    </user-layout>
</template>

<script lang="ts">
export default {
    data: () => ({
        blogs: [],
    }),

    async mounted() {
        try {
            const req = await this.axios.get("/api/blogs", {
                headers: {
                    "x-access-token": this.$cookies.get("X-Access-Token"),
                },
            });

            console.log(req);

            this.blogs = req.data.data;
        } catch (error) {
            console.error(error);
        }
    },
};
</script>