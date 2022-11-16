<template>
    <v-container>
        <v-alert type="success">I'm a success alert.</v-alert>

        <br>

        <v-alert type="info">I'm an info alert.</v-alert>

        <br>

        <v-alert type="warning">I'm a warning alert.</v-alert>

        <br>

        <v-alert type="error">I'm an error alert.</v-alert>

        <br>

        <v-alert
            density="compact"
            type="info"
        >
            I'm a compact alert with a <strong>type</strong> of info
        </v-alert>

        <br>

        <v-alert
            density="comfortable"
            type="success"
            variant="tonal"
        >
            I'm a comfortable alert with the <strong>text</strong> prop and a <strong>type</strong> of success
        </v-alert>

        <br>

        <v-alert
            border="start"
            density="default"
            type="warning"
        >
            I'm a default alert with the <strong>border</strong> prop and a <strong>type</strong> of warning
        </v-alert>

        <br>

        <!-- Density is "default" by default -->
        <v-alert
            prominent
            type="error"
            variant="outlined"
        >
            I'm a default alert with the <strong>prominent</strong> prop and a <strong>type</strong> of error
        </v-alert>

    </v-container>
</template>