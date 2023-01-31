import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";
import dotenv from 'dotenv';
dotenv.config()

// https://vitejs.dev/config/
export default defineConfig({

  server: {
    host: "0.0.0.0",
    port: 1000,
    cors: false,
    proxy: {
      '/api': {
        target: process.env.BLOGGER_URL,
        secure: false,
        changeOrigin: true, // If your backend API is not running on the localhost, we need to make this flag true.
        rewrite: (path: any) => path.replace("/api", "")
      }
    }
  },

  preview: {
    host: '0.0.0.0',
    port: 1000,
    cors: false,
    proxy: {
      '/api': {
        target: process.env.BLOGGER_URL,
        secure: false,
        changeOrigin: true, // If your backend API is not running on the localhost, we need to make this flag true.
        rewrite: (path: any) => path.replace("/api", "")
      }
    }
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
