var React = require('react');
var AuthForm = require('AuthForm');
var TokenMessage = require('TokenMessage');
var degreeAuditAuth = require('degreeAuditAuth');

var Auth = React.createClass({
    getInitialState: function() {
        return {
            isLoading: false
        }
    },
    handleAuth: function(username, password) {
        var that = this;
        this.setState({
            isLoading: true
        });

        degreeAuditAuth.getToken(username,password).then(function (token) {
            that.setState({
                token: token,
                username: username,
                password: password,
                isLoading: false
            });
        }, function (errorMessage) {
            alert(errorMessage);
            that.setState({
                isLoading: false,
                token: "",
                username: "",
                password: ""
            });
        });
    },
    
    render: function() {
        var {isLoading, username, password, token} = this.state;

        function renderMessage () {
            if (isLoading) {
                return <h3>Fetching token...</h3>;
            } else if (token) {
                return (
                    <div>
                        <TokenMessage token={token}/>
                    </div>
                )
            }
        }

        return (
            <div>
                <AuthForm onAuth={this.handleAuth}/>
                {renderMessage()}
            </div>
        );
    }
});

module.exports = Auth;