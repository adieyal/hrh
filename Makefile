SASS_DIR="site/assets/scss"
CSS_DIR="site/assets/css"

SASS=sass

rebuild: site

css:
	$(SASS) --update ${SASS_DIR}:${CSS_DIR}

site: css
	jekyll build -s site

run: site
	cd _site && python -m SimpleHTTPServer 10000
