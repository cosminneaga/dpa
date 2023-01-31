<template>
    <default-layout>
        <v-card
            variant="outlined"
            width="500"
            class="mx-auto mt-6 pa-4"
        >

            <template #title>
                <h4 class="text-h4">Login to Blogger</h4>
            </template>

            <template #text>
                <v-form>
                    <v-text-field
                        label="E-Mail"
                        type="email"
                        variant="outlined"
                        v-model="email"
                    ></v-text-field>

                    <v-text-field
                        label="Password"
                        type="password"
                        variant="outlined"
                        v-model="password"
                    ></v-text-field>

                    <v-btn
                        color="blue"
                        @click="login"
                    >Login</v-btn>
                </v-form>
            </template>

        </v-card>
    </default-layout>
</template>

<script lang="ts">
export default {
    data: () => ({
        email: "user@gmail.com",
        password: "password",
    }),

    methods: {
        async login() {
            try {
                const req = await this.axios.post("/login", {
                    email: this.email,
                    password: this.password,
                });

                // this.$cookies.set("X-Access-Token", req.data.data.token, Infinity);
                document.cookie = `X-Access-Token=${req.data.data.token}`;
                // localStorage.setItem('blogger-v-1.0', JSON.stringify(req.data.data))
                this.$router.push("/user/home");
            } catch (e) {
                this.$toast.error("An error has arised from ashes!");
            }
        },
    },
};
</script>