1-Pipe all the .html lines of codes that you want to translate
2-Ng extract the files using the following:

npm install @biesbjerg/ngx-translate-extract --save-dev
"scripts": {
  "i18n:init": "ngx-translate-extract --input ./src --output ./src/assets/i18n/template.json --key-as-default-value --replace --format json",
  "i18n:extract": "ngx-translate-extract --input ./src --output ./src/assets/i18n/{en,da,de,fi,nb,nl,sv}.json --clean --format json"
}

npm run i18n:extract
https://www.npmjs.com/package/@biesbjerg/ngx-translate-extract

3-Then use the example.py file to dump the keys with the values of the json keys

4-Then using the translating library yxor/translate-json https://github.com/yxor/translate-json to translate the values

5-the last step is to use the vs code to get rid of the extra object and json files
