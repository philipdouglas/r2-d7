# Taken from https://lostechies.com/andrewsiemer/2016/04/14/building-a-slack-bot-with-botkit-node-and-docker/
FROM node:argon

# create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install node modules
COPY package.json /usr/src/app/
RUN npm install

# Build js files
COPY r2d7.coffee /usr/src/app/
COPY cards-common.coffee /usr/src/app/
iced -c r2d7.coffee cards-common.coffee

#set startup commands
CMD ["node", "r2d7.js"]
