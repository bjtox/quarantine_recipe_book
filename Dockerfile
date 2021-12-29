FROM vorakl/alpine-pelican
RUN pip install --upgrade pelican
RUN pip install beautifulsoup4
