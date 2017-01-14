module.exports = {
    entry: './app/app.jsx',
    output: {
        path: __dirname,
        filename: './public/bundle.js'
    },
    resolve: {
        root: __dirname,
        alias: {
            degreeAuditAuth: 'app/api/degreeAuditAuth.jsx',
            Auth: 'app/components/Auth.jsx',
            AuthForm: 'app/components/AuthForm.jsx',
            Token: 'app/components/Token.jsx',
            degreeAuditFetch: 'app/api/degreeAuditFetch.jsx',
            FetchForm: 'app/components/FetchForm.jsx',
            Courses: 'app/components/Courses.jsx',
            Course: 'app/components/Course.jsx'
        },
        extensions: ['', '.js', '.jsx']
    },
    module: {
        loaders: [{
            loader: 'babel-loader',
            query: {
                presets: ['react', 'es2015', 'stage-0']
            },
            test: /\.jsx?$/,
            exclude: /(node_modules|bower_components)/
        }]
    }
};