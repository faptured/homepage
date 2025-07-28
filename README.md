# Faptured Homepage

This is the main homepage for the Faptured platform, built with Jekyll.

## Structure

```
homepage/
├── _config.yml          # Jekyll configuration
├── _layouts/           # Page layouts
│   └── default.html    # Main layout template
├── _includes/          # Reusable components
│   ├── head-custom.html
│   └── seo.html
├── assets/             # Static assets
│   ├── css/
│   │   └── style.css   # Main stylesheet
│   └── js/
│       └── scale.fix.js
├── features/           # Features section
│   └── index.html
├── content/            # Content pages
│   └── sample-compilation.md
├── index.html          # Homepage
├── Gemfile            # Ruby dependencies
└── README.md          # This file
```

## Development

To run the site locally:

1. Install Jekyll and dependencies:
   ```bash
   bundle install
   ```

2. Serve the site:
   ```bash
   bundle exec jekyll serve
   ```

3. Visit `http://localhost:4000` in your browser

## Features

- **Responsive Design**: Works on all devices
- **SEO Optimized**: Built-in SEO tags and metadata
- **Fast Loading**: Optimized assets and minimal dependencies
- **Content Collections**: Organized content and features sections
- **Attribution Focus**: Designed to showcase proper content attribution

## Customization

- Edit `_config.yml` to change site settings
- Modify `assets/css/style.css` for styling changes
- Add new pages in the root directory or within collections
- Update layouts in `_layouts/` for structural changes

## Deployment

This site is designed to be deployed on GitHub Pages or any static hosting service that supports Jekyll.

## Related

- [Links App](../links/) - Attribution links repository
- [Faptured Documentation](#) - Full platform documentation