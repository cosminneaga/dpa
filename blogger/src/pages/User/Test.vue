<template>
    <user-layout>
        <h1>test page</h1>

        <textarea
            id="my-editor"
            style="width: 100%;"
        >Hi</textarea>
    </user-layout>
</template>

<script lang="ts">
// https://github.com/kothing/kothing-Editor#install

import "kothing-editor/dist/css/kothing-editor.min.css";
import KothingEditor from "kothing-editor";
import lang from "kothing-editor/lib/lang";
import plugins from "kothing-editor/lib/plugins";

import katex from "katex";
import "katex/dist/katex.min.css";

export default {
    mounted() {
        const editor = KothingEditor.create("my-editor", {
            width: "100%",
            height: "auto",
            lang: lang.en,
            plugins: plugins,
            katex: katex,
            toolbarItem: [
                ["undo", "redo"],
                ["font", "fontSize", "formatBlock"],
                ["bold", "underline", "italic", "strike", "subscript", "superscript", "fontColor", "hiliteColor"],
                ["outdent", "indent", "align", "list", "horizontalRule"],
                ["link", "table", "image", "audio", "video"],
                "/", // Line break
                ["lineHeight", "paragraphStyle", "textStyle"],
                ["showBlocks", "codeView"],
                ["math"],
                ["preview", "print", "fullScreen"],
                ["save", "template"],
                ["removeFormat"],
            ],
            templates: [
                {
                    name: "Template-1",
                    html: "<p>HTML source1</p>",
                },
                {
                    name: "Template-2",
                    html: "<p>HTML source2</p>",
                },
            ],
            charCounter: true,
            mode: "classic",
            font: ["Arial", "Comic Sans MS", "Courier New", "Impact", "Georgia", "tahoma", "Trebuchet MS", "Verdana"],

            stickyToolbar: "100px",
        });

        editor.setContents("");

        editor.onChange = function (contents) {
            console.log(contents);
        };

        console.log(editor);
    },
};
</script>