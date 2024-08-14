const path = require('path');
require('dotenv').config({ path: path.resolve(__dirname, '../../.env') });


export const DOMAIN_NAME = process.env.DOMAIN_NAME;
export const DOMAIN_FOR_IMG = process.env.DOMAIN_NAME;