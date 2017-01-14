var React = require('react');

var Token = React.createClass({
    render: function () {
        var {token} = this.props;
        return (
            <h3>Your API Token is {token}!</h3>
        );
    }
});

module.exports = Token;