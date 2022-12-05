import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

import "./assets/main.css";

import axios from "axios";
import VueAxios from "vue-axios";

axios.defaults.headers['x-access-token'] = 'bra'

// Layouts
import Default from "@/layouts/Default.vue";
import User from "@/layouts/User.vue";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import '@mdi/font/css/materialdesignicons.css';

import Toaster from "@meforma/vue-toaster";

import VueCookies from 'vue3-cookies'

const app = createApp(App);

const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: 'light'
  },
});

app
.use(vuetify)
.use(createPinia())
.use(router)
.use(VueAxios, axios)
.use(Toaster, {
  position: 'top-right'
})
.use(VueCookies, {
  expireTimes: "30d",
  path: "/",
  domain: "",
  secure: true,
  sameSite: "None"
});
app.component("default-layout", Default).component("user-layout", User);


axios.interceptors.response.use(function (response) {
  return response;
}, function (error) {
  console.warn(error.code, error.message);
});

app.mount("#app");