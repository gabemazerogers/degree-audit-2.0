var React = require('react');

var AuthForm = React.createClass({
    onFormSubmit: function(e) {
        e.preventDefault();
        var username = this.refs.username.value;
        var password = this.refs.password.value;

        if (username.length > 0 && password.length > 0) {
            this.refs.username.value = '';
            this.refs.password.value = '';
            this.props.onAuth(username, password);
        }
    },
    render: function () {
        return (
            <div>
                <form onSubmit={this.onFormSubmit}>
                    <input type="text" placeholder="PID" ref="username"/>
                    <input type="password" ref="password"/>
                    <button>Authenticate</button>
                </form>
            </div>
        )
    }
});

module.exports = AuthForm;