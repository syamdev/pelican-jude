# pelican-jude
Build Static Site with Python Pelican Static Site Generator

## Commands

- Run dev server in output directory
`$ python -m http.server`
  
- To (re)generate site
  `$ pelican -s pelicanconf.py -o output` or `$ make html`

- To (re)generate the site with a theme overriding
  `$ pelican -s pelicanconf.py -o output -t theme content`

- Remove the generated files in output directory
  `$ make clean`
  
## Site Demo
- [Italian Foodie](https://italian-foodie.netlify.app)