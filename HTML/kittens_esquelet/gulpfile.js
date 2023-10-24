const { series, src, dest } = require('gulp');

// implements sass
const scss = require('gulp-sass')(require('sass'));
// implements minimitzacss
const cleanCSS = require('gulp-clean-css');
// implements minimitzajs
const cleanJS = require('gulp-uglify');

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

// Sass task -> tack 1
function compilaSCSS() {
    return src('sass/*.scss')
        .pipe(scss())
        .pipe(dest('css/'))
}

// WHATCH -> tack 2
function watcher() {
    watch('sass/*.scss', compilaSCSS);
    watch('sass/partials/*.scss', compilaSCSS);
}

// minimitzacss -> tasck 3
function minimitzaCSS() {
    return src('css/*.css')
        .pipe(cleanCSS())
        .pipe(dest('dist/css/'));
}

// minimitzajs -> tasck 4
function minimitzajs() {
    return src('js/*.js')
        .pipe(cleanJS())
        .pipe(dest('dist/js/'));
}


//EXPORTS 
exports.build = build;
exports.default = series(clean, build);
exports.compilaSCSS = compilaSCSS;
exports.watcher = watcher;
exports.minimitzaCSS = minimitzaCSS;
exports.minimitzajs = minimitzajs;
