<template>
    <user-layout>
        <section v-if="!blog" style="text-align: center">
            <v-progress-circular
                color="primary"
                indeterminate
                :size="128"
                :width="12"
            ></v-progress-circular>
        </section>
        <v-container style="max-width: 1000px" v-else>
            <v-container class="d-flex flex-wrap" style="gap: 10px">
                <v-btn color="primary" @click="goToEdit" class="mt-4" variant="outlined"
                    >Edit this blog</v-btn
                >

                <v-btn color="red" @click="handleDelete" class="mt-4" variant="outlined"
                    >delete this blog</v-btn
                >
            </v-container>

            <h1>{{ blog.title }}</h1>
            <h3>{{ blog.description }}</h3>

            <h4>{{ blog.author.name }}</h4>

            <v-container class="d-flex py-1 px-0" style="gap: 5px">
                <a
                    v-for="(item, i) in blog.author.links"
                    :key="i"
                    :href="item.url"
                    target="_blank"
                    rel="noopener noreferrer"
                    style="text-decoration: none"
                >
                    <v-chip label color="red" link size="large">{{ item.text }}</v-chip>
                </a>
            </v-container>

            <v-container class="d-flex py-1 px-0" style="gap: 5px">
                <v-chip v-for="(item, i) in blog.tags" :key="i" label color="primary">{{
                    item
                }}</v-chip>
            </v-container>

            <h4>{{ blog.category }}</h4>

            <div class="my-5"></div>

            <div class="blog-content" v-html="blog.content"></div>

            <v-container class="d-flex flex-wrap" style="gap: 10px">
                <v-btn color="primary" @click="goToEdit" class="mt-4" variant="outlined"
                    >Edit this blog</v-btn
                >

                <v-btn color="red" @click="handleDelete" class="mt-4" variant="outlined"
                    >delete this blog</v-btn
                >
            </v-container>
        </v-container>
    </user-layout>
</template>

<script lang="ts">
export default {
    data: () => ({
        blog: null,
    }),

    async mounted() {
        const req = await new this.Api().get(`/blog/${this.$route.params.blogID}`);
        this.blog = { ...req.data };
    },

    methods: {
        goToEdit() {
            this.$router.push(`/user/blog/update/${this.$route.params.blogID}`);
        },

        async handleDelete() {
            try {
                let conf = confirm("Are you sure you want to delete this blog?");
                if (!conf) throw new Error("Blog hasn't been deleted");
                await new this.Api().delete("/blog/" + this.$route.params.blogID);
                this.$router.push("/user/home");
                this.toast.success("Blog has been deleted successfully.");
            } catch (e: any) {
                this.toast.error(e.message);
            }
        },
    },
};
</script>
