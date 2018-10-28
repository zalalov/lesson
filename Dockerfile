FROM lesson:8

RUN apt-get update -qq && apt-get install -qqy git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /frontend

RUN npm -g install npm
RUN npm -g install phantomjs-prebuilt --phantomjs_cdnurl=http://cnpmjs.org/downloads --unsafe-perm
RUN npm -g install webpack@^3.0.0

ADD . /frontend
CMD ["./watch.sh"]
