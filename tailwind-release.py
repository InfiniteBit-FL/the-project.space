import os
from fastmvc.utilities import cache_buster

t = cache_buster(os.curdir)

os.system(f"npx tailwindcss -i ./static_pages/static/css/stylesheet.{t}.css -o ./static_pages/static/css/build.{t}.css --minify")
