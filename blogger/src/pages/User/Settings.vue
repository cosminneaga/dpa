<template>
    <user-layout>
        <v-container>
            <h1>Profile</h1>

            <br>

            <ul>
                <li>Name: {{user.first_name}} {{user.last_name}}</li>
                <li>Email: {{user.email}}</li>
                <li>Access Token: {{user.access_token}}</li>
            </ul>
        </v-container>
    </user-layout>
</template>

<script lang="ts">
export default {
    data: () => ({
        user: {
            first_name: "",
            last_name: "",
            email: "",
            access_token: "",
        },
    }),

    async mounted() {
        const req = await this.axios.get("/api/user/me", {
            headers: {
                "x-access-token": this.$cookies.get("X-Access-Token"),
            },
        });
        this.user = { ...req.data.data };

        console.log(this.user);
    },
};
</script>