<template>
    <section>
        User home page
        <br>
        {{data}}
    </section>
</template>

<script setup>
definePageMeta({
    middleware: ["auth"],
});

const { data } = await useAsyncData("data", () =>
    $fetch("http://localhost:8080/api/blogger/user/me", {
        headers: {
            "X-Access-Token": JSON.parse(localStorage.getItem("blogger")).token,
        },
    })
);
</script>


