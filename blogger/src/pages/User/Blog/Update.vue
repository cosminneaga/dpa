<script lang="ts" setup>
import UpdateCreateForm from "@/components/Blog/UpdateCreateForm.vue";
</script>

<template>
    <user-layout>
        <section
            v-if="!dd"
            style="text-align: center;"
        >
            <v-progress-circular
                color="primary"
                indeterminate
                :size="128"
                :width="12"
            ></v-progress-circular>
        </section>
        <UpdateCreateForm
            v-else
            :update="dd"
        ></UpdateCreateForm>
    </user-layout>
</template>

<script lang="ts">
export default {
    data: () => ({
        dd: null,
        loading: false,
    }),

    async mounted() {
        const req = await this.axios.get(`/api/blog/${this.$route.params.blogID}`, {
            headers: {
                "x-access-token": this.$cookies.get("X-Access-Token"),
            },
        });
        if (req) {
            this.dd = req.data.data;
        }
    },
};
</script>