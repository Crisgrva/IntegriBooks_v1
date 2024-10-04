FROM node:18.19.1

WORKDIR /app

COPY package*.json ./

RUN npm i -g @angular/cli@18.2.6
RUN npm i

COPY . .

EXPOSE 4200

CMD ["npm", "run", "start"]
