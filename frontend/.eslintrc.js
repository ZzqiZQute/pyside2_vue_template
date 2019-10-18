module.exports={
    rules:{
        "no-console":process.env.NODE_ENV==='production'?'error':'off',
        "no-undef":process.env.NODE_ENV==='production'?'error':'off',
    }
}