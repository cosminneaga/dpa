<template>
  <user-layout>
    <section v-if="!dd" style="text-align: center">
      <v-progress-circular color="primary" indeterminate :size="128" :width="12"></v-progress-circular>
    </section>
    <UpdateCreateForm v-else :update="dd"></UpdateCreateForm>
  </user-layout>
</template>

<script lang="ts">
import UpdateCreateForm from "../../../components/Blog/UpdateCreateForm.vue";

export default {
  components: { UpdateCreateForm },

  data: () => ({
    dd: null,
    loading: false,
  }),

  async mounted() {
    const req = await new this.Api().get(`/blog/${this.$route.params.blogID}`);
    if (req) this.dd = req.data;
  },
};
</script>
