<template>
    <main id="sample">
        <Editor
            v-model="EditorContent"
            :init="{
                plugins: [
                    'lists',
                    'link',
                    'image',
                    'editimage',
                    'table',
                    'code',
                    'help',
                    'wordcount',
                    'preview',
                    'advlist',
                    'charmap',
                    'emoticons',
                    'fullscreen',
                    'insertdatetime',
                    'media',
                    'pagebreak',
                    'pageembed',
                    'save',
                    'cancel',
                    'searchreplace',
                    'template',
                    'visualblocks',
                ],
                toolbar: [
                    'undo redo styles bold italic underline strikethrough alignleft aligncenter alignright alignjustify | hr | bullist numlist outdent indent | table image link',
                    'emoticons fullscreen insertdatetime media pagebreak save cancel | searchreplace template visualblocks',
                ],
                width: '100%',
                height: '80vh',

                image_title: true,
                images_file_types: 'jpeg,jpg,jpe,jfi,jif,jfif,png,gif,bmp,webp',
                automatic_uploads: true,
                file_picker_types: 'file image media',
                mediaembed_max_width: '100%',
                content_style:
                    'body { font-family:Helvetica,Arial,sans-serif; font-size:16px }',
                // file_picker_callback: (cb: any, value: any, meta: any) =>
                //    filePickerHandler2(cb, value, meta),
                // images_upload_handler: (blobInfo: any, progress: any) =>
                //    imageUploadHandler(blobInfo, progress),
            }"
        />
    </main>
</template>
<script lang="ts">
import Editor from "@tinymce/tinymce-vue";

// https://www.tiny.cloud/docs/tinymce/6/file-image-upload/#example-using-images_upload_handler

export default {
    components: { Editor },

    props: ["contentSet"],

    data: () => ({
        EditorContent: "",
    }),

    watch: {
        EditorContent: function (value) {
            this.$emit("on-change", value);
        },
    },

    beforeMount() {
        const savedContent = localStorage.getItem("blog-data");
        if (savedContent) {
            this.EditorContent = JSON.parse(savedContent)["content"];
        } else {
            if (this.$props.contentSet) {
                this.EditorContent = this.$props.contentSet;
            }
        }
    },

    methods: {
        // will be triggered on upload on images only
        async imageUploadHandler(blobInfo: any, progress: any) {
            console.log("Image has been uploaded");
            console.log(blobInfo);

            console.log(blobInfo.name());
            console.log(blobInfo.filename());
            console.log(blobInfo.blob());

            console.log(progress);
        },

        // will be triggered on pick before the upload on all files
        filePickerHandler(cb: any, value: any, meta: any) {
            console.log("File is about to be picked");

            const input = document.createElement("input");
            input.setAttribute("type", "file");
            input.setAttribute("accept", "image/*");

            input.addEventListener("change", (e: Event) => {
                const file = e.target?.files[0];

                const reader = new FileReader();
                reader.addEventListener("load", () => {
                    /*
                    Note: Now we need to register the blob in TinyMCEs image blob
                    registry. In the next release this part hopefully won't be
                    necessary, as we are looking to handle it internally.
                    */
                    console.log(reader);

                    const id = "blobid" + new Date().getTime();
                    const base64 = reader?.result?.split(",")[1];

                    console.log("FILE TO BASE64");
                    console.log(base64);

                    const blobCache = tinymce.activeEditor.editorUpload.blobCache;
                    const blobInfo = blobCache.create(id, file, base64);
                    blobCache.add(blobInfo);

                    /* call the callback and populate the Title field with the file name */
                    cb(blobInfo.blobUri(), { title: file.name });
                });
                reader.readAsDataURL(file);
            });

            input.click();
        },

        filePickerHandler2(callback: any, value: any, meta: any) {
            console.log(value);

            // Provide file and text for the link dialog
            if (meta.filetype == "file") {
                console.log("File upload");

                callback("mypage.html", { text: "My text" });
            }

            // Provide image and alt text for the image dialog
            if (meta.filetype == "image") {
                console.log("Image upload");

                callback("myimage.jpg", { alt: "My alt text" });
            }

            // Provide alternative source and posted for the media dialog
            if (meta.filetype == "media") {
                console.log("Video upload");

                callback("movie.mp4", { source2: "alt.ogg", poster: "image.jpg" });
            }
        },
    },
};
</script>

<style lang="scss">
.tox-notifications-container {
    display: none !important;
}
</style>
