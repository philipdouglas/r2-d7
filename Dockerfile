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
COPY *.coffee /usr/src/app/
COPY *.js /usr/src/app/
# RUN cat cards-common.coffee cards-en.coffee > cards-combined.coffee
RUN iced -c r2d7.coffee cardlookup.coffee utils.coffee listprinter.coffee
#cards-combined.coffee

#set startup commands
CMD ["node", "r2d7.js"]
