import { defineConfig } from "vite";
import eslintPlugin from "vite-plugin-eslint";
import react from "@vitejs/plugin-react";
import { NodeGlobalsPolyfillPlugin } from '@esbuild-plugins/node-globals-polyfill';

// https://vitejs.dev/config/
export default defineConfig((mode) => ({
  plugins: [
    react(),
    eslintPlugin({
      lintOnStart: true,
      failOnError: mode === "production",
    }),
    NodeGlobalsPolyfillPlugin({
      process: true,
      buffer: true,
      define: {
        'process.env.NODE_ENV': '"production"',
      },
    }),
  ],
  server: {
    open: true,
    proxy: {
      "/api": "http://127.0.0.1:5000",
    },
  },
  optimizeDeps: {
    esbuildOptions: {
      define: {
        global: 'globalThis',
      },
    },
  },
}));
