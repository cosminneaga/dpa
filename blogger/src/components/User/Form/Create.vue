<template>
    <section>
        <v-card
            variant="outlined"
            max-width="500"
            class="mx-auto mt-6 pa-4"
        >

            <template #title>
                <h4 class="text-h4">Register with Blogger</h4>
            </template>

            <template #text>
                <v-form @submit.prevent>
                    <v-text-field
                        label="First Name"
                        variant="outlined"
                        v-model="form.firstName"
                    ></v-text-field>
                    <v-text-field
                        label="Last Name"
                        variant="outlined"
                        v-model="form.lastName"
                    ></v-text-field>
                    <v-text-field
                        label="E-Mail"
                        type="email"
                        variant="outlined"
                        v-model="form.email"
                    ></v-text-field>

                    <v-text-field
                        label="Password"
                        type="password"
                        variant="outlined"
                        v-model="form.password"
                    ></v-text-field>
                    <!-- <v-text-field
                        label="Password Repeat"
                        type="password"
                        variant="outlined"
                    ></v-text-field> -->

                    <v-btn
                        color="blue"
                        @click="onSubmitHandler"
                    >Register</v-btn>
                </v-form>
            </template>

        </v-card>
    </section>
</template>

<script lang="ts">
export default {
    data: () => ({
        form: {
            firstName: "",
            lastName: "",
            email: "",
            password: "",
        },
    }),

    methods: {
        async onSubmitHandler() {
            try {
                const req = await this.axios.put(
                    "/register",
                    { ...this.form },
                    {
                        headers: {
                            "x-access-token": this.$cookies.get("X-Access-Token"),
                        },
                    }
                );

                console.log(req);
                

                this.form = {
                    firstName: '',
                    lastName: '',
                    email: '',
                    password: '',
                }

                this.toast.success("User registered successfully!");
            } catch (e: any) {              
                this.toast.error(e.message);
            }
        },
    },
};
</script>