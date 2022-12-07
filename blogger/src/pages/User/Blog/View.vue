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
        <v-container
            style="max-width: 1000px;"
            v-else
        >

            <v-btn
                color="red"
                size="large"
                @click="goToEdit"
                class="mb-4"
            >Edit this blog</v-btn>

            <h1>{{blog.title}}</h1>
            <h3>{{blog.description}}</h3>

            <h4>{{blog.author.name}}</h4>

            <v-container
                class="d-flex py-1 px-0"
                style="gap: 5px;"
            >
                <a
                    v-for="(item, i) in blog.author.links"
                    :key="i"
                    :href="item.url"
                    target="_blank"
                    rel="noopener noreferrer"
                    style="text-decoration: none;"
                >
                    <v-chip
                        label
                        color="red"
                        link
                        size="large"
                    >{{item.text}}</v-chip>
                </a>

            </v-container>

            <v-container
                class="d-flex py-1 px-0"
                style="gap: 5px;"
            >
                <v-chip
                    v-for="(item, i) in blog.tags"
                    :key="i"
                    label
                    color="primary"
                >{{item}}</v-chip>
            </v-container>

            <h4>{{blog.category}}</h4>

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