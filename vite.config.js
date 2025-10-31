import { defineConfig } from "vite";

export default defineConfig({
    root: ".", // Project root contains index.html
    base: "./",
    build: {
        outDir: "dist",
        emptyOutDir: true,
        rollupOptions: {
            input: "index.html",
        },
    },
    server: {
        port: 5173,
        open: true,
    },
    resolve: {
        alias: {
            "@": "/src",
        },
    },
});
