<template>
    <NuxtLayout>

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
    </NuxtLayout>
</template>
<script>
export default {
    data: () => ({
        email: "user@gmail.com",
        password: "password",
    }),

    methods: {
        async login() {
            const d = {
                email: this.email,
                password: this.password,
            };

            try {
                const res = await $fetch(
                    "http://localhost:8080/api/blogger/login",
                    {
                        method: "POST",
                        body: d,
                    }
                );

                console.log(res);

                localStorage.setItem("blogger", JSON.stringify(res.data));
                this.$router.push("/user/home");
            } catch (e) {
                console.log(e.response);
                this.$toast.error(e.response._data.message);
            }
        },
    },
};
</script>