<template>
    <div>

        <NuxtLayout>
            <v-container class="text-center">
                <iframe
                    width="600"
                    height="450"
                    src="https://www.youtube.com/embed/ru0K8uYEZWw?start=7"
                    title="YouTube video player"
                    frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen
                ></iframe>

                <h1>index page</h1>

                <Alerts />

                <Icons />

                <Table />
            </v-container>
        </NuxtLayout>

    </div>
</template>

<script>
export default {
    async mounted() {
        const res = await $fetch("http://localhost:8080/hello");
        console.log(res);
    },
};
</script>