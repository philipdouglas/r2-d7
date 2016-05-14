# Taken from https://lostechies.com/andrewsiemer/2016/04/14/building-a-slack-bot-with-botkit-node-and-docker/
FROM node:argon

# create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install node modules
COPY package.json /usr/src/app/
RUN npm --no-color install
# Install iced coffee with -g so we can call it later
RUN npm --no-color -g install iced-coffee-script

# Build js files
COPY r2d7.coffee /usr/src/app/
COPY cards-common.coffee /usr/src/app/
COPY cards-en.coffee /usr/src/app/
RUN iced -j cards-combined.coffee -c cards-common.coffee cards-en.coffee
RUN iced -c r2d7.coffee

#set startup commands
CMD ["node", "r2d7.js"]
