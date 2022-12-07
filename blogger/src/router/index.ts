import { createRouter, createWebHistory } from "vue-router";
import { authGuard } from "@/middleware/auth";

import Home from "@/pages/Home.vue";
import About from "@/pages/About.vue";
import Login from "@/pages/Login.vue";
import Logout from "@/pages/Logout.vue";
import Register from "@/pages/Register.vue";

import NotFound from "@/pages/NotFound.vue";
import Error from "@/pages/Error.vue";

import UserIndex from "@/pages/User/Index.vue";
import UserBlogCreate from "@/pages/User/Blog/Create.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/about",
      name: "about",
      component: About,
    },
    {
      path: "/login",
      component: Login,
    },
    {
      path: "/logout",
      component: Logout,
    },
    {
      path: "/register",
      component: Register,
    },
    {
      path: "/user/home",
      component: UserIndex,
      beforeEnter: [authGuard],
    },
    {
      path: "/user/blog/create",
      component: UserBlogCreate,
      beforeEnter: [authGuard],
    },
    {
      path: "/:pathMatch(.*)*",
      component: NotFound,
    },
    {
      path: "/error",
      component: Error,
    },
  ],
});

export default router;
