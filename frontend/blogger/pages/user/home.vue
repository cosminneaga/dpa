<template>
    <NuxtLayout name="user">
        <section>
            <br>
            <br>
            User home page
            <br>
            <EditorJS />
        </section>
    </NuxtLayout>
</template>

<script setup>
definePageMeta({
    middleware: ["auth"],
});
</script>

<script>
export default {
    data: () => ({}),
};
</script>
