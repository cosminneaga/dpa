<template>
  <default-layout>
    <v-card variant="outlined" width="500" class="mx-auto mt-6 pa-4">
      <template #title>
        <h4 class="text-h4">Register with Blogger</h4>
      </template>

      <template #text>
        <v-form>
          <v-text-field label="First Name" variant="outlined"></v-text-field>
          <v-text-field label="Last Name" variant="outlined"></v-text-field>
          <v-text-field label="E-Mail" type="email" variant="outlined"></v-text-field>

          <v-text-field label="Password" type="password" variant="outlined"></v-text-field>
          <v-text-field label="Password Repeat" type="password" variant="outlined"></v-text-field>

          <v-btn color="blue">Register</v-btn>
        </v-form>
      </template>
    </v-card>
  </default-layout>
</template>
