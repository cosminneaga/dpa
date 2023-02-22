import App from "./App.vue";
import router from "./router";
import { createApp } from "vue";
import { createPinia } from "pinia";

// vue-toaster
// import Vue3Toastify, { type ToastContainerOptions } from 'vue3-toastify';
import "vue3-toastify/dist/index.css";
import { toast } from "vue3-toastify";

// vue-cookies
import VueCookies from "vue3-cookies";

// css
import "./assets/main.scss";

// Layouts
import Default from "@/layouts/Default.vue";
import User from "@/layouts/User.vue";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import "@mdi/font/css/materialdesignicons.css";

// Syntax Highlighter
import VueCodeHighlight from "vue-code-highlight";
import "vue-code-highlight/themes/prism-tomorrow.css";

// axios handler
import Api from "./utils/AxiosHandler";

const app = createApp(App);

// configure vuetify
const vuetifyTheme = {
  dark: false,
  colors: {
    // background: "#FFFFFF",
    background: "#0E101A",

    // surface: "#FFFFFF",
    surface: "#000",

    // primary: "#1381d3",
    // primary: "#C46D5E",
    primary: "#39D055",
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
  },
});

app
  .use(createPinia())
  .use(router)
  .use(vuetify)
  .use(VueCookies, {
    expireTimes: "30d",
    path: "/",
    domain: "",
    secure: true,
    sameSite: "None",
  })
  .use(VueCodeHighlight);

// set layouts
app.component("default-layout", Default).component("user-layout", User);

// set global variables
app.config.globalProperties.toast = toast;
app.config.globalProperties.Api = Api;

// mount app
app.mount("#app");
