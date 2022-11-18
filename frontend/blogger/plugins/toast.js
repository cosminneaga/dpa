import ToastPlugin from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';

export default defineNuxtPlugin(nuxtApp => {

    nuxtApp.vueApp.use(ToastPlugin, {
        position: 'top-left',
        icon: true,
        duration: 3000,
    })
})