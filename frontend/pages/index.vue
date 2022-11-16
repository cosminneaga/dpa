<template>
    <div>

        <h1>index page</h1>

    </div>
</template>

<script>
export default {
    async mounted() {
        const res = await $fetch("http://localhost:8080/hello");
        console.log(res);

        const res2 = await $fetch("http://localhost:8080/blogger");
        console.log(res2);
    },
};
</script>