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
                    ></v-text-field>

                    <v-text-field
                        label="Password"
                        type="password"
                        variant="outlined"
                    ></v-text-field>

                    <v-btn color="blue">Login</v-btn>
                </v-form>
            </template>

        </v-card>
    </NuxtLayout>
</template>