<script setup lang="ts">
const bloggerUrl = import.meta.env.VITE_BLOGGER_URL;
</script>

<template>
    <user-layout>

        <v-tabs
            v-model="tab"
            color="deep-purple-accent-4"
            align-tabs="center"
        >
            <v-tab :value="1">external use</v-tab>
            <v-tab :value="2">profile</v-tab>
            <v-tab :value="3">create user</v-tab>
        </v-tabs>

        <v-window
            v-model="tab"
            style="max-width: 1000px; margin-top: 50px;"
            class="mx-auto"
        >

            <v-window-item :value="1">
                <div v-highlight>
                    <h2>How to use your external access token</h2>

                    <br>
                    <h3>dev url</h3>
                    <br>
                    <h4>Retrieve entire list of blogs</h4>
                    <pre><code class="language-javascript">{{ bloggerUrl }}/external/blogs/{{user.access_token}}</code></pre>

                    <br>
                    <h3>Retrieve single blog by id</h3>
                    <pre><code class="language-javascript">{{ bloggerUrl }}/external/blog/&lt;blogId&gt;/{{user.access_token}}</code></pre>

                    <br>
                    <h3>fetch</h3>
                    <pre class="language-javascript"><code>fetch('{{ bloggerUrl }}/external/blogs/{{user.access_token}}')
    .then((response) => response.json())
    .then((data) => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
            </code></pre>
                </div>
            </v-window-item>

            <v-window-item :value="2">
                <ul v-highlight>
                    <li>Name: {{user.first_name}} {{user.last_name}}</li>
                    <li>Email: {{user.email}}</li>
                    <li>Access Token:
                        <!-- <pre><code class="language-plaintext">{{user.access_token}}</code></pre> -->
                        <pre><code class="language-javascript" data-prismjs-copy="Copy the JavaScript snippet!">{{user.access_token}}</code></pre>
                    </li>
                </ul>
            </v-window-item>

            <v-window-item :value="3">
                <CreateUserForm />
            </v-window-item>
        </v-window>

    </user-layout>
</template>

<script lang="ts">
import CreateUserForm from "../../components/User/Form/Create.vue";
// import Prism from "prismjs";
// import "prismjs/themes/prism-tomorrow.css";

export default {
    components: { CreateUserForm },
    data: () => ({
        tab: null,
        user: {
            first_name: "",
            last_name: "",
            email: "",
            access_token: "",
        },
    }),

    async mounted() {
        const req = await this.axios.get("/user/me", {
            headers: {
                "x-access-token": this.$cookies.get("X-Access-Token"),
            },
        });
        this.user = { ...req.data.data };
        await this.fetchExternal(req.data.data.access_token);
    },

    methods: {
        async fetchExternal(token) {
            // testing external
            // blog list
            const externalReq = await this.axios.get("http://localhost:8080/api/blogger/external/blogs/" + token);
            console.log("EXTERNAL ", externalReq);

            //single blog
            const externalBlogReq = await this.axios.get(
                `http://localhost:8080/api/blogger/external/blog/${externalReq.data.data[0]["_id"]}/${token}`
            );

            console.log("EXTERNAL BLOG ", externalBlogReq);
        },
    },
};
</script>