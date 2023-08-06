(self["webpackChunkDropdownExtension"] = self["webpackChunkDropdownExtension"] || []).push([["lib_index_js"],{

/***/ "./lib/beautifierscript.js":
/*!*********************************!*\
  !*** ./lib/beautifierscript.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   beautifyPythonCode: () => (/* binding */ beautifyPythonCode)
/* harmony export */ });
function splitTokens(code, delimiters) {
    const parts = [];
    let startIndex = 0;
    let currentIndex = 0;
    while (currentIndex < code.length) {
        let currentChar = code[currentIndex];
        if (delimiters.includes(currentChar)) {
            if (currentIndex > startIndex) {
                const part = code.substring(startIndex, currentIndex);
                parts.push(part + currentChar);
            }
            startIndex = currentIndex + 1;
        }
        else {
            const part = code.substring(startIndex, currentIndex);
            if (part.trim() === 'return') {
                const savePos = currentIndex;
                currentIndex = currentIndex + 1;
                currentChar = code[currentIndex];
                let stringCheck = false;
                if (currentChar === '"') {
                    stringCheck = true;
                    currentIndex = currentIndex + 1;
                    currentChar = code[currentIndex];
                }
                if (currentChar === '(') {
                    currentIndex = currentIndex + 1;
                    currentChar = code[currentIndex];
                }
                while (currentIndex < code.length) {
                    currentIndex = currentIndex + 1;
                    if (currentChar === '"' ||
                        currentChar === ')' ||
                        (currentChar === ' ' && !stringCheck)) {
                        break;
                    }
                    currentChar = code[currentIndex];
                }
                const part = code.substring(savePos, currentIndex);
                parts.push('return' + part + '\n');
                startIndex = currentIndex + 1;
            }
        }
        currentIndex++;
    }
    if (currentIndex > startIndex) {
        const lastPart = code.substring(startIndex, currentIndex);
        parts.push(lastPart);
    }
    return parts;
}
function beautifyPythonCode(code) {
    let beautifiedCode = '';
    let indentLevel = 0;
    const lines = splitTokens(code, [',', ':', '|', '\n']);
    const regexIndentIncrease = /^(\s*)(if|for|while|def|class).*:/;
    const regexIndentDecrease = /^(\s*)(elif|else).*:/;
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i].trim();
        if (regexIndentIncrease.test(line)) {
            beautifiedCode += '    '.repeat(indentLevel) + line + '\n';
            indentLevel++;
        }
        else if (regexIndentDecrease.test(line)) {
            indentLevel--;
            beautifiedCode += '    '.repeat(indentLevel) + line + '\n';
            indentLevel++;
        }
        else {
            beautifiedCode += '    '.repeat(indentLevel) + line + '\n';
        }
    }
    return beautifiedCode;
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _beautifierscript__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./beautifierscript */ "./lib/beautifierscript.js");
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/mainmenu */ "webpack/sharing/consume/default/@jupyterlab/mainmenu");
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _linksharing__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./linksharing */ "./lib/linksharing.js");






function presentDialog(message) {
    const dialog = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog({
        title: message,
        buttons: [
            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.okButton({ label: 'OK', displayType: 'default', accept: true })
        ]
    });
    dialog.launch();
}
const plugin = {
    id: 'Dropdown menu extension:plugin',
    description: 'A JupyterLab dropdown extension for additional jupyterlab features!',
    autoStart: true,
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.INotebookTracker, _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_2__.IMainMenu],
    activate: (app, palette, notebookTracker, mainMenu) => {
        const { commands } = app;
        const beautifyCommand = 'beautify:python-code';
        commands.addCommand(beautifyCommand, {
            label: 'Beautify Python Code',
            execute: () => {
                const current = notebookTracker.currentWidget;
                if (current === null) {
                    return;
                }
                const cell = current.content.activeCell;
                if (cell === null) {
                    return;
                }
                let codeBefore = cell.model.toJSON().source;
                if (Array.isArray(codeBefore)) {
                    codeBefore = codeBefore.join('\n');
                }
                const codeAfter = (0,_beautifierscript__WEBPACK_IMPORTED_MODULE_4__.beautifyPythonCode)(codeBefore);
                presentDialog('Selected Code Beautified');
                app.commands.execute('notebook:replace-selection', { text: codeAfter });
            }
        });
        palette.addItem({
            command: beautifyCommand,
            category: 'Extension Commands'
        });
        const anomalyCommand = 'anomaly-detection:get-csv';
        commands.addCommand(anomalyCommand, {
            label: 'Get Anomalies from CSV',
            execute: () => {
                fetch('http://localhost:5000/anomaly', {
                    method: 'POST'
                })
                    .then(response => response.text())
                    .then(data => presentDialog(data))
                    .catch(error => {
                    console.error('Error:', error);
                });
            }
        });
        palette.addItem({
            command: anomalyCommand,
            category: 'Extension Commands'
        });
        const regenCommand = 'regen-dataframe:get-csv';
        commands.addCommand(regenCommand, {
            label: 'Regenerate DataFrame from CSV',
            execute: () => {
                fetch('http://localhost:5000/regen', {
                    method: 'POST'
                })
                    .then(response => response.text())
                    .then(data => presentDialog(data))
                    .catch(error => {
                    console.error('Error:', error);
                });
            }
        });
        palette.addItem({
            command: regenCommand,
            category: 'Extension Commands'
        });
        const columnCommand = 'column-correlator:get-csv';
        commands.addCommand(columnCommand, {
            label: 'Correlate columns from CSV',
            execute: () => {
                fetch('http://localhost:5000/correlator', {
                    method: 'POST'
                })
                    .then(response => response.text())
                    .then(data => presentDialog(data))
                    .catch(error => {
                    console.error('Error:', error);
                });
            }
        });
        palette.addItem({
            command: columnCommand,
            category: 'Extension Commands'
        });
        const missingCommand = 'missing-filler:get-csv';
        commands.addCommand(missingCommand, {
            label: 'Fill NaN values from CSV',
            execute: () => {
                fetch('http://localhost:5000/missing', {
                    method: 'POST'
                })
                    .then(response => response.text())
                    .then(data => presentDialog(data))
                    .catch(error => {
                    console.error('Error:', error);
                });
            }
        });
        palette.addItem({
            command: missingCommand,
            category: 'Extension Commands'
        });
        const sharingCommand = 'jp-option-4:main-menu';
        commands.addCommand(sharingCommand, {
            label: 'Sharing',
            execute: async (args) => {
                var _a, _b;
                const { shareChoice } = args;
                const current = notebookTracker.currentWidget;
                if (current === null) {
                    alert('There is no active notebook.');
                    return;
                }
                const cell = current.content.activeCell;
                if (cell === null) {
                    alert('There is no active cell in the notebook.');
                    return;
                }
                let codeBefore = cell.model.toJSON().source;
                if (Array.isArray(codeBefore)) {
                    codeBefore = codeBefore.join('\n');
                }
                if (!codeBefore) {
                    alert('The active cell is empty. There is no code to share.');
                    return;
                }
                const sessionContext = current.sessionContext;
                const future = (_b = (_a = sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel) === null || _b === void 0 ? void 0 : _b.requestExecute({
                    code: codeBefore
                });
                let codeOutput = '';
                if (future) {
                    future.onIOPub = msg => {
                        if (msg.header.msg_type === 'execute_result') {
                            const executeResultMsg = msg;
                            codeOutput += executeResultMsg.content.data['text/plain'] + '\n';
                        }
                        else if (msg.header.msg_type === 'display_data') {
                            const displayDataMsg = msg;
                            codeOutput += displayDataMsg.content.data['text/plain'] + '\n';
                        }
                        else if (msg.header.msg_type === 'stream') {
                            const streamMsg = msg;
                            codeOutput += streamMsg.content.text + '\n';
                        }
                    };
                    await future.done;
                }
                let repoFileContent = '';
                if (shareChoice === '1') {
                    repoFileContent = codeBefore.toString();
                }
                else if (shareChoice === '2') {
                    repoFileContent = codeOutput;
                }
                else if (shareChoice === '3') {
                    repoFileContent = `# Code:\n\n${codeBefore}\n\n# Output:\n\n${codeOutput}`;
                }
                else {
                    alert('Invalid choice. Please enter 1, 2 or 3.');
                    return;
                }
                let tokenDialog = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.InputDialog.getText({
                    title: 'Enter your GitHub token:'
                });
                while (tokenDialog.value === null || tokenDialog.value === '') {
                    if (tokenDialog.button.accept) {
                        await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showErrorMessage)('Input Error', 'GitHub token must not be empty.');
                        tokenDialog = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.InputDialog.getText({
                            title: 'Enter your GitHub token:'
                        });
                    }
                    else {
                        return;
                    }
                }
                const token = tokenDialog.value;
                let ownerDialog = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.InputDialog.getText({
                    title: 'Enter the GitHub repository owner:'
                });
                while (ownerDialog.value === null || ownerDialog.value === '') {
                    if (ownerDialog.button.accept) {
                        await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showErrorMessage)('Input Error', 'GitHub repository owner must not be empty.');
                        ownerDialog = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.InputDialog.getText({
                            title: 'Enter the GitHub repository owner:'
                        });
                    }
                    else {
                        return;
                    }
                }
                const owner = ownerDialog.value;
                let repoDialog = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.InputDialog.getText({
                    title: 'Enter the GitHub repository name:'
                });
                while (repoDialog.value === null || repoDialog.value === '') {
                    if (repoDialog.button.accept) {
                        await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showErrorMessage)('Input Error', 'GitHub repository name must not be empty.');
                        repoDialog = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.InputDialog.getText({
                            title: 'Enter the GitHub repository name:'
                        });
                    }
                    else {
                        return;
                    }
                }
                const repo = repoDialog.value;
                let pathDialog = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.InputDialog.getText({
                    title: 'Enter the path where you want to create the file in the repository:'
                });
                while (pathDialog.value === null || pathDialog.value === '') {
                    if (pathDialog.button.accept) {
                        await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showErrorMessage)('Input Error', 'Repository file path must not be empty.');
                        pathDialog = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.InputDialog.getText({
                            title: 'Enter the path where you want to create the file in the repository:'
                        });
                    }
                    else {
                        return;
                    }
                }
                const path = pathDialog.value;
                let messageDialog = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.InputDialog.getText({
                    title: 'Enter a commit message:'
                });
                while (messageDialog.value === null || messageDialog.value === '') {
                    if (messageDialog.button.accept) {
                        await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showErrorMessage)('Input Error', 'Commit message must not be empty.');
                        messageDialog = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.InputDialog.getText({
                            title: 'Enter a commit message:'
                        });
                    }
                    else {
                        return;
                    }
                }
                const message = messageDialog.value;
                const repoFileUrl = await (0,_linksharing__WEBPACK_IMPORTED_MODULE_5__.createRepoFile)(token, owner, repo, path, repoFileContent, message);
                if (repoFileUrl) {
                    presentDialog(`Your sharable link is: ${repoFileUrl}`);
                }
                else {
                    presentDialog('Failed to create a repo file. Please check your inputs and try again.');
                }
            }
        });
        // Create sub-menu options
        const shareCodeCommand = 'share:code';
        commands.addCommand(shareCodeCommand, {
            label: 'Share Code',
            execute: () => commands.execute(sharingCommand, { shareChoice: '1' })
        });
        palette.addItem({
            command: shareCodeCommand,
            category: 'Extension Commands'
        });
        const shareOutputCommand = 'share:output';
        commands.addCommand(shareOutputCommand, {
            label: 'Share Output',
            execute: () => commands.execute(sharingCommand, { shareChoice: '2' })
        });
        palette.addItem({
            command: shareOutputCommand,
            category: 'Extension Commands'
        });
        const shareBothCommand = 'share:both';
        commands.addCommand(shareBothCommand, {
            label: 'Share Both',
            execute: () => commands.execute(sharingCommand, { shareChoice: '3' })
        });
        palette.addItem({
            command: shareBothCommand,
            category: 'Extension Commands'
        });
        const sharingSubMenu = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__.Menu({ commands });
        sharingSubMenu.title.label = 'Sharing';
        sharingSubMenu.addItem({ command: shareCodeCommand });
        sharingSubMenu.addItem({ command: shareOutputCommand });
        sharingSubMenu.addItem({ command: shareBothCommand });
        const myMenu = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__.Menu({ commands });
        myMenu.title.label = 'Additional Features';
        myMenu.addItem({ command: beautifyCommand });
        myMenu.addItem({ command: anomalyCommand });
        myMenu.addItem({ command: regenCommand });
        myMenu.addItem({ command: columnCommand });
        myMenu.addItem({ command: missingCommand });
        myMenu.addItem({ type: 'submenu', submenu: sharingSubMenu });
        mainMenu.addMenu(myMenu, true, { rank: 1000 });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./lib/linksharing.js":
/*!****************************!*\
  !*** ./lib/linksharing.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   createRepoFile: () => (/* binding */ createRepoFile)
/* harmony export */ });
/* harmony import */ var _octokit_rest__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @octokit/rest */ "webpack/sharing/consume/default/@octokit/rest/@octokit/rest");
/* harmony import */ var _octokit_rest__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_octokit_rest__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _octokit_request_error__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @octokit/request-error */ "./node_modules/@octokit/request-error/dist-web/index.js");


async function createRepoFile(token, owner, repo, path, content, message = 'Add file') {
    var _a, _b;
    const octokit = new _octokit_rest__WEBPACK_IMPORTED_MODULE_0__.Octokit({ auth: token });
    const fileContentBase64 = btoa(unescape(encodeURIComponent(content)));
    let sha;
    try {
        const { data } = await octokit.repos.getContent({
            owner: owner,
            repo: repo,
            path: path
        });
        if (Array.isArray(data)) {
            alert('The path you provided is a directory.');
            return null;
        }
        else {
            sha = data.sha;
        }
    }
    catch (error) {
        if (error instanceof _octokit_request_error__WEBPACK_IMPORTED_MODULE_1__.RequestError && error.status === 404) {
            // File does not exist so continue with creation.
        }
        else {
            console.log('Error getting file: ', error);
            return null;
        }
    }
    const file = {
        owner: owner,
        repo: repo,
        path: path,
        sha,
        message: message,
        content: fileContentBase64
    };
    if (sha) {
        file['sha'] = sha;
    }
    try {
        const response = await octokit.repos.createOrUpdateFileContents(file);
        return ((_b = (_a = response.data) === null || _a === void 0 ? void 0 : _a.content) === null || _b === void 0 ? void 0 : _b.html_url) || null;
    }
    catch (error) {
        console.error(error);
        return null;
    }
}


/***/ }),

/***/ "./node_modules/@octokit/request-error/dist-web/index.js":
/*!***************************************************************!*\
  !*** ./node_modules/@octokit/request-error/dist-web/index.js ***!
  \***************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   RequestError: () => (/* binding */ RequestError)
/* harmony export */ });
/* harmony import */ var deprecation__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! deprecation */ "./node_modules/deprecation/dist-web/index.js");
/* harmony import */ var once__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! once */ "./node_modules/once/once.js");
/* harmony import */ var once__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(once__WEBPACK_IMPORTED_MODULE_0__);
// pkg/dist-src/index.js


var logOnceCode = once__WEBPACK_IMPORTED_MODULE_0___default()((deprecation) => console.warn(deprecation));
var logOnceHeaders = once__WEBPACK_IMPORTED_MODULE_0___default()((deprecation) => console.warn(deprecation));
var RequestError = class extends Error {
  constructor(message, statusCode, options) {
    super(message);
    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, this.constructor);
    }
    this.name = "HttpError";
    this.status = statusCode;
    let headers;
    if ("headers" in options && typeof options.headers !== "undefined") {
      headers = options.headers;
    }
    if ("response" in options) {
      this.response = options.response;
      headers = options.response.headers;
    }
    const requestCopy = Object.assign({}, options.request);
    if (options.request.headers.authorization) {
      requestCopy.headers = Object.assign({}, options.request.headers, {
        authorization: options.request.headers.authorization.replace(
          / .*$/,
          " [REDACTED]"
        )
      });
    }
    requestCopy.url = requestCopy.url.replace(/\bclient_secret=\w+/g, "client_secret=[REDACTED]").replace(/\baccess_token=\w+/g, "access_token=[REDACTED]");
    this.request = requestCopy;
    Object.defineProperty(this, "code", {
      get() {
        logOnceCode(
          new deprecation__WEBPACK_IMPORTED_MODULE_1__.Deprecation(
            "[@octokit/request-error] `error.code` is deprecated, use `error.status`."
          )
        );
        return statusCode;
      }
    });
    Object.defineProperty(this, "headers", {
      get() {
        logOnceHeaders(
          new deprecation__WEBPACK_IMPORTED_MODULE_1__.Deprecation(
            "[@octokit/request-error] `error.headers` is deprecated, use `error.response.headers`."
          )
        );
        return headers || {};
      }
    });
  }
};



/***/ }),

/***/ "./node_modules/deprecation/dist-web/index.js":
/*!****************************************************!*\
  !*** ./node_modules/deprecation/dist-web/index.js ***!
  \****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   Deprecation: () => (/* binding */ Deprecation)
/* harmony export */ });
class Deprecation extends Error {
  constructor(message) {
    super(message); // Maintains proper stack trace (only available on V8)

    /* istanbul ignore next */

    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, this.constructor);
    }

    this.name = 'Deprecation';
  }

}




/***/ }),

/***/ "./node_modules/once/once.js":
/*!***********************************!*\
  !*** ./node_modules/once/once.js ***!
  \***********************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var wrappy = __webpack_require__(/*! wrappy */ "./node_modules/wrappy/wrappy.js")
module.exports = wrappy(once)
module.exports.strict = wrappy(onceStrict)

once.proto = once(function () {
  Object.defineProperty(Function.prototype, 'once', {
    value: function () {
      return once(this)
    },
    configurable: true
  })

  Object.defineProperty(Function.prototype, 'onceStrict', {
    value: function () {
      return onceStrict(this)
    },
    configurable: true
  })
})

function once (fn) {
  var f = function () {
    if (f.called) return f.value
    f.called = true
    return f.value = fn.apply(this, arguments)
  }
  f.called = false
  return f
}

function onceStrict (fn) {
  var f = function () {
    if (f.called)
      throw new Error(f.onceError)
    f.called = true
    return f.value = fn.apply(this, arguments)
  }
  var name = fn.name || 'Function wrapped with `once`'
  f.onceError = name + " shouldn't be called more than once"
  f.called = false
  return f
}


/***/ }),

/***/ "./node_modules/wrappy/wrappy.js":
/*!***************************************!*\
  !*** ./node_modules/wrappy/wrappy.js ***!
  \***************************************/
/***/ ((module) => {

// Returns a wrapper function that returns a wrapped callback
// The wrapper function should do some stuff, and return a
// presumably different callback function.
// This makes sure that own properties are retained, so that
// decorations and such are not lost along the way.
module.exports = wrappy
function wrappy (fn, cb) {
  if (fn && cb) return wrappy(fn)(cb)

  if (typeof fn !== 'function')
    throw new TypeError('need wrapper function')

  Object.keys(fn).forEach(function (k) {
    wrapper[k] = fn[k]
  })

  return wrapper

  function wrapper() {
    var args = new Array(arguments.length)
    for (var i = 0; i < args.length; i++) {
      args[i] = arguments[i]
    }
    var ret = fn.apply(this, args)
    var cb = args[args.length-1]
    if (typeof ret === 'function' && ret !== cb) {
      Object.keys(cb).forEach(function (k) {
        ret[k] = cb[k]
      })
    }
    return ret
  }
}


/***/ })

}]);
//# sourceMappingURL=lib_index_js.c2de762d740da5c9dc45.js.map