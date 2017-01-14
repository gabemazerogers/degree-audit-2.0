var axios = require('axios');

// const DEV_HOST = "http://localhost:8000";
const PROD_HOST = "http://138.68.27.99";
const AUTH_URL = `${PROD_HOST}/auth`;

module.exports = {
    getToken: function(username, password) {
        var encodedUsername = encodeURIComponent(username);
        var encodedPassword = encodeURIComponent(password)
        var requestUrl = `${AUTH_URL}/${encodedUsername}/${encodedPassword}`;

        return axios.get(requestUrl).then(function (res) {
            return res.data.authToken;
        }, function (res) {
            console.log("Error");
            console.log(res);
        });
    }
}