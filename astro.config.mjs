import { defineConfig } from 'astro/config';

export default defineConfig({
  // 🔥 Build statique (pas de SSR, pas besoin de Node adapter)
  output: 'static',

  server: {
    hmr: {
      clientPort: 4321
    }
  },

  vite: {
    resolve: {
      alias: {
        // tu peux mettre d'autres alias ici si besoin
      }
    }
  }
});
