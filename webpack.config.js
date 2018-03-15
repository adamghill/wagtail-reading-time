module.exports = {
    entry: `./src/index.js`,
    output: {
        filename: `readingtime.bundle.js`,
        path: __dirname + `/readingtime/static`
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: [
                            '@babel/preset-env',
                            '@babel/preset-react'
                        ]
                    }
                }
            }
        ]
    },
    mode: 'production'
};