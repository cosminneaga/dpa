import { createApp } from "vue";
import { createPinia } from "pinia";

import Toaster from "@meforma/vue-toaster";
import {createToaster} from "@meforma/vue-toaster";
const toaster = createToaster();
import VueCookies from 'vue3-cookies'

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

// Quill
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import '@vueup/vue-quill/dist/vue-quill.bubble.css';
import {QuillEditor} from '@vueup/vue-quill';
QuillEditor.props.globalOptions.default = () => {
  return {
    debug: 'warn',
    placeholder: 'Compose an epic..',
    theme: 'bubble',
    modules: {
      toolbar: [
        ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
        ['blockquote', 'code-block'],
      
        [{ 'header': 1 }, { 'header': 2 }],               // custom button values
        [{ 'list': 'ordered'}, { 'list': 'bullet' }],
        [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
        [{ 'indent': '-1'}, { 'indent': '+1' }],          // outdent/indent
        [{ 'direction': 'rtl' }],                         // text direction
      
        [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
        [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
      
        [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
        [{ 'font': [] }],
        [{ 'align': [] }],
        ['image'],
      
        ['clean']   
      ]
    }
  }
}

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
app
.component("default-layout", Default)
.component("user-layout", User)
.component("QuillEditor", QuillEditor);

axios.interceptors.response.use(function (response: any) {
  if (response.data.status === 401) {
    toaster.error('Not Authorized.')
  }
  return response;
}, function (error: any) {
  console.warn(error.code, error.message);
});

app.mount("#app");