import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

import "./assets/main.css";

import axios from "axios";
import VueAxios from "vue-axios";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

import Landing from "./layouts/Landing.vue";
import User from "./layouts/User.vue";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(VueAxios, axios);

const vuetify = createVuetify({
  components,
  directives,
});
app.use(vuetify);

app.mount("#app");

app.component("landing-layout", Landing);
