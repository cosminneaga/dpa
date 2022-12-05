<template>
    <user-layout>

        <quill-editor ref="editor">

            <template #toolbar>
                <v-btn variant="text" @click="handleSubmit">Save</v-btn>
            </template>

        </quill-editor>

    </user-layout>
</template>

<script lang="ts">
export default {

    async mounted() {
        const req = await this.axios.get('/api/user/me', {
            headers: {
                'x-access-token': this.$cookies.get('X-Access-Token')
            }
        })

        console.log(req);
        
        
    },

    methods: {
        handleSubmit() {       
            const content = this.$refs.editor.getContents()
            console.log(content);
        }
    },
}
</script>