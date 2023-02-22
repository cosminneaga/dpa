<template>
    <default-layout>
        <v-card variant="outlined" max-width="500" class="mx-auto mt-6 pa-4" color="primary">
            <template #title>
                <h4 class="text-h4 text-primary mb-10">Login to Blogger</h4>
            </template>

            <template #text>
                <v-form @submit.prevent="login">
                    <v-text-field label="E-Mail" type="email" variant="outlined" v-model="email"></v-text-field>

                    <v-text-field label="Password" type="password" variant="outlined" v-model="password"></v-text-field>

                    <v-btn color="primary" variant="tonal" type="submit">Login</v-btn>
                </v-form>
            </template>
        </v-card>
    </default-layout>
</template>

<script lang="ts">
export default {
    data: () => ({
        email: "",
        password: "",
    }),

    methods: {
        async login() {
            const req = await new this.Api().post("/login", {
                email: this.email,
                password: this.password,
            });
            if (req) {
                document.cookie = `X-Access-Token=${req.data.token}`;
                this.$router.push("/user/home");
            }
        },
    },
};
</script>
