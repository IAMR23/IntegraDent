/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        "mi-coffe": "#B5985C", // Código hexadecimal
      },
    },
  },
  plugins: [],
};
