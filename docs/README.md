# AutoFaker Documentation Website

This directory contains the static website for AutoFaker documentation, designed to be deployed to GitHub Pages.

## 🌐 Website Structure

```text
docs/
├── static/                 # Static website files
│   ├── index.html         # Homepage with features and overview
│   ├── guide.html         # Comprehensive user guide
│   ├── examples.html      # Code examples and patterns
│   ├── styles.css         # CSS styles with dark mode support
│   ├── script.js          # JavaScript functionality
│   └── sw.js             # Service worker for PWA features
├── cheatsheet.ipynb       # Jupyter notebook with examples
└── README.md             # This file
```

## 🚀 Features

- **Modern Design**: Clean, responsive design inspired by successful tech documentation sites
- **Dark Mode**: Automatic and manual dark mode switching
- **Mobile-First**: Responsive design that works on all devices
- **Fast Loading**: Optimized for performance with service worker caching
- **Interactive Examples**: Comprehensive code examples with syntax highlighting
- **Copy-to-Clipboard**: Easy copying of code snippets
- **SEO Optimized**: Proper meta tags and semantic HTML

## 🎨 Design Philosophy

The website follows modern web design principles:

1. **Clean Typography**: Uses Inter for text and JetBrains Mono for code
2. **Consistent Spacing**: Systematic spacing using CSS custom properties
3. **Accessible Colors**: High contrast ratios for readability
4. **Smooth Interactions**: Subtle animations and transitions
5. **Progressive Enhancement**: Works without JavaScript, enhanced with it

## 📱 Responsive Design

- **Desktop**: Full featured layout with sidebar navigation
- **Tablet**: Optimized layout with collapsible navigation
- **Mobile**: Mobile-first design with hamburger menu and touch-friendly buttons

## 🔧 Development

### Local Development

To serve the website locally:

```bash
# Simple HTTP server (Python 3)
cd docs/static
python -m http.server 8000

# Or using Node.js
npx http-server docs/static -p 8000

# Or using Live Server extension in VS Code
```

Then visit `http://localhost:8000`

### Making Changes

1. **Content Changes**: Edit the HTML files directly
2. **Styling**: Modify `styles.css` - uses CSS custom properties for easy theming
3. **Functionality**: Update `script.js` - modular ES6 classes for maintainability
4. **Examples**: Add new examples to `examples.html`

### Theme Customization

The CSS uses custom properties for easy theming:

```css
:root {
    --primary-color: #3b82f6;
    --accent-color: #10b981;
    --background-color: #ffffff;
    /* ... more variables */
}

[data-theme="dark"] {
    --primary-color: #60a5fa;
    --background-color: #0f172a;
    /* ... dark theme overrides */
}
```

## 🚀 Deployment

The website is automatically deployed to GitHub Pages using GitHub Actions:

1. **Trigger**: Pushes to `main` or `master` branch
2. **Build**: Copies static files to deployment directory
3. **Deploy**: Uses GitHub Pages deployment action

### Manual Deployment

To deploy manually:

1. Enable GitHub Pages in repository settings
2. Set source to "GitHub Actions"
3. Push changes to trigger the workflow
4. Website will be available at `https://christianhelle.github.io/autofaker/`

## 🎯 Performance Optimizations

1. **Service Worker**: Caches resources for offline access
2. **Font Loading**: Preloads critical fonts with `font-display: swap`
3. **Image Optimization**: Uses modern formats and lazy loading
4. **CSS**: Minimal, efficient styles with logical organization
5. **JavaScript**: Modern ES6+ with tree-shaking friendly modules

## 📊 Analytics

The website includes hooks for analytics integration:

```javascript
// Track events
Analytics.trackEvent('button_click', { 
    element: 'download_button',
    page: 'homepage' 
});

// Track theme changes
Analytics.trackEvent('theme_change', { 
    theme: 'dark' 
});
```

To add analytics:

1. **Google Analytics**: Add gtag code to `script.js`
2. **Plausible**: Add plausible script and update tracking calls
3. **Custom**: Implement custom tracking in the Analytics class

## 🔍 SEO Features

- **Semantic HTML**: Proper heading hierarchy and landmarks
- **Meta Tags**: Comprehensive meta tags for social sharing
- **Structured Data**: JSON-LD for search engines
- **Sitemap**: Generated sitemap for better indexing
- **Performance**: Optimized Core Web Vitals

## ♿ Accessibility

- **Keyboard Navigation**: Full keyboard support
- **Screen Readers**: Proper ARIA labels and landmarks
- **Color Contrast**: WCAG AA compliant color ratios
- **Focus Management**: Visible focus indicators
- **Reduced Motion**: Respects user motion preferences

## 🔄 Maintenance

### Regular Updates

1. **Dependencies**: Keep fonts and external resources updated
2. **Content**: Update examples and documentation as library evolves
3. **Performance**: Monitor and optimize loading times
4. **Security**: Review and update security headers

### Browser Support

- **Modern Browsers**: Chrome 88+, Firefox 85+, Safari 14+, Edge 88+
- **Progressive Enhancement**: Core functionality works in older browsers
- **Polyfills**: Minimal polyfills for critical features

## 📝 Content Guidelines

When adding new content:

1. **Code Examples**: Include complete, runnable examples
2. **Documentation**: Keep language clear and beginner-friendly
3. **Examples**: Show both basic and advanced use cases
4. **Consistency**: Follow established patterns and terminology

## 🤝 Contributing

To contribute to the documentation:

1. Fork the repository
2. Make changes to files in `docs/static/`
3. Test locally using a local server
4. Submit a pull request

For major changes, please open an issue first to discuss the proposed changes.

## 📄 License

The documentation is licensed under the same terms as the AutoFaker project (MIT License).
