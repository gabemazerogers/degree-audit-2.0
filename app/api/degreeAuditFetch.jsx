var axios = require('axios');

// const DEV_HOST = "http://localhost:8000";
const PROD_HOST = "http://138.68.27.99";
const COURSE_URL = `${PROD_HOST}/courses`;

module.exports = {
    getCourses: function(token) {
        var encodedToken = encodeURIComponent(token);
        var requestUrl = `${COURSE_URL}/${token}//`;

        return axios.get(requestUrl).then(function (res) {
            return JSON.stringify(res.data);
        }, function (res) {
            console.log("Error");
            console.log(res);
        });
    }
}