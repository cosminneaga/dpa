<template>
    <textarea
        ref="kothingEditorTextarea"
        id="kothing-editor-textarea-1"
    >{{ contentSet }}</textarea>
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
    props: ["contentSet"],
    data: () => ({ editor: {} }),

    watch: {
        "$props.contentSet": function (content) {
            this.onSetContent(content);
        },
    },

    mounted() {
        const editor = KothingEditor.create("kothing-editor-textarea-1", {
            width: "100%",
            height: "60vh",
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
        this.editor = editor;

        editor.onChange = (contents) => this.onChangeHandle(contents);

        const savedContent = localStorage.getItem("blog-data");
        if (savedContent) {
            editor.setContents(JSON.parse(savedContent)["content"]);
        }
    },

    methods: {
        onChangeHandle(contents: any) {
            this.$emit("on-change", contents);
        },
    },
};
</script>