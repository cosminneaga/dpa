<template>
  <user-layout>
    <v-container>
      <section v-if="blogs.length > 0" fluid class="d-flex flex-row flex-wrap justify-center" style="gap: 20px">
        <router-link
          v-for="(item, i) in blogs"
          :key="i"
          :to="`/user/blog/view/${item._id}`"
          style="text-decoration: none"
        >
          <v-card
            width="400"
            height="475"
            :title="item.title"
            :subtitle="item.description"
            ripple
            variant="outlined"
            link
            color="primary"
          >
            <template v-slot:text>
              <div class="card-content" v-html="item.content"></div>
            </template>
          </v-card>
        </router-link>
      </section>

      <section v-else>
        <h3 class="text-h5">
          Seems like you have no blogs created... Go ahead and
          <router-link to="/user/blog/create" class="text-primary">create one</router-link>
          &#128515;
        </h3>
      </section>
    </v-container>
  </user-layout>
</template>

<script lang="ts">
export default {
  data: () => ({
    blogs: [{}],
  }),

  async beforeMount() {
    const req = await new this.Api().get("/blogs");
    if (req) this.blogs = req.data;
  },
};
</script>

<style lang="scss" scoped>
.card-content {
  display: inline-block;
  width: 100%;
  height: auto;
  white-space: nowrap;
  overflow: hidden !important;
  text-overflow: ellipsis;
}
</style>
