const { execSync } = require('child_process');
require('dotenv').config();

execSync('K6_WEB_DASHBOARD=true');
execSync('K6_WEB_DASHBOARD_OPEN=true');
execSync('K6_WEB_DASHBOARD_EXPORT="html-report.html"')

try {
    execSync(`k6 run --out 'web-dashboard' visit-home-page.js`, { stdio: 'inherit', env: { ...process.env } });
} catch (error) {
    console.error(error)
}
