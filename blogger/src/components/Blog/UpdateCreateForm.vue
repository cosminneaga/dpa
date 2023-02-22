<template>
    <section>
        <!-- META-INFO DRAWER -->
        <v-navigation-drawer
            v-model="drawer"
            location="left"
            temporary
            absolute
            width="700"
            class="pt-10"
            disable-resize-watcher
            disable-route-watcher
            scrim
        >
            <v-btn
                icon="mdi-close"
                color="primary"
                variant="outlined"
                :size="40"
                style="position: absolute; top: 10px; right: 10px"
                @click="drawer = false"
            ></v-btn>

            <h1 class="text-primary text-center text-h4">Blog Meta Information</h1>
            <v-form class="ma-4">
                <!-- TITLE & DESCRIPTION -->
                <v-text-field
                    label="Title"
                    density="comfortable"
                    variant="outlined"
                    v-model="blog.title"
                    color="primary"
                ></v-text-field>
                <v-textarea
                    label="Description (blog's subtitle)"
                    density="comfortable"
                    variant="outlined"
                    v-model="blog.description"
                    color="primary"
                ></v-textarea>

                <v-divider color="primary"></v-divider>

                <!-- IMAGE -->
                <section class="my-3 px-3">
                    <h2 class="text-primary">Blog Main Image</h2>
                    <section class="mt-3">
                        <v-row style="gap: 5px">
                            <v-text-field
                                variant="outlined"
                                density="compact"
                                label="Alt"
                                v-model="blog.image.alt"
                                color="primary"
                            ></v-text-field>
                            <v-text-field
                                variant="outlined"
                                density="compact"
                                label="Title"
                                v-model="blog.image.title"
                                color="primary"
                            ></v-text-field>
                            <v-text-field
                                variant="outlined"
                                density="compact"
                                label="Src"
                                v-model="blog.image.src"
                                color="primary"
                            ></v-text-field>
                        </v-row>
                    </section>
                </section>

                <v-divider color="primary"></v-divider>

                <!-- AUTHOR -->
                <section class="mt-3">
                    <h2 class="text-primary">Author</h2>
                    <v-text-field
                        variant="outlined"
                        density="comfortable"
                        label="Full Name"
                        v-model="blog.author.name"
                        color="primary"
                    ></v-text-field>
                </section>

                <v-divider color="primary"></v-divider>

                <!-- AUTHOR LINKS -->
                <section class="my-3">
                    <h2 class="text-primary">Author Links</h2>
                    <section class="my-3">
                        <v-row class="pa-5" style="gap: 10px">
                            <v-chip
                                v-for="(item, i) in blog.author.links"
                                :key="i"
                                variant="tonal"
                                :prepend-avatar="item.imageSrc"
                                label
                                size="x-large"
                            >
                                <a :href="item.url" target="_blank" style="text-decoration: none; color: white">
                                    {{ item.text }}
                                </a>

                                <v-icon color="primary" @click="removeAuthorLink(i)" class="ml-2"
                                    >mdi-close-octagon</v-icon
                                >
                            </v-chip>
                        </v-row>
                    </section>

                    <v-row style="gap: 5px" class="px-3">
                        <v-text-field
                            label="Text"
                            density="compact"
                            variant="outlined"
                            v-model="authorLink.text"
                            color="primary"
                        ></v-text-field>
                        <v-text-field
                            label="Url"
                            density="compact"
                            variant="outlined"
                            v-model="authorLink.url"
                            color="primary"
                        ></v-text-field>
                        <v-text-field
                            label="Image src"
                            density="compact"
                            variant="outlined"
                            v-model="authorLink.imageSrc"
                            color="primary"
                        ></v-text-field>
                    </v-row>

                    <v-btn @click="addAuthorLink" color="primary" variant="outlined">Add Link</v-btn>
                </section>
                <!-- AUTHOR LINKS -->

                <v-divider color="primary"></v-divider>

                <!-- CATEGORY -->
                <v-select
                    class="mt-5"
                    label="Category"
                    density="comfortable"
                    variant="outlined"
                    :items="globalData.categories"
                    color="primary"
                ></v-select>

                <v-divider color="primary"></v-divider>

                <!-- TAGS -->
                <section class="mt-3 mb-5">
                    <v-row class="pa-5" style="gap: 10px">
                        <v-chip v-for="(item, i) in blog.tags" :key="i" variant="flat" exact label>
                            {{ item }}
                            <v-icon color="purple" @click="removeTag(i)" class="ml-2">mdi-close-octagon</v-icon>
                        </v-chip>
                    </v-row>

                    <v-text-field
                        label="Tag"
                        density="comfortable"
                        variant="outlined"
                        v-model="tag"
                        color="primary"
                    ></v-text-field>

                    <v-btn @click="addTag" color="primary" variant="outlined">Add Tag</v-btn>
                </section>
                <!-- TAGS -->

                <v-divider color="primary"></v-divider>
            </v-form>
        </v-navigation-drawer>
        <!-- META-INFO DRAWER -->

        <!-- WYSIWYG EDITOR -->
        <v-container fluid>
            <v-btn @click="drawer = !drawer" color="secondary" variant="outlined" class="mb-4">Meta Info</v-btn>
            <v-btn @click="handleSubmit" color="primary" variant="outlined" class="mb-4 ml-2">Submit Blog</v-btn>

            <kothing-editor
                @on-change="(content) => onContentChange(content)"
                :contentSet="update ? update.content : null"
            />
        </v-container>
        <!-- WYSIWYG EDITOR -->
    </section>
</template>

<script lang="ts">
import KothingEditor from "../kothing-editor.vue";

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
    components: { KothingEditor },
    props: ["update"],

    data: () => ({
        drawer: true,
        blog: {
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
            content: "",
        },
        authorLink: {
            text: "",
            url: "",
            imageSrc: "",
        },
        tag: "",
    }),

    mounted() {
        if (this.$props.update) {
            this.blog = { ...this.$props.update };
            delete this.blog._id;

            this.blog.content = this.$props.update.content;
        }

        const savedContent = localStorage.getItem("blog-data");
        if (savedContent) {
            this.blog = { ...JSON.parse(savedContent) };
        }
    },

    unmounted() {
        localStorage.removeItem("blog-data");
    },

    watch: {
        blog: {
            handler(data) {
                try {
                    localStorage.setItem("blog-data", JSON.stringify(data));
                } catch (e: any) {
                    console.error(e.message);
                }
            },
            deep: true,
        },
    },

    methods: {
        async handleSubmit() {
            try {
                let req = null;
                if (this.$props.update) {
                    req = await new this.Api().put(`/blog/${this.$route.params.blogID}`, {
                        ...this.blog,
                    });
                } else {
                    req = await new this.Api().post("/blog", { ...this.blog });
                    if (req) this.$router.push(`/user/blog/view/${req.data._id}`);
                }

                this.toast.success(`Blog ${this.$props.update ? "updated" : "created"} successfully.`);
            } catch (e: any) {
                this.toast.error(e.message);
            }
        },

        addAuthorLink() {
            this.blog.author.links.push(this.authorLink);
            this.authorLink = {
                text: "",
                url: "",
                imageSrc: "",
            };
        },

        removeAuthorLink(index: number) {
            this.blog.author.links.splice(index, 1);
        },

        addTag() {
            this.blog.tags.push(this.tag.toUpperCase());
            this.tag = "";
        },

        removeTag(index: number) {
            this.blog.tags.splice(index, 1);
            this.tag = "";
        },

        onContentChange(content: any) {
            this.blog.content = content;
        },
    },
};
</script>
