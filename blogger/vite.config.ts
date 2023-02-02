import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";
// import dotenv from 'dotenv';
// dotenv.config()

// https://vitejs.dev/config/
export default defineConfig({

  server: {
    host: "0.0.0.0",
    port: 1000,
    // proxy: {
    //   '/blogger': {
    //     target: process.env.VITE_BLOGGER_URL,
    //     secure: false,
    //     changeOrigin: true, // If your backend API is not running on the localhost, we need to make this flag true.
    //     rewrite: path => path.replace(/^\/blogger/, '')
    //   }
    // }
  },

  preview: {
    host: '0.0.0.0',
    port: 1000,
    cors: true,
    // proxy: {
    //   '/blogger': {
    //     target: "http://120.0.0.1:8080/api/blogger",
    //     secure: false,
    //     changeOrigin: true, // If your backend API is not running on the localhost, we need to make this flag true.
    //     rewrite: path => path.replace(/^\/blogger/, '')
    //   }
    // }
  },

  plugins: [vue(), vueJsx()],

  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },

  build: {
    chunkSizeWarningLimit: 1500,
  },
});
