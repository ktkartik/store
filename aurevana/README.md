# AUREVANA — luxury haircare demonstration

## Open the website
Open `AUREVANA-preview.html` in Chrome, Edge or Firefox. All CSS, JavaScript and WebP imagery are embedded. No installation, server or internet required. Local storage is supported when permitted by your browser. For more predictable persistence, serve it with `python -m http.server 8000` and open `http://localhost:8000/AUREVANA-preview.html`.

## Developer source
Install Node.js, then run `npm install` and `npm run dev`. For static deployment, run `npm run build` and upload `dist/`. The Vite entry uses a React/TypeScript wrapper around the shared modular JavaScript storefront; CSS and hash routing are implemented without Tailwind, Framer Motion, React Router or Lucide dependencies. Npm access was unavailable during development, so this entry has not been dependency-installed or build-tested. The standalone preview is the dependency-free version. Rebuild it after editing source with `python build_preview.py`.

## Customization
- `src/config/brand.js`: brand, contact, shipping and promotion settings.
- `src/data/catalog.js`: products, ingredients, reviews and journal articles.
- `src/styles/main.css`: colors, typography, layout and animations.
- `src/pages/storefront.js`: page templates and UI.
- `src/context/store.js`: cart, wishlist, totals and local persistence.
- `public/images/`: original generated concept imagery, cropped into WebP assets. Several product variants, ingredient and ritual images reuse concept crops; they are not accurate individual product photos or botanical identification references. The packaging wordmark in images must be separately updated when rebranding.

## Demo behavior
Browse six fictional products, filter and sort, search, save to wishlist, add to bag, change quantity, apply `WELCOME10` for a 10% discount and place a demo order using the fill-example button. Free shipping threshold ₹999, sample standard fee ₹79. No real payment, authentication, delivery, or backend. No personal information submitted to a server or persisted. Fictional ratings are labeled. Size selector shows the single sample size per product. Social buttons show a demo message instead of opening nonexistent accounts. Google Fonts are optional in the Vite version; offline preview uses system fallbacks.
