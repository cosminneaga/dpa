<script setup lang="ts">
const bloggerUrl = import.meta.env.VITE_BLOGGER_URL;
</script>

<template>
  <user-layout>
    <v-tabs v-model="tab" color="primary" align-tabs="center" density="comfortable" direction="horizontal">
      <v-tab :value="1">profile</v-tab>
      <v-tab :value="2">external use</v-tab>
      <v-tab :value="3">create user</v-tab>
    </v-tabs>

    <v-window v-model="tab" style="max-width: 1000px; margin-top: 50px" class="mx-auto" disabled>
      <!-- PROFILE -->
      <v-window-item :value="1">
        <ul>
          <li>
            <h2 class="text-h6 text-primary">Name: {{ user.first_name }} {{ user.last_name }}</h2>
          </li>
          <li>
            <h2 class="text-h5 text-primary">Email: {{ user.email }}</h2>
          </li>
          <li>
            <h2 class="text-h6 text-primary">
              Access Token: <i>{{ user.access_token }}</i>
            </h2>
          </li>
        </ul>
      </v-window-item>
      <!-- PROFILE -->

      <!-- EXTERNAL USE -->
      <v-window-item :value="2">
        <div v-highlight>
          <h1 class="text-primary">How to use your external access token</h1>

          <br />
          <h3 class="text-primary">Retrieve entire list of blogs</h3>
          <pre><code class="language-javascript">{{ bloggerUrl }}/external/blogs/{{user.access_token}}</code></pre>

          <br />
          <h3 class="text-primary">Retrieve single blog by id</h3>
          <pre><code class="language-javascript">{{ bloggerUrl }}/external/blog/&lt;blogId&gt;/{{user.access_token}}</code></pre>

          <br />
          <h3 class="text-primary">Fetch</h3>
          <pre><code class="language-javascript">fetch('{{ bloggerUrl }}/external/blogs/{{user.access_token}}')
    .then((response) => response.json())
    .then((data) => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });</code></pre>
        </div>
      </v-window-item>
      <!-- EXTERNAL USE -->

      <!-- CREATE USER -->
      <v-window-item :value="3">
        <CreateUserForm />
      </v-window-item>
    </v-window>
    <!-- CREATE USER -->
  </user-layout>
</template>

<script lang="ts">
import CreateUserForm from "../../components/User/Form/Create.vue";

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
    const req = await new this.Api().get("/user/me");
    if (req) this.user = { ...req.data };
  },
};
</script>
