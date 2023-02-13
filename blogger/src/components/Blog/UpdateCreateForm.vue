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
                            v-model="blog.title"
                        ></v-text-field>
                        <v-textarea
                            label="Description"
                            density="comfortable"
                            variant="outlined"
                            v-model="blog.description"
                        ></v-textarea>

                        <!-- IMAGE -->
                        <p>Image</p>
                        <section style="display: flex; gap:10px;">
                            <v-text-field
                                variant="outlined"
                                density="compact"
                                label="alt"
                                v-model="blog.image.alt"
                            ></v-text-field>
                            <v-text-field
                                variant="outlined"
                                density="compact"
                                label="title"
                                v-model="blog.image.title"
                            ></v-text-field>
                        </section>
                        <v-text-field
                            variant="outlined"
                            density="compact"
                            label="src"
                            v-model="blog.image.src"
                        ></v-text-field>

                        <!-- AUTHOR -->
                        <p>Author</p>
                        <v-text-field
                            variant="outlined"
                            density="comfortable"
                            label="Full Name"
                            v-model="blog.author.name"
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
                                        v-for="(item, i) in blog.author.links"
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
                            v-model="blog.category"
                        ></v-text-field>

                        <!-- TAGS -->
                        <section class="my-3">
                            <v-row
                                class="pa-5"
                                style="gap:10px;"
                            >
                                <v-chip
                                    v-for="(item, i) in blog.tags"
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
                    <v-btn
                        @click="handleSubmit"
                        color="success"
                        class="mb-4"
                        size="large"
                    >Submit Blog</v-btn>

                    <!-- <quill-editor
                        ref="editor"
                        @editorChange="onContentChange"
                        content="html"
                    ></quill-editor> -->

                    <kothing-editor
                        @on-change="(content) => onContentChange(content)"
                        :contentSet="update ? update.content : null"
                    />

                    <v-btn
                        @click="handleSubmit"
                        color="success"
                        class="mt-4"
                        size="large"
                    >Submit Blog</v-btn>
                </v-container>
            </v-col>
        </v-row>
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
                    req = await this.axios.put(
                        `/blog/${this.$route.params.blogID}`,
                        { ...this.blog },
                        {
                            headers: {
                                "x-access-token": this.$cookies.get("X-Access-Token"),
                            },
                        }
                    );
                } else {
                    req = await this.axios.post(
                        "/blog",
                        { ...this.blog },
                        {
                            headers: {
                                "x-access-token": this.$cookies.get("X-Access-Token"),
                            },
                        }
                    );
                    
                    this.$router.push(`/user/blog/view/${req.data.data._id}`)
                }                

                this.$toast.success(`Blog ${this.$props.update ? "updated" : "created"} successfully.`);
            } catch (error) {
                console.error(error);
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
            this.blog.tags.push(this.tag);
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