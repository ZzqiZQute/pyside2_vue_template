module.exports = {
    root: true,
    parserOptions: {
        sourceType: 'module'
    },
    parser: "vue-eslint-parser",
    env: {
        browser: true,
        node: true,
        es6: true,
    },
    rules: {
        "no-console": process.env.NODE_ENV === 'production' ? 'error' : 'off',
        "no-undef": process.env.NODE_ENV === 'production' ? 'error' : 'off',
    }
}