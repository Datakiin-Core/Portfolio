/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.jinja2',
    './app/**/*.html', // Add HTML files
    './app/**/*.htm',  // Add HTM files
    './app/**/*.js',   // Add JS files
  ],
  theme: {
    extend: {animation: {
      spin: 'spin 1s linear infinite',
      }
    },
  },
  plugins: [],
}

