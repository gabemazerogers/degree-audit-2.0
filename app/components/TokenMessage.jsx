var React = require('react');

var TokenMessage = React.createClass({
    render: function () {
        var {token} = this.props;
        return (
            <h3>Your API Token is {token}</h3>
        );
    }
});

module.exports = TokenMessage;