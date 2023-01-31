<template>
    <user-layout>
        <v-container>
            <h1>Profile</h1>

            <br>

            <ul>
                <li>Name: {{user.first_name}} {{user.last_name}}</li>
                <li>Email: {{user.email}}</li>
                <li>Access Token:
                    <pre><code class="language-markup">{{user.access_token}}</code></pre>
                </li>
            </ul>

            <br>
            <h2>How to use your external access token</h2>

            <br>
            <h3>dev url</h3>
            <br>
            <h4>Retrieve entire list of blogs</h4>
            <pre><code class="language-markup">http://localhost:8080/api/blogger/external/blogs/{{user.access_token}}</code></pre>

            <br>
            <h3>Retrieve single blog by id</h3>
            <pre><code class="language-javascript">http://localhost:8080/api/blogger/external/blog/&lt;blogId&gt;/{{user.access_token}}</code></pre>

            <br>
            <h3>url</h3>
            <pre><code class="language-javascript">https://dpa.cosminneaga.dev/api/blogger/external/blogs/{{user.access_token}}</code></pre>
            <br>
            <h3>fetch</h3>
            <pre><code class="language-javascript">fetch('https://dpa.cosminneaga.dev/api/blogger/external/blogs/{{user.access_token}}')
    .then((response) => response.json())
    .then((data) => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
            </code></pre>

        </v-container>
    </user-layout>
</template>

<script lang="ts">
import Prism from "prismjs";
import "prismjs/themes/prism-tomorrow.css";

export default {
    components: { Prism },
    data: () => ({
        user: {
            first_name: "",
            last_name: "",
            email: "",
            access_token: "",
        },
    }),

    async mounted() {
        // console.log(Prism);
        Prism.highlightAll();

        const req = await this.axios.get("/api/user/me", {
            headers: {
                "x-access-token": this.$cookies.get("X-Access-Token"),
            },
        });
        this.user = { ...req.data.data };

        console.log(this.user);

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