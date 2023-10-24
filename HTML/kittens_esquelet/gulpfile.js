const { series, src, dest } = require('gulp');

// implements sass
const scss = require('gulp-sass')(require('sass'));

// The `clean` function is not exported so it can be considered a private task.
// It can still be used within the `series()` composition.
function clean(cb) {
    // body omitted
    cb();
}

// The `build` function is exported so it is public and can be run with the `gulp` command.
// It can also be used within the `series()` composition.
function build(cb) {
    // body omitted
    cb();
}

//Sass task
function compilaSCSS(){
    return src('sass/*.scss')
        .pipe(scss())
        .pipe(dest('css/'))
}

//EXPORTS 
exports.build = build;
exports.default = series(clean, build);
exports.compilaSCSS = compilaSCSS;
