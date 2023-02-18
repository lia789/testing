/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html,js}"],
  theme: {
    extend: {
      colors: {
        white: "#fff",
        black: "#000",
        "button-color": "#f0351c",
        lightcoral: "rgba(229, 127, 127, 0.9)",
      },
      fontFamily: { "button-text": "Inter" },
      borderRadius: { small: "5px", base: "10px" },
    },
    fontSize: { base: "15px" },
  },
  corePlugins: { preflight: false },
};
