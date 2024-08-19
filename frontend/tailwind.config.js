/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        green: '#04E204',
        red: "#FF3B30",
        yellow: "#FFDB0E",
        blue: "#1E94FA",
        purple: "#B41EFA"
       },
    },
  },
  plugins: [],
}