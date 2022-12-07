<template>
    <section>

        <v-row style="min-width: 1000px;">
            <v-col
                cols="3"
                class="pa-0"
                style="min-width: 400px;"
            >
                <section class="meta-blog-info bg-blue h-100 pa-3">
                    <v-form>

                        <!-- TITLE & DESCRIPTION -->
                        <v-text-field
                            label="Title"
                            density="comfortable"
                            variant="outlined"
                            v-model="meta.title"
                        ></v-text-field>
                        <v-textarea
                            label="Description"
                            density="comfortable"
                            variant="outlined"
                            v-model="meta.description"
                        ></v-textarea>

                        <!-- IMAGE -->
                        <p>Image</p>
                        <section style="display: flex; gap:10px;">
                            <v-text-field
                                variant="outlined"
                                density="compact"
                                label="alt"
                                v-model="meta.image.alt"
                            ></v-text-field>
                            <v-text-field
                                variant="outlined"
                                density="compact"
                                label="title"
                                v-model="meta.image.title"
                            ></v-text-field>
                        </section>
                        <v-text-field
                            variant="outlined"
                            density="compact"
                            label="src"
                            v-model="meta.image.src"
                        ></v-text-field>

                        <!-- AUTHOR -->
                        <p>Author</p>
                        <v-text-field
                            variant="outlined"
                            density="comfortable"
                            label="Full Name"
                            v-model="meta.author.name"
                        ></v-text-field>

                        <!-- AUTHOR LINKS -->
                        <section class="my-3">
                            <p>Author Links</p>
                            <section class="my-3">
                                <v-row
                                    class="pa-5"
                                    style="gap:10px;"
                                >
                                    <v-chip
                                        v-for="(item, i) in meta.author.links"
                                        :key="i"
                                        variant="tonal"
                                        :prepend-avatar="item.imageSrc"
                                        label
                                        size="x-large"
                                    >
                                        <a
                                            :href="item.url"
                                            target="_blank"
                                            style="text-decoration: none; color: white;"
                                        >
                                            {{ item.text }}
                                        </a>

                                        <v-icon
                                            color="purple"
                                            @click="removeAuthorLink(i)"
                                            class="ml-2"
                                        >mdi-close-octagon</v-icon>
                                    </v-chip>
                                </v-row>

                            </section>

                            <v-text-field
                                label="Text"
                                density="compact"
                                variant="outlined"
                                v-model="authorLink.text"
                            ></v-text-field>
                            <v-text-field
                                label="Url"
                                density="compact"
                                variant="outlined"
                                v-model="authorLink.url"
                            ></v-text-field>
                            <v-text-field
                                label="Image src"
                                density="compact"
                                variant="outlined"
                                v-model="authorLink.imageSrc"
                            ></v-text-field>
                            <v-btn @click="addAuthorLink">Add Link</v-btn>
                        </section>
                        <!-- AUTHOR LINKS -->

                        <!-- CATEGORY -->
                        <v-text-field
                            label="Category"
                            density="comfortable"
                            variant="outlined"
                            v-model="meta.category"
                        ></v-text-field>

                        <!-- TAGS -->
                        <section class="my-3">
                            <v-row
                                class="pa-5"
                                style="gap:10px;"
                            >
                                <v-chip
                                    v-for="(item, i) in meta.tags"
                                    :key="i"
                                    variant="flat"
                                    exact
                                    label
                                >
                                    {{item}}
                                    <v-icon
                                        color="purple"
                                        @click="removeTag(i)"
                                        class="ml-2"
                                    >mdi-close-octagon</v-icon>
                                </v-chip>
                            </v-row>

                            <v-text-field
                                label="Tag"
                                density="comfortable"
                                variant="outlined"
                                v-model="tag"
                            ></v-text-field>

                            <v-btn @click="addTag">Add Tag</v-btn>
                        </section>
                    </v-form>
                </section>
            </v-col>

            <v-col>
                <v-container fluid>
                    <quill-editor ref="editor"></quill-editor>

                    <v-btn
                        @click="handleSubmit"
                        color="success"
                        class="mt-4"
                        size="x-large"
                    >Submit Blog</v-btn>
                </v-container>
            </v-col>
        </v-row>
    </section>
</template>

<script lang="ts">
interface BlogMeta {
    title: string;
    description: string;
    image: {
        src: string;
        alt: string;
        title: string;
    };
    author: {
        name: string;
        links: [
            {
                text: string;
                url: string;
                image: string;
            }
        ];
    };
    category: string;
    tags: string[];
    content: object[];
}

interface AuthorLink {
    text: string;
    url: string;
    image: string;
}

interface ComponentData {
    meta: BlogMeta;
}

export default {
    props: ["update"],

    mounted() {
        if (this.$props.update) {
            this.meta = { ...this.$props.update };
            delete this.meta._id;

            this.$refs.editor.setHTML(this.$props.update.content);
        }
    },

    data: () => ({
        meta: {
            title: "",
            description: "",
            image: {
                src: "",
                alt: "",
                title: "",
            },
            author: {
                name: "",
                links: [],
            },
            category: "",
            tags: [],
            content: null,
        },
        authorLink: {
            text: "",
            url: "",
            imageSrc: "",
        },
        tag: "",
    }),

    watch: {
        meta: {
            handler(value) {
                localStorage.setItem("blog-create", JSON.stringify(value));
            },
            deep: true,
        },
    },

    beforeCreate() {
        const savedContent = localStorage.getItem("blog-create");

        if (savedContent) {
        }
    },

    methods: {
        async handleSubmit() {
            this.meta.content = this.$refs.editor.getHTML();

            try {
                let req = null;
                if (this.$props.update) {
                    req = await this.axios.put(`/api/blog/${this.$route.params.blogID}`, this.meta, {
                        headers: {
                            "x-access-token": this.$cookies.get("X-Access-Token"),
                        },
                    });
                } else {
                    req = await this.axios.post("/api/blog", this.meta, {
                        headers: {
                            "x-access-token": this.$cookies.get("X-Access-Token"),
                        },
                    });

                    this.meta = {
                        title: "",
                        description: "",
                        image: {
                            src: "",
                            alt: "",
                            title: "",
                        },
                        author: {
                            name: "",
                            links: [],
                        },
                        category: "",
                        tags: [],
                        content: null,
                    };
                    this.$refs.editor.setHTML("Content");
                }

                console.log(req);

                this.$toast.success(`Blog ${this.$props.update ? "updated" : "created"} successfully.`);
            } catch (error) {
                console.error(error);
            }
        },

        addAuthorLink() {
            this.meta.author.links.push(this.authorLink);
            this.authorLink = {
                text: "",
                url: "",
                imageSrc: "",
            };
        },

        removeAuthorLink(index: number) {
            this.meta.author.links.splice(index, 1);
        },

        addTag() {
            this.meta.tags.push(this.tag);
            this.tag = "";
        },

        removeTag(index: number) {
            this.meta.tags.splice(index, 1);
            this.tag = "";
        },
    },
};
</script>