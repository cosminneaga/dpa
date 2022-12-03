import { createRouter, createWebHistory } from "vue-router";

import Home from "@/pages/Home.vue";
import About from "@/pages/About.vue";
import Login from "@/pages/Login.vue";
import Register from "@/pages/Register.vue";

import NotFound from "@/pages/NotFound.vue";
import Error from "@/pages/Error.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
      meta: {
       
      },
    },
    {
      path: "/about",
      name: "about",
      component: About,
    },
    {
      path: "/login",
      component: Login
    },
    {
      path: "/register",
      component: Register
    },
    {
      path: '/:pathMatch(.*)*',
      component: NotFound
    },
    {
      path: '/error',
      component: Error
    }
  ],
});

export default router;
