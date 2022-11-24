<template>
    <section>
        <div
            class="mt-10"
            id="editorjs"
            style="border: 2px solid black;"
        />

        <v-btn @click="save">Save</v-btn>
    </section>
</template>
<script>
// https://github.com/editor-js

import EditorJS from "@editorjs/editorjs";
import Header from "@editorjs/header";
import LinkTool from "@editorjs/link";
import RawHTML from "@editorjs/raw";
import SimpleImage from "@editorjs/simple-image";
import Image from "@editorjs/image";
import Checklist from "@editorjs/checklist";
import List from "@editorjs/list";
import NestedList from "@editorjs/nested-list";
import Embed from "@editorjs/embed";
import Quote from "@editorjs/quote";
import InlineCode from "@editorjs/inline-code";
import Marker from "@editorjs/marker";
import Personality from "@editorjs/personality";
import Underline from "@editorjs/underline";
import Footnotes from "@editorjs/footnotes";
import TextVariantTune from "@editorjs/text-variant-tune";
import Table from "@editorjs/table";
import Attaches from "@editorjs/attaches";
import Delimiter from "@editorjs/delimiter";
import Warning from "@editorjs/warning";
import Paragraph from "@editorjs/paragraph";
/*
table

*/

export default {
    data: () => ({
        editor: null,
    }),

    methods: {
        save() {
            this.editor
                .save()
                .then((output) => {
                    console.log(output);
                })
                .catch((error) => {
                    console.error(error);
                });
        },
    },

    mounted() {
        const editor = new EditorJS({
            holder: "editorjs",
            autofocus: true,
            logLevel: "VERBOSE",
            tools: {
                heading: Header,
                link: LinkTool,
                raw: RawHTML,
                image: Image,
                checklist: Checklist,
                list: {
                    class: NestedList,
                    inlineToolbar: true,
                },
                embed: Embed,
                quote: Quote,
                marker: Marker,
                inlineCode: InlineCode,
                personality: Personality,
                underline: Underline,
                footnotes: Footnotes,
                textVariant: TextVariantTune,
                table: Table,
                delimiter: Delimiter,
                paragraph: {
                    class: Paragraph,
                    inlineToolbar: true,
                },
                warning: {
                    class: Warning,
                    inlineToolbar: true,
                    config: {
                        title: "WARNING",
                        message:
                            "Avoid using this method just for lulz. It can be very dangerous opposite your daily fun stuff.",
                    },
                },
                attaches: {
                    class: Attaches,
                    config: {
                        endpoint: "brrr",
                    },
                },
            },
            tunes: ["textVariant"],
        });

        this.editor = editor;
    },
};
</script>
  