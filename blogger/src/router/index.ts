import { createRouter, createWebHistory } from "vue-router";

import Home from "../pages/Home.vue";
import About from "../pages/About.vue";

// layouts
import Landing from "../layouts/Landing.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
      meta: {
        layout: Landing,
      },
    },
    {
      path: "/about",
      name: "about",
      component: About,
    },
  ],
});

export default router;
