<template>
  <textarea id="kothing-editor-textarea-1"></textarea>
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

  mounted() {
    const editor = KothingEditor.create("kothing-editor-textarea-1", {
      charCounter: true,
      mode: "classic",
      lang: lang.en,
      plugins: plugins,
      katex: katex,

      width: "100%",
      height: "75vh",

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
          name: "Blog",
          html: `<h1 style="text-align: center;">Title</h1>`,
        },
        {
          name: "Recipe",
          html: `<h2>Ingredients:</h2>
                    
                    <h2>Galery:</h2>
                    
                    <h2>Preparation:</h2>`,
        },
      ],

      font: ["Arial", "Comic Sans MS", "Courier New", "Impact", "Georgia", "tahoma", "Trebuchet MS", "Verdana"],
      fontSize: [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 48, 72],

      imageWidth: "100%",
      imageHeight: "auto",
      imageResizing: true,
      imageFileInput: false,

      videoWidth: "100%",
      videoHeight: "450px",
      videoResizing: true,
      videoFileInput: false,

      stickyToolbar: "0",
    });
    // this.editor = editor;

    const savedContent = localStorage.getItem("blog-data");
    if (savedContent) {
      editor.setContents(JSON.parse(savedContent)["content"]);
    } else {
      if (this.$props.contentSet) {
        editor.setContents(this.$props.contentSet);
      }
    }

    editor.onChange = (contents) => this.onChangeHandle(contents);
  },

  methods: {
    onChangeHandle(contents: any) {
      this.$emit("on-change", contents);
    },
  },
};
</script>

<style lang="scss" scoped>
#kothing-editor-textarea-1 {
  font-family: inherit !important;
  font-size: inherit !important;
}
</style>
