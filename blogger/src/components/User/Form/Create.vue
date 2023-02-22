<template>
    <section>
        <v-card
            variant="outlined"
            max-width="500"
            class="mx-auto mt-6 pa-4"
            color="primary"
        >
            <template #title>
                <h4 class="text-h4 text-primary">Create a new user</h4>
            </template>

            <template #text>
                <v-form @submit.prevent="onSubmitHandler">
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

                    <v-btn color="primary" variant="outlined" type="submit">Create</v-btn>
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
            const req = await new this.Api().put("/register", { ...this.form });

            if (req) {
                this.form = {
                    firstName: "",
                    lastName: "",
                    email: "",
                    password: "",
                };

                this.toast.success("User registered successfully!");
            }
        },
    },
};
</script>
