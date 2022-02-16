FROM node:16-alpine
WORKDIR /usr/src/app/

ENV PATH /usr/src/app/node_modules.bin:$PATH

COPY app/package.json .
COPY app/package-lock.json .

RUN npm ci
RUN npm install react-scripts@4.0.3 -g --silent

CMD ["npm", "start"]