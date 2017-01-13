var axios = require('axios');

const HOST = "http://localhost:8000"
const AUTH_URL = `${HOST}/auth`;

module.exports = {
    getToken: function(username, password) {
        var encodedUsername = encodeURIComponent(username);
        var encodedPassword = encodeURIComponent(password)
        var requestUrl = `${AUTH_URL}/${encodedUsername}/${encodedPassword}`;

        return axios.get(requestUrl).then(function (res) {
            console.log(res);
            return res.data.authToken;
        }, function (res) {
            console.log("Error");
            console.log(res);
        });
    }
}