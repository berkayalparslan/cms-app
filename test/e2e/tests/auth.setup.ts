import {expect, test as setup} from '@playwright/test';
import path from 'path';

const authFile = path.join(__dirname, '../.auth/admin.json');
setup('auth setup - admin', async({request}) => {
    const adminLogin = process.env.ADMIN_LOGIN;
    const adminPassword = process.env.ADMIN_PASSWORD;

    const getLogin = await request.get('/users/login/');
    const headers = getLogin.headers();
    const setCookieHeader = headers['set-cookie'];
    const match = setCookieHeader.match(/csrftoken=([^;]+)/);
    const token = match ? match[1] : "";

    const res = await request.post('users/login/', {
        form:{
            username: adminLogin,
            password: adminPassword,
            csrfmiddlewaretoken: token
        }
    })
    await expect(res.status()).toBe(200);
    await expect(res.ok()).toBeTruthy();
    await request.storageState({path: authFile});
})