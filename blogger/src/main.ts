import App from "./App.vue";
import router from "./router";
import { createApp } from "vue";
import { createPinia } from "pinia";

// vue-toaster
import Toaster from "@meforma/vue-toaster";
import { createToaster } from "@meforma/vue-toaster";
const toaster = createToaster();

// vue-cookies
import VueCookies from "vue3-cookies";

// css
import "./assets/main.css";

// axios
import VueAxios from "vue-axios";
import axios from "axios";

// Layouts
import Default from "@/layouts/Default.vue";
import User from "@/layouts/User.vue";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import "@mdi/font/css/materialdesignicons.css";


const app = createApp(App);

// app.config.globalProperties.axios = axios;
// axios.defaults.headers["x-access-token"] = "bra";

// configure vuetify
const vuetifyTheme = {
  dark: false,
  colors: {
    background: "#FFFFFF",
    surface: "#FFFFFF",
    primary: "#1381d3",
    "primary-darken-1": "#3700B3",
    secondary: "#03DAC6",
    "secondary-darken-1": "#018786",
    error: "#B00020",
    info: "#2196F3",
    success: "#4CAF50",
    warning: "#FB8C00",
  },
};
const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: "vuetifyTheme",
    themes: {
      vuetifyTheme,
    },
  }
});

app
  .use(createPinia())
  .use(router)
  .use(VueAxios, axios)
  .use(vuetify)
  .use(Toaster, {
    position: "top-right",
  })
  .use(VueCookies, {
    expireTimes: "30d",
    path: "/",
    domain: "",
    secure: true,
    sameSite: "None",
  });

// set layouts
app.component("default-layout", Default).component("user-layout", User);

// config axios
axios.defaults.baseURL = import.meta.env.VITE_BLOGGER_URL
axios.interceptors.response.use(
  function (response: any) {
    if (response.data.status === 401) {
      toaster.error("Not Authorized.");
    } else if (response.data.status === 404) {
      toaster.error("Resource not found.");
    }
    return response;
  },
  function (error: any) {

    if (error.response.status === 404) {
      toaster.error("Resource not found.");
    } else if (error.response.status === 400) {
      toaster.error(error.response.data.message);
    }

    console.error(error.code, error.message);
  }
);

// mount app
app.mount("#app");
