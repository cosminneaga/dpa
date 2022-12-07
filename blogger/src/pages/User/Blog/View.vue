<template>
    <user-layout>
        <section
            v-if="!blog"
            style="text-align: center;"
        >
            <v-progress-circular
                color="primary"
                indeterminate
                :size="128"
                :width="12"
            ></v-progress-circular>
        </section>
        <v-container v-else>

            <v-btn
                color="red"
                size="large"
                @click="goToEdit"
                class="mb-4"
            >Edit this blog</v-btn>

            <h1>{{blog.title}}</h1>
            <h3>{{blog.description}}</h3>

            {{blog.author.name}}

            {{blog.author.links}}

            {{blog.tags}}

            {{blog.category}}

            <div class="my-5"></div>

            <div v-html="blog.content"></div>

            <v-btn
                color="red"
                size="large"
                @click="goToEdit"
                class="mt-4"
            >Edit this blog</v-btn>
        </v-container>
    </user-layout>
</template>



<script lang="ts">
export default {
    data: () => ({
        blog: null,
    }),

    async mounted() {
        const req = await this.axios.get(`/api/blog/${this.$route.params.blogID}`, {
            headers: {
                "x-access-token": this.$cookies.get("X-Access-Token"),
            },
        });

        this.blog = { ...req.data.data };
    },

    methods: {
        goToEdit() {
            this.$router.push(`/user/blog/update/${this.$route.params.blogID}`);
        },
    },
};
</script>

<style>
@import "https://cdn.quilljs.com/1.3.6/quill.snow.css";
@import "https://cdn.quilljs.com/1.3.6/quill.bubble.css";
</style>